# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MaternalFeedingInfluence'
        db.create_table('mpepu_list_maternalfeedinginfluence', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='melissa', max_length=50, db_index=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250, db_index=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True, db_index=True)),
            ('display_index', self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True)),
            ('field_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('version', self.gf('django.db.models.fields.CharField')(default='1.0', max_length=35)),
        ))
        db.send_create_signal('mpepu_list', ['MaternalFeedingInfluence'])

        # Adding index on 'ChronicCond', fields ['name']
        db.create_index('mpepu_list_chroniccond', ['name'])


        # Changing field 'ChronicCond.short_name'
        db.alter_column('mpepu_list_chroniccond', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'ChronicCond', fields ['short_name']
        db.create_index('mpepu_list_chroniccond', ['short_name'])

        # Adding index on 'ChronicCond', fields ['display_index']
        db.create_index('mpepu_list_chroniccond', ['display_index'])

        # Adding index on 'DeathStudyDrug', fields ['name']
        db.create_index('mpepu_list_deathstudydrug', ['name'])


        # Changing field 'DeathStudyDrug.short_name'
        db.alter_column('mpepu_list_deathstudydrug', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'DeathStudyDrug', fields ['short_name']
        db.create_index('mpepu_list_deathstudydrug', ['short_name'])

        # Adding index on 'DeathStudyDrug', fields ['display_index']
        db.create_index('mpepu_list_deathstudydrug', ['display_index'])

        # Adding index on 'AutopsyInfoSource', fields ['name']
        db.create_index('mpepu_list_autopsyinfosource', ['name'])


        # Changing field 'AutopsyInfoSource.short_name'
        db.alter_column('mpepu_list_autopsyinfosource', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'AutopsyInfoSource', fields ['short_name']
        db.create_index('mpepu_list_autopsyinfosource', ['short_name'])

        # Adding index on 'AutopsyInfoSource', fields ['display_index']
        db.create_index('mpepu_list_autopsyinfosource', ['display_index'])

        # Adding index on 'HhGoods', fields ['name']
        db.create_index('mpepu_list_hhgoods', ['name'])


        # Changing field 'HhGoods.short_name'
        db.alter_column('mpepu_list_hhgoods', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'HhGoods', fields ['short_name']
        db.create_index('mpepu_list_hhgoods', ['short_name'])

        # Adding index on 'HhGoods', fields ['display_index']
        db.create_index('mpepu_list_hhgoods', ['display_index'])

        # Adding index on 'Suppliment', fields ['name']
        db.create_index('mpepu_list_suppliment', ['name'])


        # Changing field 'Suppliment.short_name'
        db.alter_column('mpepu_list_suppliment', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'Suppliment', fields ['short_name']
        db.create_index('mpepu_list_suppliment', ['short_name'])

        # Adding index on 'Suppliment', fields ['display_index']
        db.create_index('mpepu_list_suppliment', ['display_index'])

        # Adding index on 'PriorArv', fields ['name']
        db.create_index('mpepu_list_priorarv', ['name'])


        # Changing field 'PriorArv.short_name'
        db.alter_column('mpepu_list_priorarv', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'PriorArv', fields ['short_name']
        db.create_index('mpepu_list_priorarv', ['short_name'])

        # Adding index on 'PriorArv', fields ['display_index']
        db.create_index('mpepu_list_priorarv', ['display_index'])

        # Adding index on 'DeathNevirapine', fields ['name']
        db.create_index('mpepu_list_deathnevirapine', ['name'])


        # Changing field 'DeathNevirapine.short_name'
        db.alter_column('mpepu_list_deathnevirapine', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'DeathNevirapine', fields ['short_name']
        db.create_index('mpepu_list_deathnevirapine', ['short_name'])

        # Adding index on 'DeathNevirapine', fields ['display_index']
        db.create_index('mpepu_list_deathnevirapine', ['display_index'])

        # Adding index on 'ObComp', fields ['name']
        db.create_index('mpepu_list_obcomp', ['name'])


        # Changing field 'ObComp.short_name'
        db.alter_column('mpepu_list_obcomp', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'ObComp', fields ['short_name']
        db.create_index('mpepu_list_obcomp', ['short_name'])

        # Adding index on 'ObComp', fields ['display_index']
        db.create_index('mpepu_list_obcomp', ['display_index'])

        # Adding index on 'DelComp', fields ['name']
        db.create_index('mpepu_list_delcomp', ['name'])


        # Changing field 'DelComp.short_name'
        db.alter_column('mpepu_list_delcomp', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'DelComp', fields ['short_name']
        db.create_index('mpepu_list_delcomp', ['short_name'])

        # Adding index on 'DelComp', fields ['display_index']
        db.create_index('mpepu_list_delcomp', ['display_index'])

        # Adding index on 'InfantVaccines', fields ['name']
        db.create_index('mpepu_list_infantvaccines', ['name'])


        # Changing field 'InfantVaccines.short_name'
        db.alter_column('mpepu_list_infantvaccines', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'InfantVaccines', fields ['short_name']
        db.create_index('mpepu_list_infantvaccines', ['short_name'])

        # Adding index on 'InfantVaccines', fields ['display_index']
        db.create_index('mpepu_list_infantvaccines', ['display_index'])

        # Adding index on 'HealthCond', fields ['name']
        db.create_index('mpepu_list_healthcond', ['name'])


        # Changing field 'HealthCond.short_name'
        db.alter_column('mpepu_list_healthcond', 'short_name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'HealthCond', fields ['short_name']
        db.create_index('mpepu_list_healthcond', ['short_name'])

        # Adding index on 'HealthCond', fields ['display_index']
        db.create_index('mpepu_list_healthcond', ['display_index'])


    def backwards(self, orm):
        # Removing index on 'HealthCond', fields ['display_index']
        db.delete_index('mpepu_list_healthcond', ['display_index'])

        # Removing index on 'HealthCond', fields ['short_name']
        db.delete_index('mpepu_list_healthcond', ['short_name'])

        # Removing index on 'HealthCond', fields ['name']
        db.delete_index('mpepu_list_healthcond', ['name'])

        # Removing index on 'InfantVaccines', fields ['display_index']
        db.delete_index('mpepu_list_infantvaccines', ['display_index'])

        # Removing index on 'InfantVaccines', fields ['short_name']
        db.delete_index('mpepu_list_infantvaccines', ['short_name'])

        # Removing index on 'InfantVaccines', fields ['name']
        db.delete_index('mpepu_list_infantvaccines', ['name'])

        # Removing index on 'DelComp', fields ['display_index']
        db.delete_index('mpepu_list_delcomp', ['display_index'])

        # Removing index on 'DelComp', fields ['short_name']
        db.delete_index('mpepu_list_delcomp', ['short_name'])

        # Removing index on 'DelComp', fields ['name']
        db.delete_index('mpepu_list_delcomp', ['name'])

        # Removing index on 'ObComp', fields ['display_index']
        db.delete_index('mpepu_list_obcomp', ['display_index'])

        # Removing index on 'ObComp', fields ['short_name']
        db.delete_index('mpepu_list_obcomp', ['short_name'])

        # Removing index on 'ObComp', fields ['name']
        db.delete_index('mpepu_list_obcomp', ['name'])

        # Removing index on 'DeathNevirapine', fields ['display_index']
        db.delete_index('mpepu_list_deathnevirapine', ['display_index'])

        # Removing index on 'DeathNevirapine', fields ['short_name']
        db.delete_index('mpepu_list_deathnevirapine', ['short_name'])

        # Removing index on 'DeathNevirapine', fields ['name']
        db.delete_index('mpepu_list_deathnevirapine', ['name'])

        # Removing index on 'PriorArv', fields ['display_index']
        db.delete_index('mpepu_list_priorarv', ['display_index'])

        # Removing index on 'PriorArv', fields ['short_name']
        db.delete_index('mpepu_list_priorarv', ['short_name'])

        # Removing index on 'PriorArv', fields ['name']
        db.delete_index('mpepu_list_priorarv', ['name'])

        # Removing index on 'Suppliment', fields ['display_index']
        db.delete_index('mpepu_list_suppliment', ['display_index'])

        # Removing index on 'Suppliment', fields ['short_name']
        db.delete_index('mpepu_list_suppliment', ['short_name'])

        # Removing index on 'Suppliment', fields ['name']
        db.delete_index('mpepu_list_suppliment', ['name'])

        # Removing index on 'HhGoods', fields ['display_index']
        db.delete_index('mpepu_list_hhgoods', ['display_index'])

        # Removing index on 'HhGoods', fields ['short_name']
        db.delete_index('mpepu_list_hhgoods', ['short_name'])

        # Removing index on 'HhGoods', fields ['name']
        db.delete_index('mpepu_list_hhgoods', ['name'])

        # Removing index on 'AutopsyInfoSource', fields ['display_index']
        db.delete_index('mpepu_list_autopsyinfosource', ['display_index'])

        # Removing index on 'AutopsyInfoSource', fields ['short_name']
        db.delete_index('mpepu_list_autopsyinfosource', ['short_name'])

        # Removing index on 'AutopsyInfoSource', fields ['name']
        db.delete_index('mpepu_list_autopsyinfosource', ['name'])

        # Removing index on 'DeathStudyDrug', fields ['display_index']
        db.delete_index('mpepu_list_deathstudydrug', ['display_index'])

        # Removing index on 'DeathStudyDrug', fields ['short_name']
        db.delete_index('mpepu_list_deathstudydrug', ['short_name'])

        # Removing index on 'DeathStudyDrug', fields ['name']
        db.delete_index('mpepu_list_deathstudydrug', ['name'])

        # Removing index on 'ChronicCond', fields ['display_index']
        db.delete_index('mpepu_list_chroniccond', ['display_index'])

        # Removing index on 'ChronicCond', fields ['short_name']
        db.delete_index('mpepu_list_chroniccond', ['short_name'])

        # Removing index on 'ChronicCond', fields ['name']
        db.delete_index('mpepu_list_chroniccond', ['name'])

        # Deleting model 'MaternalFeedingInfluence'
        db.delete_table('mpepu_list_maternalfeedinginfluence')


        # Changing field 'ChronicCond.short_name'
        db.alter_column('mpepu_list_chroniccond', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'DeathStudyDrug.short_name'
        db.alter_column('mpepu_list_deathstudydrug', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'AutopsyInfoSource.short_name'
        db.alter_column('mpepu_list_autopsyinfosource', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'HhGoods.short_name'
        db.alter_column('mpepu_list_hhgoods', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'Suppliment.short_name'
        db.alter_column('mpepu_list_suppliment', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'PriorArv.short_name'
        db.alter_column('mpepu_list_priorarv', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'DeathNevirapine.short_name'
        db.alter_column('mpepu_list_deathnevirapine', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'ObComp.short_name'
        db.alter_column('mpepu_list_obcomp', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'DelComp.short_name'
        db.alter_column('mpepu_list_delcomp', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'InfantVaccines.short_name'
        db.alter_column('mpepu_list_infantvaccines', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

        # Changing field 'HealthCond.short_name'
        db.alter_column('mpepu_list_healthcond', 'short_name', self.gf('django.db.models.fields.CharField')(default=0, max_length=250, unique=True))

    models = {
        'bhp_code_lists.dxcode': {
            'Meta': {'object_name': 'DxCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_list.autopsyinfosource': {
            'Meta': {'object_name': 'AutopsyInfoSource'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.chroniccond': {
            'Meta': {'object_name': 'ChronicCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.deathnevirapine': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathNevirapine'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.deathstudydrug': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathStudyDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.delcomp': {
            'Meta': {'object_name': 'DelComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.healthcond': {
            'Meta': {'object_name': 'HealthCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.hhgoods': {
            'Meta': {'object_name': 'HhGoods'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.infantvaccines': {
            'Meta': {'object_name': 'InfantVaccines'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.labdeldx': {
            'Meta': {'object_name': 'LabDelDx', '_ormbases': ['bhp_code_lists.DxCode']},
            'dxcode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_code_lists.DxCode']", 'unique': 'True', 'primary_key': 'True'})
        },
        'mpepu_list.maternalfeedinginfluence': {
            'Meta': {'object_name': 'MaternalFeedingInfluence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.obcomp': {
            'Meta': {'object_name': 'ObComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.priorarv': {
            'Meta': {'object_name': 'PriorArv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.suppliment': {
            'Meta': {'object_name': 'Suppliment'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'melissa'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        }
    }

    complete_apps = ['mpepu_list']