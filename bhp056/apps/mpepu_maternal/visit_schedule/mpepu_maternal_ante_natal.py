from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionTuple

from ..models import MaternalVisit, MaternalEligibilityAnte


class MpepuMaternalAnteNatalVisitSchedule(VisitScheduleConfiguration):

    name = 'antenatal visit schedule'
    app_label = 'mpepu_maternal'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'maternal_eligible_antenat': MembershipFormTuple('maternal_eligible_antenat', MaternalEligibilityAnte, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Maternal Ante Natal Reg': ScheduleGroupTuple('Maternal Ante Natal Reg', 'maternal_eligible_antenat', 'ELIGIBILITY', None),
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
                RequisitionTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Hematology (ARV)', 'Hematology', 'TEST', 'WB'),
                RequisitionTuple(200L, u'mpepu_lab', u'maternalrequisition', 'Viral load (storage only)', 'Viral load (storage)', 'STORAGE', 'WB'),
                RequisitionTuple(300L, u'mpepu_lab', u'maternalrequisition', 'CD4 (ARV)', 'CD4', 'TEST', 'WB'),
                RequisitionTuple(400L, u'mpepu_lab', u'maternalrequisition', 'Plasma and Buffy Coat Storage', 'Plasma and Buffy Coat Storage', 'STORAGE', 'WB'),
                RequisitionTuple(500L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'Viral load (PHS)', 'TEST', 'WB'),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalenroll'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalenrolldem'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalenrollmed'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalenrollclin'),
                EntryTuple(50L, u'mpepu_maternal', u'maternalenrollob'),
                EntryTuple(60L, u'mpepu_maternal', u'maternalenrollarv'),
                EntryTuple(70L, u'mpepu_maternal', u'maternalarvpreg'),
                EntryTuple(80L, u'mpepu_maternal', u'maternalarvpreghistory'),
                EntryTuple(90L, u'mpepu_maternal', u'maternalarvpphistory'),
                EntryTuple(100L, u'mpepu_maternal', u'maternallabdel'),
                EntryTuple(110L, u'mpepu_maternal', u'maternallabdelmed'),
                EntryTuple(120L, u'mpepu_maternal', u'maternallabdeldx'),
                EntryTuple(130L, u'mpepu_maternal', u'maternallabdelclinic'),
                EntryTuple(140L, u'mpepu_maternal', u'maternallocator'),
                EntryTuple(150L, u'mpepu_maternal', u'feedingchoice'),
                EntryTuple(160L, u'mpepu_maternal', u'feedingchoicesectionone'),
                EntryTuple(170L, u'mpepu_maternal', u'feedingchoicesectiontwo'),
            )}
        }
    )

site_visit_schedules.register(MpepuMaternalAnteNatalVisitSchedule)
