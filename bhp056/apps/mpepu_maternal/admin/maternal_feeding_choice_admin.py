from django.contrib import admin

from .maternal_enroll_admin import BaseMaternalEnrollAdmin
from ..models import FeedingChoice, FeedingChoiceSectionOne, FeedingChoiceSectionTwo, FeedingChoiceSectionThree
from ..forms import FeedingChoiceForm, FeedingChoiceSectionOneForm, FeedingChoiceSectionTwoForm, FeedingChoiceSectionThreeForm


class FeedingChoiceAdmin(BaseMaternalEnrollAdmin):

    form = FeedingChoiceForm
    fields = (
        "maternal_visit",
        "first_time_feeding")
    radio_fields = {
        "first_time_feeding": admin.VERTICAL}
admin.site.register(FeedingChoice, FeedingChoiceAdmin)


class FeedingChoiceSectionOneAdmin(BaseMaternalEnrollAdmin):

    form = FeedingChoiceSectionOneForm
    fields = (
        "maternal_visit",
        "last_baby_feeding",
        "baby_weaned_age",
        "hiv_aware_feeding",
        "hiv_status")
    radio_fields = {
        "last_baby_feeding": admin.VERTICAL,
        "hiv_aware_feeding": admin.VERTICAL,
        "hiv_status": admin.VERTICAL}
admin.site.register(FeedingChoiceSectionOne, FeedingChoiceSectionOneAdmin)


class FeedingChoiceSectionTwoAdmin(BaseMaternalEnrollAdmin):

    form = FeedingChoiceSectionTwoForm
    fields = (
        "maternal_visit",
        "status_disclosure",
        "disclose_hiv_father",
        "outside_disclosure",
        "influential_people",
        'influential_people_other',
        "work_influence",
        "work_return",
        "bf_hiv_worry",
        "infant_hiv_risk",
        "hiv_worry",
        "death_worry",
        "bf_hiv_arv",
        "safe_ff",
        "bf_ff_benefits",
        "baby_bf_choice",
        "doc_feeding_advice")
    radio_fields = {
        "status_disclosure": admin.VERTICAL,
        "disclose_hiv_father": admin.VERTICAL,
        "outside_disclosure": admin.VERTICAL,
        "work_influence": admin.VERTICAL,
        "work_return": admin.VERTICAL,
        "bf_hiv_worry": admin.VERTICAL,
        "infant_hiv_risk": admin.VERTICAL,
        "hiv_worry": admin.VERTICAL,
        "death_worry": admin.VERTICAL,
        "bf_hiv_arv": admin.VERTICAL,
        "safe_ff": admin.VERTICAL,
        "bf_ff_benefits": admin.VERTICAL,
        "baby_bf_choice": admin.VERTICAL,
        "doc_feeding_advice": admin.VERTICAL}
    filter_horizontal = ("influential_people",)
admin.site.register(FeedingChoiceSectionTwo, FeedingChoiceSectionTwoAdmin)


class FeedingChoiceSectionThreeAdmin(BaseMaternalEnrollAdmin):

    form = FeedingChoiceSectionThreeForm
    fields = (
        "maternal_visit",
        "risk_benefit_training",
        "und_risk_benefit",
        "ff_advice",
        "bf_advice",
        "feeding_choice_made",
        "chosen_feeding_choice",
        "undecided_feeding")
    radio_fields = {
        "und_risk_benefit": admin.VERTICAL,
        "ff_advice": admin.VERTICAL,
        "bf_advice": admin.VERTICAL,
        "feeding_choice_made": admin.VERTICAL,
        "chosen_feeding_choice": admin.VERTICAL}
    filter_horizontal = (
        "risk_benefit_training",
        "undecided_feeding",)
admin.site.register(FeedingChoiceSectionThree, FeedingChoiceSectionThreeAdmin)
