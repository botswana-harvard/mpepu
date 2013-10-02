# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # Adding field 'PackingList.timestamp'
        db.add_column('mpepu_lab_packinglist', 'timestamp', self.gf('django.db.models.fields.IntegerField')(null=True), keep_default=False)


    def backwards(self, orm):
        pass
        # Deleting field 'PackingList.timestamp'
        db.delete_column('mpepu_lab_packinglist', 'timestamp')

