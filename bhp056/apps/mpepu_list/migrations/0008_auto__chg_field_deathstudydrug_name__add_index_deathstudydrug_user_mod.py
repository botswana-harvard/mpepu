# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'DeathStudyDrug.name'
        db.alter_column(u'mpepu_list_deathstudydrug', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'DeathStudyDrug', fields ['user_modified']
        db.create_index(u'mpepu_list_deathstudydrug', ['user_modified'])

        # Adding index on 'DeathStudyDrug', fields ['user_created']
        db.create_index(u'mpepu_list_deathstudydrug', ['user_created'])


        # Changing field 'AutopsyInfoSource.name'
        db.alter_column(u'mpepu_list_autopsyinfosource', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'AutopsyInfoSource', fields ['user_modified']
        db.create_index(u'mpepu_list_autopsyinfosource', ['user_modified'])

        # Adding index on 'AutopsyInfoSource', fields ['user_created']
        db.create_index(u'mpepu_list_autopsyinfosource', ['user_created'])


        # Changing field 'HhGoods.name'
        db.alter_column(u'mpepu_list_hhgoods', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'HhGoods', fields ['user_modified']
        db.create_index(u'mpepu_list_hhgoods', ['user_modified'])

        # Adding index on 'HhGoods', fields ['user_created']
        db.create_index(u'mpepu_list_hhgoods', ['user_created'])


        # Changing field 'Suppliment.name'
        db.alter_column(u'mpepu_list_suppliment', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'Suppliment', fields ['user_modified']
        db.create_index(u'mpepu_list_suppliment', ['user_modified'])

        # Adding index on 'Suppliment', fields ['user_created']
        db.create_index(u'mpepu_list_suppliment', ['user_created'])


        # Changing field 'PriorArv.name'
        db.alter_column(u'mpepu_list_priorarv', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'PriorArv', fields ['user_modified']
        db.create_index(u'mpepu_list_priorarv', ['user_modified'])

        # Adding index on 'PriorArv', fields ['user_created']
        db.create_index(u'mpepu_list_priorarv', ['user_created'])


        # Changing field 'MaternalBfFfRisksBenefits.name'
        db.alter_column(u'mpepu_list_maternalbfffrisksbenefits', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'MaternalBfFfRisksBenefits', fields ['user_modified']
        db.create_index(u'mpepu_list_maternalbfffrisksbenefits', ['user_modified'])

        # Adding index on 'MaternalBfFfRisksBenefits', fields ['user_created']
        db.create_index(u'mpepu_list_maternalbfffrisksbenefits', ['user_created'])


        # Changing field 'DeathNevirapine.name'
        db.alter_column(u'mpepu_list_deathnevirapine', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'DeathNevirapine', fields ['user_modified']
        db.create_index(u'mpepu_list_deathnevirapine', ['user_modified'])

        # Adding index on 'DeathNevirapine', fields ['user_created']
        db.create_index(u'mpepu_list_deathnevirapine', ['user_created'])


        # Changing field 'DelComp.name'
        db.alter_column(u'mpepu_list_delcomp', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'DelComp', fields ['user_modified']
        db.create_index(u'mpepu_list_delcomp', ['user_modified'])

        # Adding index on 'DelComp', fields ['user_created']
        db.create_index(u'mpepu_list_delcomp', ['user_created'])


        # Changing field 'LabDelDx.dxcode_ptr'
        db.alter_column(u'mpepu_list_labdeldx', u'dxcode_ptr_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['code_lists.DxCode'], unique=True, primary_key=True))

        # Changing field 'MaternalFeedingInfluence.name'
        db.alter_column(u'mpepu_list_maternalfeedinginfluence', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'MaternalFeedingInfluence', fields ['user_modified']
        db.create_index(u'mpepu_list_maternalfeedinginfluence', ['user_modified'])

        # Adding index on 'MaternalFeedingInfluence', fields ['user_created']
        db.create_index(u'mpepu_list_maternalfeedinginfluence', ['user_created'])


        # Changing field 'ChronicCond.name'
        db.alter_column(u'mpepu_list_chroniccond', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'ChronicCond', fields ['user_modified']
        db.create_index(u'mpepu_list_chroniccond', ['user_modified'])

        # Adding index on 'ChronicCond', fields ['user_created']
        db.create_index(u'mpepu_list_chroniccond', ['user_created'])


        # Changing field 'InfantVaccines.name'
        db.alter_column(u'mpepu_list_infantvaccines', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'InfantVaccines', fields ['user_modified']
        db.create_index(u'mpepu_list_infantvaccines', ['user_modified'])

        # Adding index on 'InfantVaccines', fields ['user_created']
        db.create_index(u'mpepu_list_infantvaccines', ['user_created'])


        # Changing field 'MaternalUndecidedFeeding.name'
        db.alter_column(u'mpepu_list_maternalundecidedfeeding', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'MaternalUndecidedFeeding', fields ['user_modified']
        db.create_index(u'mpepu_list_maternalundecidedfeeding', ['user_modified'])

        # Adding index on 'MaternalUndecidedFeeding', fields ['user_created']
        db.create_index(u'mpepu_list_maternalundecidedfeeding', ['user_created'])


        # Changing field 'HealthCond.name'
        db.alter_column(u'mpepu_list_healthcond', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'HealthCond', fields ['user_modified']
        db.create_index(u'mpepu_list_healthcond', ['user_modified'])

        # Adding index on 'HealthCond', fields ['user_created']
        db.create_index(u'mpepu_list_healthcond', ['user_created'])


        # Changing field 'ObComp.name'
        db.alter_column(u'mpepu_list_obcomp', 'name', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True))
        # Adding index on 'ObComp', fields ['user_modified']
        db.create_index(u'mpepu_list_obcomp', ['user_modified'])

        # Adding index on 'ObComp', fields ['user_created']
        db.create_index(u'mpepu_list_obcomp', ['user_created'])


    def backwards(self, orm):
	pass
        # Removing index on 'ObComp', fields ['user_created']
        #db.delete_index(u'mpepu_list_obcomp', ['user_created'])

        # Removing index on 'ObComp', fields ['user_modified']
        #db.delete_index(u'mpepu_list_obcomp', ['user_modified'])

        # Removing index on 'HealthCond', fields ['user_created']
        #db.delete_index(u'mpepu_list_healthcond', ['user_created'])

        # Removing index on 'HealthCond', fields ['user_modified']
        #db.delete_index(u'mpepu_list_healthcond', ['user_modified'])

        # Removing index on 'MaternalUndecidedFeeding', fields ['user_created']
        #db.delete_index(u'mpepu_list_maternalundecidedfeeding', ['user_created'])

        # Removing index on 'MaternalUndecidedFeeding', fields ['user_modified']
        #db.delete_index(u'mpepu_list_maternalundecidedfeeding', ['user_modified'])

        # Removing index on 'InfantVaccines', fields ['user_created']
        #db.delete_index(u'mpepu_list_infantvaccines', ['user_created'])

        # Removing index on 'InfantVaccines', fields ['user_modified']
        #db.delete_index(u'mpepu_list_infantvaccines', ['user_modified'])

        # Removing index on 'ChronicCond', fields ['user_created']
        #db.delete_index(u'mpepu_list_chroniccond', ['user_created'])

        # Removing index on 'ChronicCond', fields ['user_modified']
        #db.delete_index(u'mpepu_list_chroniccond', ['user_modified'])

        # Removing index on 'MaternalFeedingInfluence', fields ['user_created']
        #db.delete_index(u'mpepu_list_maternalfeedinginfluence', ['user_created'])

        # Removing index on 'MaternalFeedingInfluence', fields ['user_modified']
        #db.delete_index(u'mpepu_list_maternalfeedinginfluence', ['user_modified'])

        # Removing index on 'DelComp', fields ['user_created']
        #db.delete_index(u'mpepu_list_delcomp', ['user_created'])

        # Removing index on 'DelComp', fields ['user_modified']
        #db.delete_index(u'mpepu_list_delcomp', ['user_modified'])

        # Removing index on 'DeathNevirapine', fields ['user_created']
        #db.delete_index(u'mpepu_list_deathnevirapine', ['user_created'])

        # Removing index on 'DeathNevirapine', fields ['user_modified']
        #db.delete_index(u'mpepu_list_deathnevirapine', ['user_modified'])

        # Removing index on 'MaternalBfFfRisksBenefits', fields ['user_created']
        #db.delete_index(u'mpepu_list_maternalbfffrisksbenefits', ['user_created'])

        # Removing index on 'MaternalBfFfRisksBenefits', fields ['user_modified']
        #db.delete_index(u'mpepu_list_maternalbfffrisksbenefits', ['user_modified'])

        # Removing index on 'PriorArv', fields ['user_created']
        #db.delete_index(u'mpepu_list_priorarv', ['user_created'])

        # Removing index on 'PriorArv', fields ['user_modified']
        #db.delete_index(u'mpepu_list_priorarv', ['user_modified'])

        # Removing index on 'Suppliment', fields ['user_created']
        #db.delete_index(u'mpepu_list_suppliment', ['user_created'])

        # Removing index on 'Suppliment', fields ['user_modified']
        #db.delete_index(u'mpepu_list_suppliment', ['user_modified'])

        # Removing index on 'HhGoods', fields ['user_created']
        #db.delete_index(u'mpepu_list_hhgoods', ['user_created'])

        # Removing index on 'HhGoods', fields ['user_modified']
        #db.delete_index(u'mpepu_list_hhgoods', ['user_modified'])

        # Removing index on 'AutopsyInfoSource', fields ['user_created']
        #db.delete_index(u'mpepu_list_autopsyinfosource', ['user_created'])

        # Removing index on 'AutopsyInfoSource', fields ['user_modified']
        #db.delete_index(u'mpepu_list_autopsyinfosource', ['user_modified'])

        # Removing index on 'DeathStudyDrug', fields ['user_created']
        #db.delete_index(u'mpepu_list_deathstudydrug', ['user_created'])

        # Removing index on 'DeathStudyDrug', fields ['user_modified']
        #db.delete_index(u'mpepu_list_deathstudydrug', ['user_modified'])


        # Changing field 'DeathStudyDrug.name'
        #db.alter_column(u'mpepu_list_deathstudydrug', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'AutopsyInfoSource.name'
        #db.alter_column(u'mpepu_list_autopsyinfosource', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'HhGoods.name'
        #db.alter_column(u'mpepu_list_hhgoods', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'Suppliment.name'
        #db.alter_column(u'mpepu_list_suppliment', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'PriorArv.name'
        #db.alter_column(u'mpepu_list_priorarv', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'MaternalBfFfRisksBenefits.name'
        #db.alter_column(u'mpepu_list_maternalbfffrisksbenefits', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'DeathNevirapine.name'
        #db.alter_column(u'mpepu_list_deathnevirapine', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'DelComp.name'
        #db.alter_column(u'mpepu_list_delcomp', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'LabDelDx.dxcode_ptr'
        #db.alter_column(u'mpepu_list_labdeldx', 'dxcode_ptr_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_code_lists.DxCode'], unique=True, primary_key=True))

        # Changing field 'MaternalFeedingInfluence.name'
        #db.alter_column(u'mpepu_list_maternalfeedinginfluence', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'ChronicCond.name'
        #db.alter_column(u'mpepu_list_chroniccond', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'InfantVaccines.name'
        #db.alter_column(u'mpepu_list_infantvaccines', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'MaternalUndecidedFeeding.name'
        #db.alter_column(u'mpepu_list_maternalundecidedfeeding', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'HealthCond.name'
        #db.alter_column(u'mpepu_list_healthcond', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

        # Changing field 'ObComp.name'
        #db.alter_column(u'mpepu_list_obcomp', 'name', self.gf('django.db.models.fields.CharField')(default='', max_length=250, unique=True))

    models = {
        'code_lists.dxcode': {
            'Meta': {'object_name': 'DxCode', 'db_table': "'bhp_code_lists_dxcode'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_list.autopsyinfosource': {
            'Meta': {'object_name': 'AutopsyInfoSource'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.chroniccond': {
            'Meta': {'object_name': 'ChronicCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.deathnevirapine': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathNevirapine'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.deathstudydrug': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathStudyDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.delcomp': {
            'Meta': {'object_name': 'DelComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.healthcond': {
            'Meta': {'object_name': 'HealthCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.hhgoods': {
            'Meta': {'object_name': 'HhGoods'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.infantvaccines': {
            'Meta': {'object_name': 'InfantVaccines'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.labdeldx': {
            'Meta': {'object_name': 'LabDelDx', '_ormbases': ['code_lists.DxCode']},
            u'dxcode_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['code_lists.DxCode']", 'unique': 'True', 'primary_key': 'True'})
        },
        'mpepu_list.maternalbfffrisksbenefits': {
            'Meta': {'object_name': 'MaternalBfFfRisksBenefits'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.maternalfeedinginfluence': {
            'Meta': {'object_name': 'MaternalFeedingInfluence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.maternalundecidedfeeding': {
            'Meta': {'object_name': 'MaternalUndecidedFeeding'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.obcomp': {
            'Meta': {'object_name': 'ObComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.priorarv': {
            'Meta': {'object_name': 'PriorArv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.suppliment': {
            'Meta': {'object_name': 'Suppliment'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        }
    }

    complete_apps = ['mpepu_list']
