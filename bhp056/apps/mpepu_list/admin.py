from django.contrib import admin
from edc.base.modeladmin.admin import BaseModelAdmin
from models import PriorArv, ChronicCond, HhGoods
from models import HealthCond, DelComp, ObComp, Suppliment, LabDelDx, InfantVaccines, MaternalFeedingInfluence, MaternalBfFfRisksBenefits, MaternalUndecidedFeeding


class PriorArvAdmin(BaseModelAdmin):
    pass
admin.site.register(PriorArv, PriorArvAdmin)


class ChronicCondAdmin(BaseModelAdmin):
    pass
admin.site.register(ChronicCond, ChronicCondAdmin)


class HhGoodsAdmin(BaseModelAdmin):
    pass
admin.site.register(HhGoods, HhGoodsAdmin)


class HealthCondAdmin(BaseModelAdmin):
    pass
admin.site.register(HealthCond, HealthCondAdmin)


class DelCompAdmin(BaseModelAdmin):
    pass
admin.site.register(DelComp, DelCompAdmin)


class ObCompAdmin(BaseModelAdmin):
    pass
admin.site.register(ObComp, ObCompAdmin)


class SupplimentAdmin(BaseModelAdmin):
    pass
admin.site.register(Suppliment, SupplimentAdmin)


class LabDelDxAdmin(BaseModelAdmin):
    pass
admin.site.register(LabDelDx, LabDelDxAdmin)


class InfantVaccinesAdmin(BaseModelAdmin):
    pass
admin.site.register(InfantVaccines, InfantVaccinesAdmin)


class MaternalFeedingInfluenceAdmin(BaseModelAdmin):
    pass
admin.site.register(MaternalFeedingInfluence, MaternalFeedingInfluenceAdmin)


class MaternalBfFfRisksBenefitsAdmin(BaseModelAdmin):
    pass
admin.site.register(MaternalBfFfRisksBenefits, MaternalBfFfRisksBenefitsAdmin)


class MaternalUndecidedFeedingAdmin(BaseModelAdmin):
    pass
admin.site.register(MaternalUndecidedFeeding, MaternalUndecidedFeedingAdmin)
