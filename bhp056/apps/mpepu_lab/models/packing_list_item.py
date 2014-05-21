from django.db import models

from edc.lab.lab_packing.models import BasePackingListItem

from .panel import Panel
from .packing_list import PackingList


class PackingListItem(BasePackingListItem):

    packing_list = models.ForeignKey(PackingList, null=True)

    panel = models.ForeignKey(Panel,
        null=True,
        blank=True,
        )

    class Meta:
        app_label = "mpepu_lab"
        verbose_name = 'Packing List Item'
