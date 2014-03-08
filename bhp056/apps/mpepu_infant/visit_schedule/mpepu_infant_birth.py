from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionTuple
from edc.utils.constants import SHOW_FORM, HIDE_FORM

from ..models import InfantVisit, InfantBirth

#from ...mpepu_maternal.models import MaternalConsent


class MpepuInfantBirthVisitSchedule(VisitScheduleConfiguration):

    name = 'birth visit schedule'
    app_label = 'mpepu_infant'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'infant_birth_record': MembershipFormTuple('infant_birth_record', InfantBirth, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Infant Birth': ScheduleGroupTuple('Infant Birth', 'infant_birth_record', None, None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict(
        {'2000': {
            'title': 'Birth',
            'time_point': 0,
            'base_interval': 0,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Birth',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB', SHOW_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantbirthdata', SHOW_FORM),
                EntryTuple(20L, u'mpepu_infant', u'infantbirthexam', SHOW_FORM),
                EntryTuple(30L, u'mpepu_infant', u'infantbirtharv', SHOW_FORM),
                EntryTuple(40L, u'mpepu_infant', u'infantbirthfeed', SHOW_FORM),
            )}
        }
    )

site_visit_schedules.register(MpepuInfantBirthVisitSchedule)
