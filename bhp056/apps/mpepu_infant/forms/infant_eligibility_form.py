from apps.mpepu_infant.models import InfantEligibility
from .base_infant_eligibility_form import BaseInfantEligibilityForm


class InfantEligibilityForm (BaseInfantEligibilityForm):

    suppress_eligibility_exception = False

    class Meta:
        model = InfantEligibility
