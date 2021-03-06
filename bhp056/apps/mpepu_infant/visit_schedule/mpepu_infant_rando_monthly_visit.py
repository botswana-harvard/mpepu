from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionPanelTuple
from edc.constants import REQUIRED, NOT_ADDITIONAL, NOT_REQUIRED, ADDITIONAL

from ..models import InfantVisit, InfantEligibility

# from ...mpepu_maternal.models import MaternalConsent


class MpepuInfantRandoMonthlyVisitSchedule(VisitScheduleConfiguration):

    name = 'monthly visit schedule'
    app_label = 'mpepu_infant'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'infant_rando_eligible': MembershipFormTuple('infant_rando_eligible', InfantEligibility, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Infant Rando and F/Up': ScheduleGroupTuple('Infant Rando and F/Up', 'infant_rando_eligible', None, None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict()

    visit_definitions['2020'] = {
            'title': 'Infant 2 Months Visit',
            'time_point': 20,
            'base_interval': 2,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL)
            )}
    visit_definitions['2030'] = {
            'title': 'Infant 3 Months Visit',
            'time_point': 30,
            'base_interval': 3,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(130L, u'mpepu_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL)
            )}
    visit_definitions['2060'] = {
            'title': 'Infant 6 Months Visit',
            'time_point': 60,
            'base_interval': 6,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB',NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(130L, u'mpepu_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL)
            )}
    visit_definitions['2090'] = {
            'title': 'Infant 9 Months Visit',
            'time_point': 90,
            'base_interval': 9,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL)
            )}
    visit_definitions['2120'] = {
            'title': 'Infant 12 Months Visit',
            'time_point': 120,
            'base_interval': 12,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL)
            )}
    visit_definitions['2150'] = {
            'title': 'Infant 15 Months Visit',
            'time_point': 150,
            'base_interval': 15,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantarvproph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantnvpadherence', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(110L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(120L, u'mpepu_infant', u'infantfeeding', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', NOT_REQUIRED, ADDITIONAL)
            )}
    visit_definitions['2180'] = {
            'title': 'Infant18 Months Visit',
            'time_point': 180,
            'base_interval': 18,
            'base_interval_unit': 'M',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                RequisitionPanelTuple(100L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(200L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(300L, u'mpepu_lab', u'infantrequisition', 'Stool storage', 'STORAGE', 'ST', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(400L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(500L, u'mpepu_lab', u'infantrequisition', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(600L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(700L, u'mpepu_lab', u'infantrequisition', 'Bana 01 Chemistry', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(800L, u'mpepu_lab', u'infantrequisition', 'Hepatitis B only', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                RequisitionPanelTuple(900L, u'mpepu_lab', u'infantrequisition', 'HIV Western Blot', 'TEST', 'WB', NOT_REQUIRED, ADDITIONAL),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantfu', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(20L, u'mpepu_infant', u'infantfuphysical', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(30L, u'mpepu_infant', u'infantfudx', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(40L, u'mpepu_infant', u'infantfud', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx2proph', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(60L, u'mpepu_infant', u'infantfunewmed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(70L, u'mpepu_infant', u'infantfumed', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(80L, u'mpepu_infant', u'infantstudydrug', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(90L, u'mpepu_infant', u'infantctxplaceboadh', REQUIRED, NOT_ADDITIONAL),
                EntryTuple(100L, u'mpepu_infant', u'infantstoolcollection', REQUIRED, NOT_ADDITIONAL),
                #following are additional forms
                EntryTuple(200L, u'mpepu_infant', u'infantdeath', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(201L, u'mpepu_infant', u'infantsurvival', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(210L, u'mpepu_infant', u'infantverbalautopsy', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(220L, u'mpepu_infant', u'infantoffdrug', NOT_REQUIRED, ADDITIONAL),
                EntryTuple(230L, u'mpepu_infant', u'infantoffstudy', REQUIRED, NOT_ADDITIONAL),
            )}
site_visit_schedules.register(MpepuInfantRandoMonthlyVisitSchedule)
