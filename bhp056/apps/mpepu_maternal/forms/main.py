from base_maternal_model_form import BaseMaternalModelForm

from ..models import MaternalDeath, MaternalLocator


class MaternalDeathForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalDeath


class MaternalLocatorForm (BaseMaternalModelForm):

    class Meta:
        model = MaternalLocator
