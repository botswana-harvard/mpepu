from django.db import models

from edc.lab.lab_packing.models import BasePackingList


class PackingList(BasePackingList):
    
    @property
    def item_models(self):
        item_m = []
        item_m.append(models.get_model('mpepu_lab', 'InfantRequisition'))
        item_m.append(models.get_model('mpepu_lab', 'MaternalRequisition'))
        item_m.append(models.get_model('mpepu_lab', 'Aliquot'))
        return item_m

    @property
    def packing_list_item_model(self):
        return models.get_model('mpepu_lab', 'PackingListItem')

    class Meta:
        app_label = "mpepu_lab"
        verbose_name = 'Packing List'
