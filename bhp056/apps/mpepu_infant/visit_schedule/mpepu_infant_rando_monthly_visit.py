from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionTuple

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

    visit_definitions['2010'] = {
            'title': 'Randomization',
            'time_point': 10,
            'base_interval': 27,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'infant',
            'visit_tracking_model': InfantVisit,
            'schedule_group': 'Infant Rando and F/Up',
            'instructions': None,
            'requisitions': (
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'Hematology', 'TEST', 'WB'),
                RequisitionTuple(200L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB'),
                RequisitionTuple(300L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
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
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'Hematology', 'TEST', 'WB'),
                RequisitionTuple(200L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
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
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'Hematology', 'TEST', 'WB'),
                RequisitionTuple(200L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
                RequisitionTuple(300L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB'),
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
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
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
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
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
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'Hematology (ARV)', 'Hematology', 'TEST', 'WB'),
                RequisitionTuple(200L, u'mpepu_lab', u'infantrequisition', 'DNA PCR', 'Infant PCR', 'TEST', 'WB'),
                RequisitionTuple(300L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB'),
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
                RequisitionTuple(100L, u'mpepu_lab', u'infantrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB'),
                RequisitionTuple(200L, u'mpepu_lab', u'infantrequisition', 'ELISA', 'ELISA', 'TEST', 'WB'),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_infant', u'infantfu'),
                EntryTuple(20L, u'mpepu_infant', u'infantfuphysical'),
                EntryTuple(30L, u'mpepu_infant', u'infantfudx'),
                EntryTuple(40L, u'mpepu_infant', u'infantfud'),
                EntryTuple(50L, u'mpepu_infant', u'infantfudx2proph'),
                EntryTuple(60L, u'mpepu_infant', u'infantfunewmed'),
                EntryTuple(70L, u'mpepu_infant', u'infantfumed'),
                EntryTuple(80L, u'mpepu_infant', u'infantstudydrug'),
                EntryTuple(90L, u'mpepu_infant', u'infantctxplaceboadh'),
            )}
site_visit_schedules.register(MpepuInfantRandoMonthlyVisitSchedule)
