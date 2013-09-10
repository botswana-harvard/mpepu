from django.contrib import admin
from lab_packing.admin import BasePackingListAdmin, BasePackingListItemAdmin
from base_infant_requisition_model_admin import BaseInfantRequisitionModelAdmin
from base_maternal_requisition_model_admin import BaseMaternalRequisitionModelAdmin
from mpepu_lab.models import InfantRequisition, MaternalRequisition
from mpepu_lab.models import PackingList, PackingListItem
from mpepu_lab.forms import InfantRequisitionForm, MaternalRequisitionForm
from mpepu_lab.forms import PackingListForm, PackingListItemForm


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
