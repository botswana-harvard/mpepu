# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Lab'
        db.delete_table('mpepu_dashboard_lab')


    def backwards(self, orm):
        
        # Adding model 'Lab'
        db.create_table('mpepu_dashboard_lab', (
            ('release_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(1, 1, 1, 0, 0))),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='dmc3', max_length=50, blank=True)),
            ('aliquot_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('receive_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('result_item_count', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('release_status', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('review_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('review_status', self.gf('django.db.models.fields.CharField')(default='NOT_REVIEWED', max_length=25)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='dmc3', max_length=50, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('receive_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('order_identifier', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('result_item', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('drawn_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('panel', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_dashboard', ['Lab'])


    models = {
        
    }

    complete_apps = ['mpepu_dashboard']
