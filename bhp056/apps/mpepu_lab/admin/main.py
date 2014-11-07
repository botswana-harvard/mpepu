from django.contrib import admin

from edc.lab.lab_packing.admin import BasePackingListAdmin, BasePackingListItemAdmin
from edc.base.modeladmin.admin import BaseModelAdmin

from lis.labeling.actions import print_aliquot_label
from ..models import (InfantRequisition, MaternalRequisition, Aliquot, AliquotType, Receive, Panel)
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
    requisition = [InfantRequisition, MaternalRequisition, Aliquot ]
    packing_list_item_model = PackingListItem
admin.site.register(PackingList, PackingListAdmin)


class PackingListItemAdmin(BasePackingListItemAdmin):
    form = PackingListItemForm
    requisition = [InfantRequisition, MaternalRequisition, Aliquot]
admin.site.register(PackingListItem, BasePackingListItemAdmin)


class AliquotAdmin(BaseModelAdmin):
    date_hierarchy = 'created'

    actions = [print_aliquot_label]

    list_display = ("aliquot_identifier", 'subject_identifier', 'to_receive', 'drawn', "aliquot_type", 'aliquot_condition', 'created', 'user_created', 'hostname_created')

    search_fields = ('aliquot_identifier', 'receive__receive_identifier', 'receive__registered_subject__subject_identifier')

    list_filter = ('aliquot_type', 'aliquot_condition', 'created', 'user_created', 'hostname_created')

    list_per_page = 15

admin.site.register(Aliquot, AliquotAdmin)


class AliquotTypeAdmin(BaseModelAdmin):

    list_display = ('name', 'alpha_code', 'numeric_code')

admin.site.register(AliquotType, AliquotTypeAdmin)


class ReceiveAdmin(BaseModelAdmin):

    date_hierarchy = 'receive_datetime'

    list_display = ("receive_identifier", "infant_requisition", "maternal_requisition", "receive_datetime", "drawn_datetime", 'registered_subject', 'subject_type', 'created', 'modified', 'import_datetime')

    search_fields = ('registered_subject__subject_identifier', 'subject_type', "receive_identifier", "requisition_identifier",)

    list_filter = ('created', "receive_datetime", "drawn_datetime", 'modified', 'import_datetime', )

    list_per_page = 15

    def get_readonly_fields(self, request, obj):
        return ['receive_identifier', 'requisition_model_name', 'clinician_initials'] + [field.name for field in obj._meta.fields if field.editable]

admin.site.register(Receive, ReceiveAdmin)


class PanelAdmin(BaseModelAdmin):

    list_display = ('name', 'panel_type')

    filter_horizontal = ("test_code", "aliquot_type", )

    list_filter = ('panel_type', )

admin.site.register(Panel, PanelAdmin)
