from django.contrib import admin
from collections import OrderedDict

from edc.export.actions import export_as_csv_action
from edc.subject.consent.admin import BaseConsentModelAdmin, BaseConsentUpdateModelAdmin, BaseConsentUpdateInlineAdmin

from ..models import MaternalConsent, MaternalConsentUpdate
from ..forms import MaternalConsentForm, MaternalConsentUpdateForm


class MaternalConsentUpdateInlineAdmin(BaseConsentUpdateInlineAdmin):
    model = MaternalConsentUpdate
    form = MaternalConsentUpdateForm
    extra = 0


class MaternalConsentUpdateAdmin(BaseConsentUpdateModelAdmin):

    form = MaternalConsentUpdateForm
    consent_name = 'maternal_consent'

admin.site.register(MaternalConsentUpdate, MaternalConsentUpdateAdmin)


class MaternalConsentAdmin(BaseConsentModelAdmin):

    form = MaternalConsentForm
    inlines = [MaternalConsentUpdateInlineAdmin, ]

    def __init__(self, *args, **kwargs):
        super(MaternalConsentAdmin, self).__init__(*args, **kwargs)
        # remove these fields from admin fields list, default values should apply
        for fld in ['witness_name', 'is_literate', 'guardian_name']:
            self.fields.remove(fld)

    actions = [export_as_csv_action(description="CSV Export of Maternal Consent",
        fields=[],
        delimiter=',',
        exclude=['created', 'modified', 'user_created', 'user_modified', 'revision', 'id', 'hostname_created', 'hostname_modified', 'last_name', 'identity', 'confirm_identity', 'first_name' ],
        extra_fields=OrderedDict(
            {'subject_identifier': 'registered_subject__subject_identifier',
             'gender': 'registered_subject__gender',
             'dob': 'registered_subject__dob',
             'registered': 'registered_subject__registration_datetime'}),
        )]

admin.site.register(MaternalConsent, MaternalConsentAdmin)
