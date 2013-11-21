from edc.subject.rule_groups.classes import RuleGroup, ScheduledDataRule, Logic, rule_groups


class ArvVisitRuleGroup(RuleGroup):
    pass
#     consent_version_two = ScheduledDataRule(
#         logic=Logic(
#             predicate=('consent_version', 'gte', 2),
#             consequence='new',
#             alternative='not_required',
#             comment='v2 only'),
#         target_model=['feedingchoice', 'feedingchoicesectionone', 'feedingchoicesectiontwo', 'feedingchoicesectionthree'])
# 
#     class Meta:
#         app_label = 'mpepu_maternal'
#         filter_model = (MaternalVisit, 'maternal_visit')
#         source_model = RegisteredSubject

rule_groups.register(ArvVisitRuleGroup)