from base_infant_eligibility_form import BaseInfantEligibilityForm
from mpepu_infant.models import InfantEligibility


class InfantEligibilityForm (BaseInfantEligibilityForm):

    suppress_eligibility_exception = False

    class Meta:
        model = InfantEligibility
