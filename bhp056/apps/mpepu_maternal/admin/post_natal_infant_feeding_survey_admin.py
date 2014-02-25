from django.contrib import admin

from ..models import PostNatalInfantFeedingSurvey
from ..forms import PostNatalInfantFeedingSurveyForm
from .maternal_enroll_admin import BaseMaternalEnrollAdmin


class PostNatalInfantFeedingSurveyAdmin(BaseMaternalEnrollAdmin):

    form = PostNatalInfantFeedingSurveyForm
    fields = (
        "maternal_visit",
        "feeding_satisfaction",
        "feeding_period",
        "feeding_duration", 
        "correct_bf_duration",
        "next_feeding_choice", )
    radio_fields = {
        "feeding_satisfaction": admin.VERTICAL,
        "next_feeding_choice": admin.VERTICAL,
        "feeding_period": admin.VERTICAL,
        "feeding_duration": admin.VERTICAL,
        "correct_bf_duration": admin.VERTICAL}
admin.site.register(PostNatalInfantFeedingSurvey, PostNatalInfantFeedingSurveyAdmin)
