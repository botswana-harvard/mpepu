from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.constants import REQUIRED, NOT_ADDITIONAL

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

    visit_definitions['ARVR'] = {
            'title': 'Maternal ARV Resistance',
            'time_point': 0,
            'base_interval': 0,
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
          #'RequisitionPanelTuple', 'entry_order app_label model_name requisition_panel_name panel_type aliquot_type_alpha_code form_visible
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'ARV Resistance Testing', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                             ),
            'entries': (
                #additional forms for the TAB study
                EntryTuple(10L, u'mpepu_maternal', u'resistanceeligibility', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'resistancedisc', REQUIRED, NOT_ADDITIONAL),
            )}
site_visit_schedules.register(MpepuResistanceStudyVisitSchedule)
