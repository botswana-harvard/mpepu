from datetime import datetime

from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.contrib import messages

from edc.export.classes import ExportAsCsv

from .utils import update_call_list, call_participant, contacted, verified


def update_call_list_action(modeladmin, request, queryset):
    update_call_list()
update_call_list_action.short_description = "Update Call List"


def call_participant_action(modeladmin, request, queryset):
    call_participant(queryset)
call_participant.short_description = "Call participant"


def contacted_action(modeladmin, request, queryset):
    contacted(queryset)
contacted_action.short_description = "Contacted"


def verified_action(modeladmin, request, queryset):
    verified(request, queryset)
verified_action.short_description = "Verify"
