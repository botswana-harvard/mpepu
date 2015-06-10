from django.db.models import get_model

from config.celery import app

from edc.map.exceptions import MapperError
from edc.constants import NEW


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
                registered_subject__subject_identifier=consent.subject_identifier,
                may_follow_up='Yes')

            options.update(
                first_name=consent.first_name,
                initials=consent.initials,
                cell=locator.subject_cell,
                alt_cell=get_alt_cell(locator),
                consent=consent,
#                 age_in_years=target_household_member.age_in_years,
#                 gender=target_household_member.gender,
                subject_identifier=consent.subject_identifier,
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
        if call_list.call_status == 'New':
            call_list.call_status = 'Open'
        if call_list.call_attempts == 3:
            call_list.call_status = 'Closed'
            call_list.contacted = True
        try:
            call_list.save()
        except Exception as e:
            print('Call not logged for particpant {}'.format(call_list.subject_identifier))


def get_alt_cell(locator):
    if locator.subject_cell_alt:
        return locator.subject_cell_alt
    if locator.subject_phone_alt:
        return locator.subject_phone_alt
    if locator.contact_cell:
        return locator.contact_cell
    if locator.contact_phone:
        return locator.contact_phone
