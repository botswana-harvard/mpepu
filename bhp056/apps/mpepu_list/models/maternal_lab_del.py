from bhp_base_model.models import BaseListModel
from edc.subject.code_lists.models import DxCode


class HealthCond (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal LabDel: Health Cond"


class DelComp (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal LabDel: Delivery Comp"


class ObComp(BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal LabDel: Ob Comp"


class Suppliment (BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal LabDel: Suppliments"


class LabDelDx (DxCode):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Maternal LabDel: Dx"
