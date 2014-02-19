from collections import OrderedDict

from edc.subject.visit_schedule.classes import VisitScheduleConfiguration, site_visit_schedules, EntryTuple, MembershipFormTuple, ScheduleGroupTuple, RequisitionTuple

from ..models import MaternalVisit, MaternalConsent


class MpepuMaternalPostPartumVisitSchedule(VisitScheduleConfiguration):

    name = 'visit schedule'
    app_label = 'mpepu_maternal'
    # membership forms
    # (name, model, visible)
    membership_forms = OrderedDict({
        'maternal_post_reg': MembershipFormTuple('maternal_post_reg', MaternalConsent, True),
        })

    # schedule groups
    # (name, membership_form_name, grouping_key, comment)
    schedule_groups = OrderedDict({
        'Post Partum Follow-up': ScheduleGroupTuple('Post Partum Follow-up', 'maternal_post_reg', None, None),
        })

    # visit_schedule
    # see edc.subject.visit_schedule.models.visit_defintion
    visit_definitions = OrderedDict(
        {'2010M': {
            'title': 'Maternal Post Natal Registration',
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
                RequisitionTuple(100L, u'mpepu_lab', u'maternalrequisition', 'Breast Milk (Storage)', 'Breast Milk', 'STORAGE', 'BM'),
                RequisitionTuple(200L, u'mpepu_lab', u'maternalrequisition', 'PBMC Plasma (STORE ONLY)', 'PBMC Plasma Storage', 'STORAGE', 'WB'),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2020M': {
            'title': 'Maternal Post Natal Registration',
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
                # (entry_order, app_label, model_name, panel.name, panel.edc_name, panel.panel_type, aliquot_type)
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2030M': {
            'title': 'Maternal Post Natal Registration',
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
                RequisitionTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'Viral load (PHS)', 'TEST', 'WB'),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2060M': {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2090M': {
            'title': 'Maternal Post Natal Registration',
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
                RequisitionTuple(10L, u'mpepu_lab', u'maternalrequisition', 'PHS: Ultrasensetive Viral Load', 'Viral load (PHS)', 'TEST', 'WB'),
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2120M': {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2150M': {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
            )}
        },
        {'2180M': {
            'title': 'Maternal Post Natal Registration',
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
                ),
            'entries': (
                EntryTuple(10L, u'mpepu_maternal', u'maternalpostfu'),
                EntryTuple(20L, u'mpepu_maternal', u'maternalpostfudx'),
                EntryTuple(30L, u'mpepu_maternal', u'maternalarvpost'),
                EntryTuple(40L, u'mpepu_maternal', u'maternalarvpostadh'),
                EntryTuple(50L, u'mpepu_maternal', u'postnatalinfantfeedingsurvey'),
            )}
        },
    )

site_visit_schedules.register(MpepuMaternalPostPartumVisitSchedule)
