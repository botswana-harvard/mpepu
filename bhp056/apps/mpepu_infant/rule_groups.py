from edc.subject.rule_groups.classes import RuleGroup, ScheduledDataRule, Logic, site_rule_groups, AdditionalDataRule
from edc.subject.registration.models import RegisteredSubject
from edc.subject.appointment.models import Appointment
from .models import (InfantVisit, InfantArvProph, InfantFu, InfantStudyDrug)


class InfantPrerandoLossRuleGroup(RuleGroup):

    lost = AdditionalDataRule(
        logic=Logic(
            predicate=(('reason', 'equals', 'lost'), ('sid', 'equals', None, 'and')),
            consequence='required',
            alternative='not_required'),
        target_model=['infantprerandoloss','infantoffstudy'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (RegisteredSubject, 'registered_subject')
site_rule_groups.register(InfantPrerandoLossRuleGroup)


class InfantPrerandoLossOffDrugRuleGroup(RuleGroup):

    lost_off_drug = AdditionalDataRule(
        logic=Logic(
            predicate=(('reason', 'equals', 'lost'), ('sid', 'ne', None, 'and')),
            consequence='required',
            alternative='not_required'),
        target_model=['infantoffdrug', 'infantoffstudy'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (RegisteredSubject, 'registered_subject')
site_rule_groups.register(InfantPrerandoLossOffDrugRuleGroup)


class InfantDeathRuleGroup(RuleGroup):

    death = AdditionalDataRule(
        logic=Logic(
            predicate=(('reason', 'equals', 'death'), ('sid', 'equals', None, 'and')),
            consequence='required',
            alternative='not_required'),
        target_model=[ 'infantprerandoloss', 'infantsurvival', 'infantdeath',
                      'infantverbalautopsy','infantoffstudy'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (RegisteredSubject, 'registered_subject')
site_rule_groups.register(InfantDeathRuleGroup)


class InfantDeathOffDrugRuleGroup(RuleGroup):

    death_off_drug = AdditionalDataRule(
        logic=Logic(
            predicate=(('reason', 'equals', 'death'), ('sid', 'ne', None, 'and')),
            consequence='required',
            alternative='not_required'),
        target_model=['infantoffdrug', 'infantsurvival', 'infantdeath',
                      'infantverbalautopsy', 'infantoffstudy'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (Appointment, 'appointment')
site_rule_groups.register(InfantDeathOffDrugRuleGroup)


class InfantOffDrugRuleGroup(RuleGroup):

    off_drug = AdditionalDataRule(
        logic=Logic(
            predicate=('study_status', 'equals', 'onstudy rando offdrug'),
            consequence='required',
            alternative='not_required'),
        target_model=['infantoffdrug'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (Appointment, 'appointment')
site_rule_groups.register(InfantOffDrugRuleGroup)


class InfantOffStudyRuleGroup(RuleGroup):

    off_study = AdditionalDataRule(
        logic=Logic(
            predicate=('study_status', 'equals', 'offstudy'),
            consequence='required',
            alternative='not_required'),
        target_model=['infantoffstudy'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (Appointment, 'appointment')
site_rule_groups.register(InfantOffStudyRuleGroup)


#class InfantBirthDataRuleGroup(RuleGroup):
#
#    congenital_anomalities = AdditionalDataRule(
#        logic=Logic(
#            predicate=('congenital_anomalities', 'equals', 'yes'),
#            consequence='required',
#            alternative='not_required'),
#        target_model=['infantcongenitalanomalies'])
#
#    class Meta:
#        app_label = 'mpepu_infant'
#        source_model = InfantBirthData
#        filter_model = (InfantVisit, 'infant_visit')
#site_rule_groups.register(InfantBirthDataRuleGroup)


#class InfantBirthDataRuleGroup(RuleGroup):
#
#    congenital_anomalities = AdditionalDataRule(
#        logic=Logic(
#            predicate=('congenital_anomalities', 'equals', 'yes'),
#            consequence='required',
#            alternative='not_required'),
#        target_model=['infantcongenitalanomalies'])
#
#    class Meta:
#        app_label = 'mpepu_infant'
#        source_model = InfantBirthData
#        filter_model = (InfantVisit, 'infant_visit')
#site_rule_groups.register(InfantBirthDataRuleGroup)


class InfantArvProphRuleGroup(RuleGroup):

    prophylatic_nvp = ScheduledDataRule(
        logic=Logic(
            predicate=('prophylatic_nvp', 'equals', 'no'),
            consequence='not_required',
            alternative='new'),
        target_model=['infantnvpadherence'])

    class Meta:
        app_label = 'mpepu_infant'
        filter_model = (InfantVisit, 'infant_visit')
        source_model = InfantArvProph
site_rule_groups.register(InfantArvProphRuleGroup)


class InfantFuRuleGroup(RuleGroup):

    diarrhea_illness = ScheduledDataRule(
        logic=Logic(
            predicate=('diarrhea_illness', 'equals', 'no'),
            consequence='not_required',
            alternative='new'),
        target_model=['Infantfud'])

    has_dx = ScheduledDataRule(
        logic=Logic(
            predicate=('has_dx', 'equals', 'no'),
            consequence='not_required',
            alternative='new'),
        target_model=['Infantfudx'])

    class Meta:
        app_label = 'mpepu_infant'
        filter_model = (InfantVisit, 'infant_visit')
        source_model = InfantFu
site_rule_groups.register(InfantFuRuleGroup)


class InfantStudyDrugRuleGroup(RuleGroup):

    on_placebo_status = ScheduledDataRule(
        logic=Logic(
            predicate=('on_placebo_status', 'equals', 'no'),
            consequence='not_required',
            alternative='new'),
        target_model=['infantctxplaceboadh'])

    class Meta:
        app_label = 'mpepu_infant'
        filter_model = (InfantVisit, 'infant_visit')
        source_model = InfantStudyDrug
site_rule_groups.register(InfantStudyDrugRuleGroup)


#class InfantOffStudyDrugRuleGroup(RuleGroup):
#
#    on_placebo_status = ScheduledDataRule(
#        logic=Logic(
#            predicate=('id', 'ne', None),
#            consequence='not_required',
#            alternative='new'),
#        target_model=['infantctxplaceboadh'])
#
#    class Meta:
#        app_label = 'mpepu_infant'
#        filter_model = (InfantVisit, 'infant_visit')
#        source_model = InfantStudyDrug
#site_rule_groups.register(InfantOffStudyDrugRuleGroup)


class InfantVisitSurvivalRuleGroup(RuleGroup):

    survival_status = AdditionalDataRule(
        logic=Logic(
            predicate=('survival_status', 'equals', 'DEAD'),
            consequence='required',
            alternative='not_required'),
        target_model=['infantdeath'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (Appointment, 'appointment')
site_rule_groups.register(InfantVisitSurvivalRuleGroup)


class InfantVisitTelephoneRuleGroup(RuleGroup):

    info_source = ScheduledDataRule(
        logic=Logic(
            predicate=('info_source', 'equals', 'telephone'),
            consequence='not_required',
            alternative='new'),
        target_model=['infantfu', 'infantfuphysical', 'infantfud', 'infantfudx', 'infantfudx2proph', 'infantfunewmed', 'infantfumed'])

    class Meta:
        app_label = 'mpepu_infant'
        source_model = InfantVisit
        filter_model = (Appointment, 'appointment')
site_rule_groups.register(InfantVisitTelephoneRuleGroup)
