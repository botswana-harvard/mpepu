from lab_packing.forms import BasePackingListForm, BasePackingListItemForm
from lab_requisition.forms import BaseRequisitionForm
from models import InfantRequisition, MaternalRequisition
from models import PackingList, PackingListItem


class InfantRequisitionForm (BaseRequisitionForm):

    def clean(self):
        return super(InfantRequisitionForm, self).clean()

    class Meta:
        model = InfantRequisition


class MaternalRequisitionForm (BaseRequisitionForm):

    def clean(self):
        return super(MaternalRequisitionForm, self).clean()

    class Meta:
        model = MaternalRequisition


class PackingListForm (BasePackingListForm):

    def clean(self):
        self.requisition = [InfantRequisition, MaternalRequisition, ]
        return  super(PackingListForm, self).clean()

    class Meta:
        model = PackingList


class PackingListItemForm (BasePackingListItemForm):

    def clean(self):
        self.requisition = [InfantRequisition, MaternalRequisition, ]
        return  super(BasePackingListItemForm, self).clean()

    class Meta:
        model = PackingListItem
