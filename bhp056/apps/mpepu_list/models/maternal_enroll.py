from edc.base.model.models import BaseListModel


class PriorArv (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal Enrollment List: Prior ARV"


class ChronicCond (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal Enrollment List: Cond"


class HhGoods (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal Enrollment List: HH Goods"
