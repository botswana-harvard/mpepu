from apps.mpepu_infant.models import InfantPreEligibility
from .base_infant_eligibility_form import BaseInfantEligibilityForm


class InfantPreEligibilityForm (BaseInfantEligibilityForm):

    suppress_eligibility_exception = True

    class Meta:
        model = InfantPreEligibility
