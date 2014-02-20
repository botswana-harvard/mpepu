from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionTuple

from ..models import InfantVisit

from ...mpepu_maternal.models import MaternalConsent


class MpepuInfantPreRandoVisitSchedule(VisitScheduleConfiguration):

    name = 'visit schedule'
    app_label = 'mpepu_infant'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'infant_pre_eligibility': MembershipFormTuple('infant_pre_eligibility', MaternalConsent, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Infant Pre-eligibility': ScheduleGroupTuple('Infant Pre-eligibility', 'infant_pre_eligibility', None, None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict(
        {'2015': {
            'title': 'Randomization II',
            'time_point': 15,
            'base_interval': 27,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Pre-eligibility',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
#                 RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'Hematology', 'TEST', 'WB'),
#                 RequisitionTuple(200L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB'),
#                 RequisitionTuple(300L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph'),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence'),
                EntryTuple(30L, u'mpepu_infant', u'infantfu'),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical'),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx'),
                EntryTuple(60L, u'mpepu_infant', u'infantfud'),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph'),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed'),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed'),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug'),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh'),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding'),
                EntryTuple(130L, u'mpepu_infant', u'infantstudydruginit'),
            )}
        }
    )

site_visit_schedules.register(MpepuInfantPreRandoVisitSchedule)
