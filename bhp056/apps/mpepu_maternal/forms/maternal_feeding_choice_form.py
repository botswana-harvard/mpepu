from .base_maternal_model_form import BaseMaternalModelForm
from ..models import FeedingChoice, FeedingChoiceSectionOne, FeedingChoiceSectionTwo, FeedingChoiceSectionThree


class FeedingChoiceForm (BaseMaternalModelForm):

    class Meta:
        model = FeedingChoice


class FeedingChoiceSectionOneForm (BaseMaternalModelForm):

    class Meta:
        model = FeedingChoiceSectionOne


class FeedingChoiceSectionTwoForm (BaseMaternalModelForm):

    class Meta:
        model = FeedingChoiceSectionTwo


class FeedingChoiceSectionThreeForm (BaseMaternalModelForm):

    class Meta:
        model = FeedingChoiceSectionThree
