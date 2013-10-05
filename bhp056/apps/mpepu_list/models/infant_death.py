from edc.base.model.models import BaseListModel


class DeathStudyDrug (BaseListModel):
    class Meta:
        app_label = "mpepu_list"
        ordering = ['display_index']


class DeathNevirapine (BaseListModel):
    class Meta:
        app_label = "mpepu_list"
        ordering = ['display_index']
