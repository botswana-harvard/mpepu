from bhp_entry_rules.classes import RuleGroup, ScheduledDataRule, Logic, rule_groups
from edc.subject.registration.models import RegisteredSubject

from .models import (MaternalVisit, MaternalArvPreg, MaternalArvPost,
                                   MaternalEnroll, FeedingChoice)


class ConsentRuleGroup(RuleGroup):

    consent_version_two = ScheduledDataRule(
        logic=Logic(
            predicate=('consent_version', 'gte', 2),
            consequence='new',
            alternative='not_required',
            comment='v2 only'),
        target_model=['feedingchoice', 'feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree'])

    class Meta:
        app_label = 'mpepu_maternal'
        filter_model = (MaternalVisit, 'maternal_visit')
        source_model = RegisteredSubject
rule_groups.register(ConsentRuleGroup)


class MaternalEnrollRuleGroup(RuleGroup):

    prev_pregnancies = ScheduledDataRule(
        logic=Logic(
            predicate=('prev_pregnancies', 'equals', 0),
            consequence='not_required',
            alternative='new'),
        target_model=['maternalenrollob'])

    prior_health_haart = ScheduledDataRule(
        logic=Logic(
            predicate=('prior_health_haart', 'equals', 'yes'),
            consequence='new',
            alternative='not_required',
            ),
        target_model=['maternalenrollarv'])

    prev_pregnancy_arv = ScheduledDataRule(
        logic=Logic(
            predicate=('prev_pregnancy_arv', 'equals', 'yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalenrollclin'])

    class Meta:
        app_label = 'mpepu_maternal'
        filter_model = (MaternalVisit, 'maternal_visit')
        source_model = MaternalEnroll
rule_groups.register(MaternalEnrollRuleGroup)


class MaternalArvPregRuleGroup(RuleGroup):

    took_arv = ScheduledDataRule(
        logic=Logic(
            predicate=('took_arv', 'equals', 'yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalarvpreghistory'])

    start_pp = ScheduledDataRule(
        logic=Logic(
            predicate=('start_pp', 'equals', 'yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalarvpphistory'])

    class Meta:
        app_label = 'mpepu_maternal'
        filter_model = (MaternalVisit, 'maternal_visit')
        source_model = MaternalArvPreg
rule_groups.register(MaternalArvPregRuleGroup)


class MaternalArvPostRuleGroup(RuleGroup):

    haart = ScheduledDataRule(
        logic=Logic(
            predicate=(('haart_last_visit', 'equals', 'no'), ('arv_status', 'equals', 'never started', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['maternalarvpostadh'])

    class Meta:
        app_label = 'mpepu_maternal'
        filter_model = (MaternalVisit, 'maternal_visit')
        source_model = MaternalArvPost
rule_groups.register(MaternalArvPostRuleGroup)


class FeedingChoiceRuleGroup(RuleGroup):

    first_time_feeding = ScheduledDataRule(
        logic=Logic(
            predicate=('first_time_feeding', 'equals', 'no'),
            consequence='new',
            alternative='not_required'),
        target_model=['feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree'])

    first_time_feeding_yes = ScheduledDataRule(
        logic=Logic(
            predicate=('first_time_feeding', 'equals', 'yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['feedingchoicesectiontwo', 'feedingchoicesectionthree'])

    class Meta:
        app_label = 'mpepu_maternal'
        filter_model = (MaternalVisit, 'maternal_visit')
        source_model = FeedingChoice
rule_groups.register(FeedingChoiceRuleGroup)
