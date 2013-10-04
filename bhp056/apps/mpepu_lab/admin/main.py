from django.contrib import admin
from edc.lab.lab_packing.admin import BasePackingListAdmin, BasePackingListItemAdmin

from ..models import InfantRequisition, MaternalRequisition
from ..models import PackingList, PackingListItem
from ..forms import InfantRequisitionForm, MaternalRequisitionForm
from ..forms import PackingListForm, PackingListItemForm

from .base_infant_requisition_model_admin import BaseInfantRequisitionModelAdmin
from .base_maternal_requisition_model_admin import BaseMaternalRequisitionModelAdmin


# MaternalRequisition
class MaternalRequisitionAdmin(BaseMaternalRequisitionModelAdmin):
    form = MaternalRequisitionForm
admin.site.register(MaternalRequisition, MaternalRequisitionAdmin)


# InfantRequisition
class InfantRequisitionAdmin(BaseInfantRequisitionModelAdmin):
    form = InfantRequisitionForm
admin.site.register(InfantRequisition, InfantRequisitionAdmin)


class PackingListAdmin(BasePackingListAdmin):
    form = PackingListForm
    requisition = [InfantRequisition, MaternalRequisition, ]
    packing_list_item_model = PackingListItem
admin.site.register(PackingList, PackingListAdmin)


class PackingListItemAdmin(BasePackingListItemAdmin):
    form = PackingListItemForm
    requisition = [InfantRequisition, MaternalRequisition, ]
admin.site.register(PackingListItem, BasePackingListItemAdmin)
