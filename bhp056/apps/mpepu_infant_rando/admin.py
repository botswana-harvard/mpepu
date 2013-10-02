from django.contrib import admin
from edc.base.admin.admin import BaseModelAdmin
from models import InfantRando


class InfantRandoAdmin(BaseModelAdmin):

    list_display = ('sid', 'subject_identifier', 'infant_initials', 'site', 'stratum', 'bf_duration', 'randomization_datetime', 'user_modified', 'dispensed')
    search_fields = ('sid', 'subject_identifier', 'dispensed', 'infant_initials')
    list_filter = ('randomization_datetime', 'site', 'stratum')
    readonly_fields = (
        'sid',
        'subject_identifier',
        'feeding_choice',
        'haart_status',
        'infant_initials',
        'stratum',
        'rx',
        'site',
        'bf_duration',
        'randomization_datetime')
admin.site.register(InfantRando, InfantRandoAdmin)
