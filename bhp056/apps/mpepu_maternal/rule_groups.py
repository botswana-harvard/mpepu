from datetime import date

from edc.subject.rule_groups.classes import RuleGroup, site_rule_groups, ScheduledDataRule, Logic
from edc.subject.registration.models import RegisteredSubject

from .models import (MaternalVisit, MaternalArvPreg, MaternalArvPost,
                                   MaternalEnroll, FeedingChoice)


def func_feeding_survey(visit_instance):
    if visit_instance.reason=='scheduled' and visit_instance.report_datetime.date() >= date(2015, 4, 7):
        return True
    return False


class MaternalEnrollRuleGroup(RuleGroup):

    prev_pregnancies = ScheduledDataRule(
        logic=Logic(
            predicate=('prev_pregnancies', 'equals', 0),
            consequence='not_required',
            alternative='new'),
        target_model=['maternalenrollob'])

    prior_health_haart = ScheduledDataRule(
        logic=Logic(
            predicate=('prior_health_haart', 'equals', 'Yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalenrollarv'])

    prev_pregnancy_arv = ScheduledDataRule(
        logic=Logic(
            predicate=('prev_pregnancy_arv', 'equals', 'Yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalenrollclin'])

    class Meta:
        app_label = 'mpepu_maternal'
        source_fk = (MaternalVisit, 'maternal_visit')
        source_model = MaternalEnroll
site_rule_groups.register(MaternalEnrollRuleGroup)


class MaternalArvPregRuleGroup(RuleGroup):

    took_arv = ScheduledDataRule(
        logic=Logic(
            predicate=('took_arv', 'equals', 'Yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalarvpreghistory'])

    start_pp = ScheduledDataRule(
        logic=Logic(
            predicate=('start_pp', 'equals', 'Yes'),
            consequence='new',
            alternative='not_required'),
        target_model=['maternalarvpphistory'])

    class Meta:
        app_label = 'mpepu_maternal'
        source_fk = (MaternalVisit, 'maternal_visit')
        source_model = MaternalArvPreg
site_rule_groups.register(MaternalArvPregRuleGroup)


class MaternalArvPostRuleGroup(RuleGroup):

    haart = ScheduledDataRule(
        logic=Logic(
            predicate=(('haart_last_visit', 'equals', 'No'), ('arv_status', 'equals', 'never started', 'or')),
            consequence='not_required',
            alternative='new'),
        target_model=['maternalarvpostadh'])

    class Meta:
        app_label = 'mpepu_maternal'
        source_fk = (MaternalVisit, 'maternal_visit')
        source_model = MaternalArvPost
site_rule_groups.register(MaternalArvPostRuleGroup)


class FeedingChoiceRuleGroup(RuleGroup):

    first_time_feeding = ScheduledDataRule(
        logic=Logic(
            predicate=('first_time_feeding', 'equals', 'No'),
            consequence='new',
            alternative='not_required'),
        target_model=['feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree'])

    first_time_feeding_yes = ScheduledDataRule(
        logic=Logic(
            predicate=('first_time_feeding', 'equals', 'Yes'),
            consequence='new',
            alternative='none'),
        target_model=['feedingchoicesectiontwo', 'feedingchoicesectionthree'])

    class Meta:
        app_label = 'mpepu_maternal'
        source_fk = (MaternalVisit, 'maternal_visit')
        source_model = FeedingChoice
site_rule_groups.register(FeedingChoiceRuleGroup)

class CessationRuleGroup(RuleGroup):

    first_time_feeding = ScheduledDataRule(
        logic=Logic(
            predicate=func_feeding_survey,
            consequence='new',
            alternative='not_required'),
        target_model=['PostNatalInfantFeedingSurvey'])

    class Meta:
        app_label = 'mpepu_maternal'
        source_fk = None
        source_model = RegisteredSubject
site_rule_groups.register(CessationRuleGroup)

# class MaternalDeathRuleGroup(RuleGroup):
#
#     death = ScheduledDataRule(
#         logic=Logic(
#             predicate=('reason', 'equals', 'death'),
#             consequence='new',
#             alternative='not_required'),
#         target_model=['maternaldeath', 'maternaloffstudy'])
#
#     class Meta:
#         app_label = 'mpepu_maternal'
#         source_fk = None
#         source_model = RegisteredSubject
# site_rule_groups.register(MaternalDeathRuleGroup)
#
#
# class MaternalOffStudyRuleGroup(RuleGroup):
#
#     off_study = ScheduledDataRule(
#         logic=Logic(
#             predicate=('reason', 'equals', 'off study'),
#             consequence='new',
#             alternative='not_required'),
#         target_model=['maternaloffstudy'])
#
#     class Meta:
#         app_label = 'mpepu_maternal'
#         source_fk = None
#         source_model = RegisteredSubject
# site_rule_groups.register(MaternalOffStudyRuleGroup)
