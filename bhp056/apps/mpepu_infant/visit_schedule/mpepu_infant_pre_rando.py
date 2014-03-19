from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.utils.constants import SHOW_FORM, HIDE_FORM

from ..models import InfantVisit, InfantPreEligibility

# from ...mpepu_maternal.models import MaternalConsent


class MpepuInfantPreRandoVisitSchedule(VisitScheduleConfiguration):

    name = 'pre-rando visit schedule'
    app_label = 'mpepu_infant'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'infant_pre_randomize': MembershipFormTuple('infant_pre_randomize', InfantPreEligibility, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Infant Pre-eligibility': ScheduleGroupTuple('Infant Pre-eligibility', 'infant_pre_randomize', None, None),
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
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', SHOW_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', SHOW_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', SHOW_FORM),
                #(entry_order, app_label, model_name, requisition_panel_name, panel_type, aliquot_type_alpha_code, form_visible)
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', HIDE_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(900L, u'mpepu_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', SHOW_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', SHOW_FORM),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', SHOW_FORM),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', SHOW_FORM),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', SHOW_FORM),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', SHOW_FORM),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', SHOW_FORM),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', SHOW_FORM),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', SHOW_FORM),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', SHOW_FORM),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', SHOW_FORM),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', SHOW_FORM),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', SHOW_FORM),
                EntryTuple(130L, u'mpepu_infant', u'infantstudydruginit', SHOW_FORM),
            )}
        }
    )

site_visit_schedules.register(MpepuInfantPreRandoVisitSchedule)
