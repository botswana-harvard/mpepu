from lab_packing.models import BasePackingList


class PackingList(BasePackingList):

    class Meta:
        app_label = "mpepu_lab"
        verbose_name = 'Packing List'
