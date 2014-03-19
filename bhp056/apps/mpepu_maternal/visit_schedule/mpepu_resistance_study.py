from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple
from edc.utils.constants import SHOW_FORM, HIDE_FORM

from ..models import MaternalVisit, ResistanceConsent


class MpepuResistanceStudyVisitSchedule(VisitScheduleConfiguration):

    name = 'resistance visit schedule'
    app_label = 'mpepu_maternal'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'maternal_resistance': MembershipFormTuple('maternal_resistance', ResistanceConsent, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Resistance Study': ScheduleGroupTuple('Resistance Study', 'maternal_resistance', None, None),
        })
    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict()

    visit_definitions['2030R'] = {
            'title': 'Maternal ARV Resistance',
            'time_point': 30,
            'base_interval': 3,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Resistance Study',
            'instructions': None,
            'requisitions': (
                             ),
            'entries': (
                #additional forms for the TAB study
                EntryTuple(10L, u'mpepu_maternal', u'resistanceeligibility', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'resistancedisc', SHOW_FORM),
            )}
site_visit_schedules.register(MpepuResistanceStudyVisitSchedule)
