from edc.base.model.models.base_list_model import BaseListModel


class DeathHaart (BaseListModel):

    class Meta:
        app_label = "mpepu"
        ordering = ['display_index']


class DeathTradMed (BaseListModel):

    class Meta:
        app_label = "mpepu"
        ordering = ['display_index']
