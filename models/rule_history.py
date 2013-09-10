from datetime import datetime
from django.db import models
from bhp_base_model.models import BaseModel


class RuleHistory(BaseModel):

    model = models.CharField(
        max_length=100)
    rule = models.CharField(
        max_length=500)
    predicate = models.CharField(
        max_length=100)
    action = models.CharField(
        max_length=25)
    timestamp = models.CharField(
        max_length=50,
        null=True,
        db_index=True)

    def __unicode__(self):
        return '%s %s %s' % (self.model, self.action, self.rule)

    def save(self, *args, **kwargs):

        if not self.timestamp:
            self.timestamp = int(datetime.today().strftime('%Y%m%d%H%M%S%f'))
        super(RuleHistory, self).save(*args, **kwargs)

    class Meta:
        app_label = "bhp_entry_rules"
        ordering = ['timestamp', ]
