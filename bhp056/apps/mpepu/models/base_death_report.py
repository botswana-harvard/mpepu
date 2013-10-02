from bhp_base_model.models import BaseListModel


class DeathHaart (BaseListModel):

    class Meta:
        app_label = "mpepu"
        ordering = ['display_index']


class DeathTradMed (BaseListModel):

    class Meta:
        app_label = "mpepu"
        ordering = ['display_index']
