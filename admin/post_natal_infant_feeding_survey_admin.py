from django.contrib import admin
from mpepu_maternal.models import PostNatalInfantFeedingSurvey
from mpepu_maternal.forms import PostNatalInfantFeedingSurveyForm
from maternal_enroll_admin import BaseMaternalEnrollAdmin


class PostNatalInfantFeedingSurveyAdmin(BaseMaternalEnrollAdmin):

    form = PostNatalInfantFeedingSurveyForm
    fields = (
        "maternal_visit",
        "feeding_satisfaction",
        "next_feeding_choice",
        "feeding_period",
        "feeding_duration",
        "correct_bf_duration")
    radio_fields = {
        "feeding_satisfaction": admin.VERTICAL,
        "next_feeding_choice": admin.VERTICAL,
        "feeding_period": admin.VERTICAL,
        "feeding_duration": admin.VERTICAL,
        "correct_bf_duration": admin.VERTICAL}
admin.site.register(PostNatalInfantFeedingSurvey, PostNatalInfantFeedingSurveyAdmin)
