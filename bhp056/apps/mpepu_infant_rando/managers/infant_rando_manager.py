from django.db import models
from ..classes import Randomization


class InfantRandoManager(models.Manager):

    def randomize(self, **kwargs):
        infant_eligibility = kwargs.get('infant_eligibility')
        return Randomization().randomize(infant_eligibility)
