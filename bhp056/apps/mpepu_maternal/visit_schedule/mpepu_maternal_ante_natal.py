from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.utils.constants import SHOW_FORM, HIDE_FORM

from ..models import MaternalVisit, MaternalEligibilityAnte


class MpepuMaternalAnteNatalVisitSchedule(VisitScheduleConfiguration):

    name = 'antenatal visit schedule'
    app_label = 'mpepu_maternal'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'maternal_eligible_antenatal': MembershipFormTuple('maternal_eligible_antenatal', MaternalEligibilityAnte, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Maternal Ante Natal Reg': ScheduleGroupTuple('Maternal Ante Natal Reg', 'maternal_eligible_antenatal', 'ELIGIBILITY', None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict(
        {'1000M': {
            'title': 'Maternal Ante Natal Registration',
            'time_point': 0,
            'base_interval': 0,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Ante Natal Reg',
            'instructions': 'As of 2012-11-26, submit requisition for Viral Load (storage only) instead of PHS Ultrasensitive Viral Load (<50)',
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', SHOW_FORM),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', SHOW_FORM),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', SHOW_FORM),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', SHOW_FORM),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', SHOW_FORM),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', HIDE_FORM),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', HIDE_FORM),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalenroll', SHOW_FORM),
                EntryTuple(20L, u'mpepu_maternal', u'maternalenrolldem', SHOW_FORM),
                EntryTuple(30L, u'mpepu_maternal', u'maternalenrollmed', SHOW_FORM),
                EntryTuple(40L, u'mpepu_maternal', u'maternalenrollclin', SHOW_FORM),
                EntryTuple(50L, u'mpepu_maternal', u'maternalenrollob', SHOW_FORM),
                EntryTuple(60L, u'mpepu_maternal', u'maternalenrollarv', SHOW_FORM),
                EntryTuple(70L, u'mpepu_maternal', u'maternalarvpreg', SHOW_FORM),
                EntryTuple(80L, u'mpepu_maternal', u'maternalarvpreghistory', SHOW_FORM),
                EntryTuple(90L, u'mpepu_maternal', u'maternalarvpphistory', SHOW_FORM),
                EntryTuple(100L, u'mpepu_maternal', u'maternallabdel', SHOW_FORM),
                EntryTuple(110L, u'mpepu_maternal', u'maternallabdelmed', SHOW_FORM),
                EntryTuple(120L, u'mpepu_maternal', u'maternallabdeldx', SHOW_FORM),
                EntryTuple(130L, u'mpepu_maternal', u'maternallabdelclinic', SHOW_FORM),
                EntryTuple(140L, u'mpepu_maternal', u'maternallocator', SHOW_FORM),
                EntryTuple(150L, u'mpepu_maternal', u'feedingchoice', SHOW_FORM),
                EntryTuple(160L, u'mpepu_maternal', u'feedingchoicesectionone', SHOW_FORM),
                EntryTuple(170L, u'mpepu_maternal', u'feedingchoicesectiontwo', SHOW_FORM),
            )}
        }
    )

site_visit_schedules.register(MpepuMaternalAnteNatalVisitSchedule)
