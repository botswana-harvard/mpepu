# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'InfantRandoAudit'
        db.create_table('mpepu_infant_infantrando_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='home', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='home', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('stratum', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sid', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('rx', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('bf_duration', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('feeding_choice', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('haart_status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('randomization_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('infant_initials', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('dispensed', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant_rando', ['InfantRandoAudit'])

        # Adding model 'InfantRando'
        db.create_table('mpepu_infant_infantrando', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='home', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='home', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('stratum', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=15)),
            ('rx', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('bf_duration', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('feeding_choice', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('haart_status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
            ('randomization_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('infant_initials', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('dispensed', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('mpepu_infant_rando', ['InfantRando'])


    def backwards(self, orm):
        
        # Deleting model 'InfantRandoAudit'
        db.delete_table('mpepu_infant_infantrando_audit')

        # Deleting model 'InfantRando'
        db.delete_table('mpepu_infant_infantrando')


    models = {
        'mpepu_infant_rando.infantrando': {
            'Meta': {'ordering': "['sid']", 'object_name': 'InfantRando', 'db_table': "'mpepu_infant_infantrando'"},
            'bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dispensed': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'haart_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rx': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'stratum': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant_rando.infantrandoaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantRandoAudit', 'db_table': "'mpepu_infant_infantrando_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dispensed': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'haart_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'rx': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'stratum': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        }
    }

    complete_apps = ['mpepu_infant_rando']
