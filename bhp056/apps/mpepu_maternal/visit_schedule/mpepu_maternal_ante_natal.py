from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL

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
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalenroll', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalenrolldem', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalenrollmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalenrollclin', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_maternal', u'maternalenrollob', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_maternal', u'maternalenrollarv', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_maternal', u'maternalarvpreg', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_maternal', u'maternalarvpreghistory', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_maternal', u'maternalarvpphistory', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_maternal', u'maternallabdel', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_maternal', u'maternallabdelmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_maternal', u'maternallabdeldx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(130L, u'mpepu_maternal', u'maternallabdelclinic', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(140L, u'mpepu_maternal', u'maternallocator', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(150L, u'mpepu_maternal', u'feedingchoice', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(160L, u'mpepu_maternal', u'feedingchoicesectionone', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(170L, u'mpepu_maternal', u'feedingchoicesectiontwo', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(180L, u'mpepu_maternal', u'feedingchoicesectionthree', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(190L, u'mpepu_maternal', u'postnatalinfantfeedingsurvey', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_maternal', u'maternaldeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_maternal', u'maternaloffstudy', NOT_REQUIRED, ADDITIONAL),
            )}
        }
    )

site_visit_schedules.register(MpepuMaternalAnteNatalVisitSchedule)
