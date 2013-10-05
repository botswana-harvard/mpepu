from edc.subject.consent.forms import BaseConsentedModelForm

from ..models import MaternalEligibilityPost, MaternalEligibilityAnte


class BaseMaternalEligibilityForm (BaseConsentedModelForm):
    pass


class MaternalEligibilityPostForm(BaseMaternalEligibilityForm):

    class Meta:
        model = MaternalEligibilityPost


class MaternalEligibilityAnteForm(BaseMaternalEligibilityForm):

    class Meta:
        model = MaternalEligibilityAnte
