from collections import OrderedDict
from edc.constants import REQUIRED, NOT_REQUIRED, ADDITIONAL, NOT_ADDITIONAL

from edc.subject.visit_schedule.classes import (VisitScheduleConfiguration, site_visit_schedules, EntryTuple,
                                                 MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple)

from ..models import MaternalVisit, MaternalEligibilityPost


class MpepuMaternalPostNatalVisitSchedule(VisitScheduleConfiguration):

    name = 'postnatal visit schedule'
    app_label = 'mpepu_maternal'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'maternal_eligible_postnatal': MembershipFormTuple('maternal_eligible_postnatal', MaternalEligibilityPost, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Maternal Post Partum Reg': ScheduleGroupTuple('Maternal Post Partum Reg', 'maternal_eligible_postnatal', 'ELIGIBILITY', None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict()

    visit_definitions['2000M'] = {
            'title': 'Maternal Post Natal Registration',
            'time_point': 0,
            'base_interval': 0,
            'base_interval_unit': 'D',
            'window_lower_bound': 15,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 34,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': 'As of 2012-11-26, submit requisition for Viral Load (storage only) instead of PHS Ultrasensitive Viral Load (<50)',
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'PHS Ultrasensitive Viral Load (>50)', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                #EntryTuple = namedtuple('EntryTuple', 'order app_label model_name form_status')
                EntryTuple(1L, u'mpepu_maternal', u'maternalpostfu', NOT_REQUIRED, NOT_ADDITIONAL),
                EntryTuple(10L, u'mpepu_maternal', u'maternalenroll', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalenrolldem', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalenrollmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalenrollob', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_maternal', u'maternalenrollclin', REQUIRED, NOT_ADDITIONAL),
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
            )}
    visit_definitions['2010M'] = {
            'title': 'Infant Randomization',
            'time_point': 10,
            'base_interval': 1,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2020M'] = {
            'title': '2 Months Postpartum Visit',
            'time_point': 20,
            'base_interval': 2,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, requisition_panel_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2030M'] = {
            'title': '3 Months Postpartum Visit',
            'time_point': 30,
            'base_interval': 3,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2060M'] = {
            'title': '6 Months Postpartum Visit',
            'time_point': 60,
            'base_interval': 6,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2090M'] = {
            'title': '9 Months Postpartum Visit',
            'time_point': 90,
            'base_interval': 9,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2120M'] = {
            'title': '12 Months Postpartum Visit',
            'time_point': 120,
            'base_interval': 12,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2150M'] = {
            'title': '15 Months Postpartum Visit',
            'time_point': 150,
            'base_interval': 15,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
            )}
    visit_definitions['2180M'] = {
            'title': '18 Months Postpartum Visit',
            'time_point': 180,
            'base_interval': 18,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'maternal',
            'visit_tracking_model': MaternalVisit,
            'schedule_group': 'Maternal Post Partum Reg',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionPanelTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'STORAGE', 'BM', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_maternal', u'postnatalinfantfeedingsurvey', REQUIRED, NOT_ADDITIONAL),
            )}

site_visit_schedules.register(MpepuMaternalPostNatalVisitSchedule)
