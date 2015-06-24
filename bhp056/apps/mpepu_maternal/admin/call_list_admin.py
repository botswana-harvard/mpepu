from django.contrib import admin

from edc.base.modeladmin.admin import BaseModelAdmin
from edc.subject.registration.models import RegisteredSubject

from ..actions import update_call_list_action, call_participant_action, contacted_action
from ..forms import CallListForm
from ..models import CallList, MaternalConsent


class CallListAdmin(BaseModelAdmin):

    form = CallListForm
    date_hierarchy = 'created'
    fields = (
        'maternal_identifier',
        'call_attempts',
        'label',
        'call_status',
        'call_outcome',
        'contacted'
    )
    radio_fields = {
        'call_status': admin.VERTICAL,
    }

    list_display = (
        'maternal_identifier',
        'first_name',
        'initials',
        'infant_identifier',
        'call_attempts',
        'call_status',
        'call_outcome',
        'contacted',
        'cell',
        'consent_datetime',
        'label',
    )

    list_filter = (
        'label',
        'call_attempts',
        'call_status',
        'rando_arm',
        'created',
        'consent_datetime',
        'hostname_created',
        'user_created',
    )

    readonly_fields = (
        'maternal_identifier',
        'call_attempts',
    )

    search_fields = ('maternal_identifier',
                     'first_name',
                     'initials',
                     )

    actions = [update_call_list_action, call_participant_action, contacted_action]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "consent":
            if request.GET.get('registered_subject'):
                maternal_subject_identifier = RegisteredSubject.objects.get(id=request.GET.get('registered_subject')).subject_identifier
                kwargs["queryset"] = MaternalConsent.objects.filter(subject_identifier=maternal_subject_identifier)
        return super(CallListAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(CallList, CallListAdmin)
