from django.db import models
from lab_packing.models import BasePackingListItem
from packing_list import PackingList


class PackingListItem(BasePackingListItem):

    packing_list = models.ForeignKey(PackingList)

    class Meta:
        app_label = "mpepu_lab"
        verbose_name = 'Packing List Item'
