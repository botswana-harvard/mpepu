from bhp_base_model.models import BaseListModel


class AutopsyInfoSource(BaseListModel):

    class Meta:
        app_label = "mpepu_list"
        verbose_name = "Autopsy Info Source"
