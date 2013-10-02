from bhp_base_model.models import BaseListModel


class DeathStudyDrug (BaseListModel):
    class Meta:
        app_label = "mpepu_list"
        ordering = ['display_index']


class DeathNevirapine (BaseListModel):
    class Meta:
        app_label = "mpepu_list"
        ordering = ['display_index']
