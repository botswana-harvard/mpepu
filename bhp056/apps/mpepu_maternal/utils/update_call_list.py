from django.db.models import get_model
from django.utils.datastructures import SortedDict
from django.core.exceptions import ObjectDoesNotExist

from config.celery import app

from edc.map.exceptions import MapperError
from edc.constants import NEW, CLOSED, OPEN


@app.task
def update_call_list(label, verbose=True):
    """Adds information from SubjectConsent instances from the specified survey to the
    CallList model for the current survey.

    If there is no SubjectLocator or subject_locator.may_follow='No', the subject is not added
    to the call list.

    If needed, the household member for the next survey will be created.
    See (HouseholdStructure manager method add_household_members_from_survey).
    """
    CallList = get_model('mpepu_maternal', 'CallList')
    MaternalConsent = get_model('mpepu_maternal', 'MaternalConsent')
    MaternalLocator = get_model('mpepu_maternal', 'MaternalLocator')

    options = {}
    n = 0

    total = MaternalConsent.objects.all().count()
    print 'Pulled {} consents.'.format(total)
    for consent in MaternalConsent.objects.all().order_by('subject_identifier'):
        n += 1
        try:
            locator = MaternalLocator.objects.get(
                registered_subject__subject_identifier=consent.subject_identifier,)
#                 may_follow_up='Yes')

            options.update(
                first_name=consent.first_name,
                initials=consent.initials,
                cell=locator.subject_cell,
                alt_cell=get_alt_cell(locator),
                consent=consent,
                maternal_identifier=consent.subject_identifier,
                infant_identifier=infant_identifier(consent),
                infant_death=infant_death(consent),
                maternal_death=maternal_death(consent),
#                 age_in_years=target_household_member.age_in_years,
#                 gender=target_household_member.gender,
                app_label=MaternalConsent._meta.app_label,
                object_name=MaternalConsent._meta.object_name,
                object_pk=consent.pk,
                consent_datetime=consent.consent_datetime,
                call_status=NEW,
                label=label,
                hostname_created=consent.hostname_created,
                user_created=consent.user_created,
            )
            try:
                call_list = CallList.objects.get(consent=consent, label=label)
                if verbose:
                    print '{}/{}    {} already added to call list'.format(n, total, consent.subject_identifier)

            except CallList.DoesNotExist:
                call_list = CallList.objects.create(**options)
                if verbose:
                    print '{}/{} Added {} to call list'.format(n, total, consent.subject_identifier)
            call_list.hostname_created = consent.hostname_created
            call_list.user_created = consent.user_created
            call_list.save()
        except MaternalLocator.DoesNotExist:
            print('Not adding {} to call list. No contact information or may not '
                  'follow (SubjectLocator)'.format(consent))


@app.task
def call_participant(query_set):
    for call_list in query_set:
        call_list.call_attempts += 1
        if call_list.call_attempts < 3:
            call_list.call_status = OPEN
        else:
            call_list.call_status = CLOSED

        try:
            call_list.save()
        except Exception as e:
            print('Call not logged for particpant {}'.format(call_list.subject_identifier))


@app.task
def contacted(query_set):
    for call_list in query_set:
        call_list.contacted = True
        call_list.call_status = CLOSED
        try:
            call_list.save()
        except Exception as e:
            print('Call not logged for particpant {}'.format(call_list.subject_identifier))


@app.Task
def verified(query_set):
    for call_list in query_set:
        call_list.verified = True
        try:
            call_list.save()
        except Exception as e:
            print('Call not logged for participant {}'.format(call_list.subject_identifier))


def infant_identifier(consent):
    RegisteredSubject = get_model('registration', 'RegisteredSubject')
    registered_subject = RegisteredSubject.objects.filter(relative_identifier=consent.subject_identifier)
    if len(registered_subject) == 0:
        return ("No infant registered")
    elif len(registered_subject) == 1:
        return ("{} : {}".format(registered_subject[0].subject_identifier, rando_arm(registered_subject[0].subject_identifier)))
    else:
        subject = ""
        for subj in registered_subject:
            subject +=("{} : {}\n".format(subj.subject_identifier, rando_arm(subj.subject_identifier)))
#             subject[subj.subject_identifier] = rando_arm(subj.subject_identifier)
        return subject


def rando_arm(infant_identifier):
    InfantRando = get_model('mpepu_infant_rando', 'InfantRando')
    infant_rando = InfantRando.objects.filter(subject_identifier=infant_identifier)
    if infant_rando:
        return infant_rando[0].rx


def infant_death(consent):
    RegisteredSubject = get_model('registration', 'RegisteredSubject')
    InfantDeath = get_model('mpepu_infant', 'InfantDeath')
    registered_subject = RegisteredSubject.objects.filter(relative_identifier=consent.subject_identifier)
    death = {}
    for subject in registered_subject:
        try:
            infant_death = InfantDeath.objects.get(registered_subject__subject_identifier=subject.subject_identifier)
            subject_identifier = subject.subject_identifier
            death.update(
                subject_identifier="deceased",
            )
        except InfantDeath.DoesNotExist:
            pass
    return death


def maternal_death(consent):
    MaternalDeath = get_model('mpepu_maternal', 'MaternalDeath')
    try:
        maternal_death = MaternalDeath.objects.get(registered_subject__subject_identifier=consent.subject_identifier)
        return True
    except MaternalDeath.DoesNotExist:
        return False


def get_alt_cell(locator):
    if locator.subject_cell_alt:
        return locator.subject_cell_alt
    if locator.subject_phone_alt:
        return locator.subject_phone_alt
    if locator.contact_cell:
        return locator.contact_cell
    if locator.contact_phone:
        return locator.contact_phone
