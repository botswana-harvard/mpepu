from django.contrib import admin
from django.core.exceptions import ValidationError

from edc.subject.consent.admin import BaseConsentModelAdmin
from edc.subject.registration.models import RegisteredSubject

from apps.mpepu_maternal.models import MaternalConsent
from apps.mpepu_maternal.admin import MaternalVisitModelAdmin

from ..models import ResistanceConsent, ResistanceEligibility, ResistanceDisc
from ..forms import ResistanceConsentForm, ResistanceEligibilityForm, ResistanceDiscForm


class ResistanceConsentAdmin(BaseConsentModelAdmin):

    form = ResistanceConsentForm

    def __init__(self, *args, **kwargs):

        super(ResistanceConsentAdmin, self).__init__(*args, **kwargs)
        self.search_fields = ['id', 'subject_identifier', 'first_name', 'last_name', 'identity', ]
        self.list_display = ['subject_identifier', 'first_name', 'initials', 'gender', 'dob',
                                 'consent_datetime', 'created', 'modified', 'user_created', 'user_modified', ]

        self.fields = [
            'subject_identifier',
            'first_name',
            'last_name',
            'initials',
            'witness_name',
            'consent_datetime',
            'study_site',
            'gender',
            'dob',
            'guardian_name',
            'is_dob_estimated',
            'identity',
            'identity_type',
            'may_store_samples',
            'comment', ]
        self.radio_fields = {
            "gender": admin.VERTICAL,
            "study_site": admin.VERTICAL,
            "is_dob_estimated": admin.VERTICAL,
            "identity_type": admin.VERTICAL,
            "may_store_samples": admin.VERTICAL,
            }

    def save_model(self, request, obj, form, change):
        """Confirms maternal_consent exists."""
        if not change:
            # these fields are encrypted?
            if MaternalConsent.objects.filter(first_name=obj.first_name, gender=obj.gender, identity=obj.identity, dob=obj.dob).exists():
                maternal_consent = MaternalConsent.objects.get(first_name=obj.first_name, gender=obj.gender, identity=obj.identity, dob=obj.dob)
                obj.subject_identifier = maternal_consent.subject_identifier
                if RegisteredSubject.objects.filter(subject_identifier=obj.subject_identifier).exists():
                    obj.registered_subject = RegisteredSubject.objects.get(subject_identifier=obj.subject_identifier)
            else:
                raise ValidationError('Unable to locate Mpepu Maternal consent using the first_name, gender, dob and identity number provided.')
        super(ResistanceConsentAdmin, self).save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "registered_subject":
            kwargs["queryset"] = RegisteredSubject.objects.filter(id__exact=request.GET.get('registered_subject'))
        return super(ResistanceConsentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(ResistanceConsent, ResistanceConsentAdmin)


class ResistanceEligibilityAdmin(MaternalVisitModelAdmin):

    form = ResistanceEligibilityForm

    fields = (
        "maternal_visit",
        "report_datetime",
        "co_enrolled",
        "status_evidence",
        "lates_cd4",
        "who_illness",
        "stopped_arv",
        "incarcerated",
        )
    radio_fields = {
        "co_enrolled": admin.VERTICAL,
        "status_evidence": admin.VERTICAL,
        "who_illness": admin.VERTICAL,
        "stopped_arv": admin.VERTICAL,
        "incarcerated": admin.VERTICAL,
        }
admin.site.register(ResistanceEligibility, ResistanceEligibilityAdmin)


class ResistanceDiscAdmin(MaternalVisitModelAdmin):

    form = ResistanceDiscForm

    fields = (
        "maternal_visit",
        "regimen",
        "date_arv_started",
        "discontinued_by",
        "stopped_once",
        "last_arv_date",
        "last_ftc_date",
        "last_tdf_date",
        "last_3tc_date",
        "as_prescribed",
        "info_source",
    )
    radio_fields = {'regimen': admin.VERTICAL,
                     'discontinued_by': admin.VERTICAL,
                     'stopped_once': admin.VERTICAL,
                     'as_prescribed': admin.VERTICAL}
admin.site.register(ResistanceDisc, ResistanceDiscAdmin)
