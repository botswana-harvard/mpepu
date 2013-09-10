from bhp_consent.forms import BaseConsentedModelForm
from mpepu_maternal.models import MaternalEligibilityPost, MaternalEligibilityAnte


class BaseMaternalEligibilityForm (BaseConsentedModelForm):
    pass


class MaternalEligibilityPostForm(BaseMaternalEligibilityForm):

    class Meta:
        model = MaternalEligibilityPost


class MaternalEligibilityAnteForm(BaseMaternalEligibilityForm):

    class Meta:
        model = MaternalEligibilityAnte
