from base_infant_eligibility_form import BaseInfantEligibilityForm
from mpepu_infant.models import InfantPreEligibility


class InfantPreEligibilityForm (BaseInfantEligibilityForm):

    suppress_eligibility_exception = True

    class Meta:
        model = InfantPreEligibility
