# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'InfantVisitAudit'
        db.create_table('mpepu_infant_infantvisit_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('info_source', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_source_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('information_provider', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('information_provider_other', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('study_status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('appointment', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantvisit', to=orm['bhp_appointment.Appointment'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantVisitAudit'])

        # Adding model 'InfantVisit'
        db.create_table('mpepu_infant_infantvisit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('appointment', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_appointment.Appointment'], unique=True)),
            ('report_datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('info_source', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_source_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('information_provider', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('information_provider_other', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('study_status', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantVisit'])

        # Adding model 'InfantBirthAudit'
        db.create_table('mpepu_infant_infantbirth_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirth', to=orm['bhp_registration.RegisteredSubject'])),
            ('maternal_lab_del', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirth', to=orm['mpepu_maternal.MaternalLabDel'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('birth_order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthAudit'])

        # Adding model 'InfantBirth'
        db.create_table('mpepu_infant_infantbirth', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject'])),
            ('maternal_lab_del', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_maternal.MaternalLabDel'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('initials', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('birth_order', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('dob', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirth'])

        # Adding unique constraint on 'InfantBirth', fields ['initials', 'maternal_lab_del']
        db.create_unique('mpepu_infant_infantbirth', ['initials', 'maternal_lab_del_id'])

        # Adding model 'InfantBirthDataAudit'
        db.create_table('mpepu_infant_infantbirthdata_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirthdata', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_birth_weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('infant_length', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('head_circumference', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('apgar_score', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('apgar_score_min_1', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('apgar_score_min_5', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('apgar_score_min_10', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('congenital_anomalities', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('other_birth_info', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('infant_birth', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirthdata', to=orm['mpepu_infant.InfantBirth'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthDataAudit'])

        # Adding model 'InfantBirthData'
        db.create_table('mpepu_infant_infantbirthdata', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_birth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantBirth'], unique=True)),
            ('infant_birth_weight', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('infant_length', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=1)),
            ('head_circumference', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('apgar_score', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('apgar_score_min_1', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('apgar_score_min_5', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('apgar_score_min_10', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('congenital_anomalities', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('other_birth_info', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthData'])

        # Adding model 'InfantBirthExamAudit'
        db.create_table('mpepu_infant_infantbirthexam_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirthexam', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_exam_date', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('general_activity', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('abnormal_activity', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('physical_exam_result', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('heent_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('heent_no_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resp_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('resp_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cardiac_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('cardiac_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('abdominal_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('abdominal_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('skin_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('skin_exam_other', self.gf('django.db.models.fields.TextField')(max_length=15, null=True, blank=True)),
            ('macular_papular_rash', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('neurologic_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('neuro_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('other_exam_info', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('infant_birth', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirthexam', to=orm['mpepu_infant.InfantBirth'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthExamAudit'])

        # Adding model 'InfantBirthExam'
        db.create_table('mpepu_infant_infantbirthexam', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_birth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantBirth'], unique=True)),
            ('infant_exam_date', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('general_activity', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('abnormal_activity', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('physical_exam_result', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('heent_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('heent_no_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('resp_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('resp_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('cardiac_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('cardiac_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('abdominal_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('abdominal_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('skin_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('skin_exam_other', self.gf('django.db.models.fields.TextField')(max_length=15, null=True, blank=True)),
            ('macular_papular_rash', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('neurologic_exam', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('neuro_exam_other', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('other_exam_info', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthExam'])

        # Adding model 'InfantBirthArvAudit'
        db.create_table('mpepu_infant_infantbirtharv_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirtharv', to=orm['mpepu_infant.InfantVisit'])),
            ('azt_after_birth', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('azt_dose_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('azt_additional_dose', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sdnvp_after_birth', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nvp_dose_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('additional_nvp_doses', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('azt_discharge_supply', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nvp_discharge_supply', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('infant_arv_comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('infant_birth', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirtharv', to=orm['mpepu_infant.InfantBirth'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthArvAudit'])

        # Adding model 'InfantBirthArv'
        db.create_table('mpepu_infant_infantbirtharv', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_birth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantBirth'], unique=True)),
            ('azt_after_birth', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('azt_dose_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('azt_additional_dose', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('sdnvp_after_birth', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nvp_dose_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('additional_nvp_doses', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('azt_discharge_supply', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('nvp_discharge_supply', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('infant_arv_comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthArv'])

        # Adding model 'InfantBirthFeedAudit'
        db.create_table('mpepu_infant_infantbirthfeed_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirthfeed', to=orm['mpepu_infant.InfantVisit'])),
            ('feeding_after_delivery', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('infant_birth', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantbirthfeed', to=orm['mpepu_infant.InfantBirth'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthFeedAudit'])

        # Adding model 'InfantBirthFeed'
        db.create_table('mpepu_infant_infantbirthfeed', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_birth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantBirth'], unique=True)),
            ('feeding_after_delivery', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantBirthFeed'])

        # Adding M2M table for field vaccination on 'InfantBirthFeed'
        db.create_table('mpepu_infant_infantbirthfeed_vaccination', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infantbirthfeed', models.ForeignKey(orm['mpepu_infant.infantbirthfeed'], null=False)),
            ('infantvaccines', models.ForeignKey(orm['mpepu_list.infantvaccines'], null=False))
        ))
        db.create_unique('mpepu_infant_infantbirthfeed_vaccination', ['infantbirthfeed_id', 'infantvaccines_id'])

        # Adding model 'InfantEligibilityAudit'
        db.create_table('mpepu_infant_infanteligibility_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('hiv_status', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('ctx_contra', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('congen_anomaly', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('maternal_art_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('maternal_feeding_choice', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('randomization_site', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infanteligibility', to=orm['bhp_registration.RegisteredSubject'])),
            ('infant_birth', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infanteligibility', to=orm['mpepu_infant.InfantBirth'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantEligibilityAudit'])

        # Adding model 'InfantEligibility'
        db.create_table('mpepu_infant_infanteligibility', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('infant_birth', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantBirth'], unique=True)),
            ('hiv_status', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('ctx_contra', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('congen_anomaly', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('maternal_art_status', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('maternal_feeding_choice', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('randomization_site', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantEligibility'])

        # Adding model 'InfantArvProphAudit'
        db.create_table('mpepu_infant_infantarvproph_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantarvproph', to=orm['mpepu_infant.InfantVisit'])),
            ('prophylatic_nvp', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('arv_status', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantArvProphAudit'])

        # Adding model 'InfantArvProph'
        db.create_table('mpepu_infant_infantarvproph', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('prophylatic_nvp', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('arv_status', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantArvProph'])

        # Adding model 'InfantArvProphModAudit'
        db.create_table('mpepu_infant_infantarvprophmod_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('arv_code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('dose_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('modification_date', self.gf('django.db.models.fields.DateField')()),
            ('modification_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_arv_proph', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantarvprophmod', to=orm['mpepu_infant.InfantArvProph'])),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantArvProphModAudit'])

        # Adding model 'InfantArvProphMod'
        db.create_table('mpepu_infant_infantarvprophmod', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('arv_code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('dose_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('modification_date', self.gf('django.db.models.fields.DateField')()),
            ('modification_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('infant_arv_proph', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantArvProph'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantArvProphMod'])

        # Adding model 'InfantDeathAudit'
        db.create_table('mpepu_infant_infantdeath_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('death_cause_info', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantdeath', to=orm['bhp_adverse.DeathCauseInfo'])),
            ('death_cause_info_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('perform_autopsy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('death_cause', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('death_cause_category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantdeath', to=orm['bhp_adverse.DeathCauseCategory'])),
            ('death_cause_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('dx_code', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantdeath', max_length=25, to=orm['bhp_code_lists.DxCode'])),
            ('illness_duration', self.gf('django.db.models.fields.IntegerField')()),
            ('death_medical_responsibility', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantdeath', to=orm['bhp_adverse.DeathMedicalResponsibility'])),
            ('participant_hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('death_reason_hospitalized', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantdeath', to=orm['bhp_adverse.DeathReasonHospitalized'])),
            ('days_hospitalized', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantdeath', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantDeathAudit'])

        # Adding model 'InfantDeath'
        db.create_table('mpepu_infant_infantdeath', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('death_date', self.gf('django.db.models.fields.DateField')()),
            ('death_cause_info', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseInfo'])),
            ('death_cause_info_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('perform_autopsy', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('death_cause', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('death_cause_category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseCategory'])),
            ('death_cause_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('dx_code', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_code_lists.DxCode'], max_length=25)),
            ('illness_duration', self.gf('django.db.models.fields.IntegerField')()),
            ('death_medical_responsibility', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathMedicalResponsibility'])),
            ('participant_hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('death_reason_hospitalized', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathReasonHospitalized'])),
            ('days_hospitalized', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantDeath'])

        # Adding model 'InfantHaartAudit'
        db.create_table('mpepu_infant_infanthaart_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('hiv_positive_date', self.gf('django.db.models.fields.DateField')()),
            ('haart_initiated', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('haart_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('arv_status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infanthaart', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantHaartAudit'])

        # Adding model 'InfantHaart'
        db.create_table('mpepu_infant_infanthaart', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('hiv_positive_date', self.gf('django.db.models.fields.DateField')()),
            ('haart_initiated', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('haart_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('arv_status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantHaart'])

        # Adding model 'InfantHaartModAudit'
        db.create_table('mpepu_infant_infanthaartmod_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('arv_code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('dose_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('modification_date', self.gf('django.db.models.fields.DateField')()),
            ('modification_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_haart', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infanthaartmod', to=orm['mpepu_infant.InfantHaart'])),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantHaartModAudit'])

        # Adding model 'InfantHaartMod'
        db.create_table('mpepu_infant_infanthaartmod', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('arv_code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('dose_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('modification_date', self.gf('django.db.models.fields.DateField')()),
            ('modification_code', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('infant_haart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantHaart'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantHaartMod'])

        # Adding model 'InfantOffDrugAudit'
        db.create_table('mpepu_infant_infantoffdrug_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('last_dose_date', self.gf('django.db.models.fields.DateField')()),
            ('reason_off', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_off_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantoffdrug', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantOffDrugAudit'])

        # Adding model 'InfantOffDrug'
        db.create_table('mpepu_infant_infantoffdrug', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('last_dose_date', self.gf('django.db.models.fields.DateField')()),
            ('reason_off', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_off_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantOffDrug'])

        # Adding model 'InfantSurvivalAudit'
        db.create_table('mpepu_infant_infantsurvival_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_survival_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_provider', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_provider_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantsurvival', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantSurvivalAudit'])

        # Adding model 'InfantSurvival'
        db.create_table('mpepu_infant_infantsurvival', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('infant_survival_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_provider', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('info_provider_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantSurvival'])

        # Adding model 'InfantNvpAdherenceAudit'
        db.create_table('mpepu_infant_infantnvpadherence_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantnvpadherence', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_arv_proph', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantnvpadherence', to=orm['mpepu_infant.InfantArvProph'])),
            ('days_missed', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('reason_missed_other', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantNvpAdherenceAudit'])

        # Adding model 'InfantNvpAdherence'
        db.create_table('mpepu_infant_infantnvpadherence', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_arv_proph', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantArvProph'])),
            ('days_missed', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('reason_missed_other', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantNvpAdherence'])

        # Adding model 'InfantPrerandoLossAudit'
        db.create_table('mpepu_infant_infantprerandoloss_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('reason_loss', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('loss_code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_loss_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantprerandoloss', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantPrerandoLossAudit'])

        # Adding model 'InfantPrerandoLoss'
        db.create_table('mpepu_infant_infantprerandoloss', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('reason_loss', self.gf('django.db.models.fields.TextField')(max_length=250)),
            ('loss_code', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_loss_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantPrerandoLoss'])

        # Adding model 'InfantStudyDrugInitAudit'
        db.create_table('mpepu_infant_infantstudydruginit_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantstudydruginit', to=orm['mpepu_infant.InfantVisit'])),
            ('initiated', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('first_dose_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reason_not_init', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('reason_not_survive', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('reason_not_init_other', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantStudyDrugInitAudit'])

        # Adding model 'InfantStudyDrugInit'
        db.create_table('mpepu_infant_infantstudydruginit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('initiated', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('first_dose_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reason_not_init', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('reason_not_survive', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('reason_not_init_other', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantStudyDrugInit'])

        # Adding model 'InfantStudyDrugAudit'
        db.create_table('mpepu_infant_infantstudydrug_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantstudydrug', to=orm['mpepu_infant.InfantVisit'])),
            ('on_placebo_status', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('drug_status', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantStudyDrugAudit'])

        # Adding model 'InfantStudyDrug'
        db.create_table('mpepu_infant_infantstudydrug', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('on_placebo_status', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('drug_status', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantStudyDrug'])

        # Adding model 'InfantStudyDrugItemsAudit'
        db.create_table('mpepu_infant_infantstudydrugitems_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('inf_study_drug', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantstudydrugitems', to=orm['mpepu_infant.InfantStudyDrug'])),
            ('dose_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('igestion_date', self.gf('django.db.models.fields.DateField')()),
            ('modification_reason', self.gf('django.db.models.fields.CharField')(max_length=35)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantStudyDrugItemsAudit'])

        # Adding model 'InfantStudyDrugItems'
        db.create_table('mpepu_infant_infantstudydrugitems', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('inf_study_drug', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantStudyDrug'])),
            ('dose_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('igestion_date', self.gf('django.db.models.fields.DateField')()),
            ('modification_reason', self.gf('django.db.models.fields.CharField')(max_length=35)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantStudyDrugItems'])

        # Adding model 'InfantCtxPlaceboAdhAudit'
        db.create_table('mpepu_infant_infantctxplaceboadh_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantctxplaceboadh', to=orm['mpepu_infant.InfantVisit'])),
            ('day_missed_drug', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=50)),
            ('reason_missed_other', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantCtxPlaceboAdhAudit'])

        # Adding model 'InfantCtxPlaceboAdh'
        db.create_table('mpepu_infant_infantctxplaceboadh', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('day_missed_drug', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('reason_missed', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=50)),
            ('reason_missed_other', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantCtxPlaceboAdh'])

        # Adding model 'InfantFuAudit'
        db.create_table('mpepu_infant_infantfu_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfu', to=orm['mpepu_infant.InfantVisit'])),
            ('physical_assessment', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('diarrhea_illness', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuAudit'])

        # Adding model 'InfantFu'
        db.create_table('mpepu_infant_infantfu', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('physical_assessment', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('diarrhea_illness', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFu'])

        # Adding model 'InfantFuPhysicalAudit'
        db.create_table('mpepu_infant_infantfuphysical_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfuphysical', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfuphysical', to=orm['mpepu_infant.InfantFu'])),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('height', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('has_abnormalities', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('abnormalities', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('was_hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('days_hospitalized', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuPhysicalAudit'])

        # Adding model 'InfantFuPhysical'
        db.create_table('mpepu_infant_infantfuphysical', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFu'])),
            ('weight', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('height', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('has_abnormalities', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('abnormalities', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('was_hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('days_hospitalized', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuPhysical'])

        # Adding model 'InfantFuDxAudit'
        db.create_table('mpepu_infant_infantfudx_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfudx', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfudx', to=orm['mpepu_infant.InfantFu'])),
            ('has_dx', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDxAudit'])

        # Adding model 'InfantFuDx'
        db.create_table('mpepu_infant_infantfudx', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFu'])),
            ('has_dx', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDx'])

        # Adding model 'InfantFuDxItemsAudit'
        db.create_table('mpepu_infant_infantfudxitems_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_fu_dx', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfudxitems', to=orm['mpepu_infant.InfantFuDx'])),
            ('fu_dx', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fu_dx_specify', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('health_facility', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('was_hosptalized', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDxItemsAudit'])

        # Adding model 'InfantFuDxItems'
        db.create_table('mpepu_infant_infantfudxitems', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_fu_dx', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFuDx'])),
            ('fu_dx', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fu_dx_specify', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('health_facility', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('was_hosptalized', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDxItems'])

        # Adding model 'InfantFuDx2ProphAudit'
        db.create_table('mpepu_infant_infantfudx2proph_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfudx2proph', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfudx2proph', to=orm['mpepu_infant.InfantFu'])),
            ('has_dx', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('who_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDx2ProphAudit'])

        # Adding model 'InfantFuDx2Proph'
        db.create_table('mpepu_infant_infantfudx2proph', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFu'])),
            ('has_dx', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('who_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDx2Proph'])

        # Adding M2M table for field wcs_dx_ped on 'InfantFuDx2Proph'
        db.create_table('mpepu_infant_infantfudx2proph_wcs_dx_ped', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infantfudx2proph', models.ForeignKey(orm['mpepu_infant.infantfudx2proph'], null=False)),
            ('wcsdxped', models.ForeignKey(orm['bhp_code_lists.wcsdxped'], null=False))
        ))
        db.create_unique('mpepu_infant_infantfudx2proph_wcs_dx_ped', ['infantfudx2proph_id', 'wcsdxped_id'])

        # Adding model 'InfantFuDx2ProphItemsAudit'
        db.create_table('mpepu_infant_infantfudx2prophitems_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_fu_dx', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfudx2prophitems', to=orm['mpepu_infant.InfantFuDx2Proph'])),
            ('dx', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ctx', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nvp', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDx2ProphItemsAudit'])

        # Adding model 'InfantFuDx2ProphItems'
        db.create_table('mpepu_infant_infantfudx2prophitems', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_fu_dx', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFuDx2Proph'])),
            ('dx', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('ctx', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('nvp', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDx2ProphItems'])

        # Adding model 'InfantFuDAudit'
        db.create_table('mpepu_infant_infantfud_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfud', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfud', to=orm['mpepu_infant.InfantFu'])),
            ('diarrhea_grade', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('health_facility', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bloody_diarrhea', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('fever_present', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('diarrhea_episodes', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuDAudit'])

        # Adding model 'InfantFuD'
        db.create_table('mpepu_infant_infantfud', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFu'])),
            ('diarrhea_grade', self.gf('django.db.models.fields.IntegerField')(max_length=2)),
            ('health_facility', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('bloody_diarrhea', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('fever_present', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('diarrhea_episodes', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuD'])

        # Adding model 'InfantFuMedAudit'
        db.create_table('mpepu_infant_infantfumed_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfumed', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfumed', to=orm['mpepu_infant.InfantFu'])),
            ('vaccines_received', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuMedAudit'])

        # Adding model 'InfantFuMed'
        db.create_table('mpepu_infant_infantfumed', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFu'])),
            ('vaccines_received', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuMed'])

        # Adding M2M table for field vaccination on 'InfantFuMed'
        db.create_table('mpepu_infant_infantfumed_vaccination', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('infantfumed', models.ForeignKey(orm['mpepu_infant.infantfumed'], null=False)),
            ('infantvaccines', models.ForeignKey(orm['mpepu_list.infantvaccines'], null=False))
        ))
        db.create_unique('mpepu_infant_infantfumed_vaccination', ['infantfumed_id', 'infantvaccines_id'])

        # Adding model 'InfantFuNewMedAudit'
        db.create_table('mpepu_infant_infantfunewmed_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfunewmed', to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfunewmed', to=orm['mpepu_infant.InfantFu'])),
            ('new_medications', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('other_medications', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuNewMedAudit'])

        # Adding model 'InfantFuNewMed'
        db.create_table('mpepu_infant_infantfunewmed', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('infant_fu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFu'])),
            ('new_medications', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('other_medications', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuNewMed'])

        # Adding model 'InfantFuNewMedItemsAudit'
        db.create_table('mpepu_infant_infantfunewmeditems_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_fu_med', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfunewmeditems', to=orm['mpepu_infant.InfantFuNewMed'])),
            ('medication', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('drug_route', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuNewMedItemsAudit'])

        # Adding model 'InfantFuNewMedItems'
        db.create_table('mpepu_infant_infantfunewmeditems', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_fu_med', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantFuNewMed'])),
            ('medication', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('drug_route', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFuNewMedItems'])

        # Adding model 'InfantFeedingAudit'
        db.create_table('mpepu_infant_infantfeeding_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantfeeding', to=orm['mpepu_infant.InfantVisit'])),
            ('last_att_sche_visit', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('other_feeding', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('formula_intro_occur', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('formula_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reason_rcv_formula', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('reason_rcv_fm_other', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('water_used', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=50)),
            ('water_used_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('formula', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('water', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('juice', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('cow_milk', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('cow_milk_yes', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('other_milk', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('other_milk_animal', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('milk_boiled', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('fruits_veg', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('cereal_porridge', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=12)),
            ('solid_liquid', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('rehydration_salts', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('ever_breastfeed', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('complete_weaning', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('weaned_completely', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('most_recent_bm', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('times_breastfed', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=50)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFeedingAudit'])

        # Adding model 'InfantFeeding'
        db.create_table('mpepu_infant_infantfeeding', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'])),
            ('last_att_sche_visit', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('other_feeding', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('formula_intro_occur', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('formula_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reason_rcv_formula', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('reason_rcv_fm_other', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('water_used', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=50)),
            ('water_used_other', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('formula', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('water', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('juice', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('cow_milk', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('cow_milk_yes', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=25)),
            ('other_milk', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=15)),
            ('other_milk_animal', self.gf('django.db.models.fields.CharField')(max_length=35, null=True, blank=True)),
            ('milk_boiled', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('fruits_veg', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('cereal_porridge', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=12)),
            ('solid_liquid', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=10)),
            ('rehydration_salts', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('ever_breastfeed', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('complete_weaning', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('weaned_completely', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=3)),
            ('most_recent_bm', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('times_breastfed', self.gf('django.db.models.fields.CharField')(default='N/A', max_length=50)),
            ('comments', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantFeeding'])

        # Adding model 'InfantOffStudyAudit'
        db.create_table('mpepu_infant_infantoffstudy_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('offstudy_date', self.gf('django.db.models.fields.DateField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantoffstudy', to=orm['bhp_registration.RegisteredSubject'])),
        ))
        db.send_create_signal('mpepu_infant', ['InfantOffStudyAudit'])

        # Adding model 'InfantOffStudy'
        db.create_table('mpepu_infant_infantoffstudy', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
            ('offstudy_date', self.gf('django.db.models.fields.DateField')()),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('reason_other', self.gf('django.db.models.fields.CharField')(max_length=35, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantOffStudy'])

        # Adding model 'InfantVerbalAutopsyAudit'
        db.create_table('mpepu_infant_infantverbalautopsy_audit', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
            ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantverbalautopsy', to=orm['bhp_registration.RegisteredSubject'])),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_sign', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('prop_cause', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('_audit_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
            ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantVerbalAutopsyAudit'])

        # Adding model 'InfantVerbalAutopsy'
        db.create_table('mpepu_infant_infantverbalautopsy', (
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, blank=True)),
            ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
            ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject'])),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_sign', self.gf('django.db.models.fields.TextField')(max_length=1000)),
            ('prop_cause', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal('mpepu_infant', ['InfantVerbalAutopsy'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'InfantBirth', fields ['initials', 'maternal_lab_del']
        db.delete_unique('mpepu_infant_infantbirth', ['initials', 'maternal_lab_del_id'])

        # Deleting model 'InfantVisitAudit'
        db.delete_table('mpepu_infant_infantvisit_audit')

        # Deleting model 'InfantVisit'
        db.delete_table('mpepu_infant_infantvisit')

        # Deleting model 'InfantBirthAudit'
        db.delete_table('mpepu_infant_infantbirth_audit')

        # Deleting model 'InfantBirth'
        db.delete_table('mpepu_infant_infantbirth')

        # Deleting model 'InfantBirthDataAudit'
        db.delete_table('mpepu_infant_infantbirthdata_audit')

        # Deleting model 'InfantBirthData'
        db.delete_table('mpepu_infant_infantbirthdata')

        # Deleting model 'InfantBirthExamAudit'
        db.delete_table('mpepu_infant_infantbirthexam_audit')

        # Deleting model 'InfantBirthExam'
        db.delete_table('mpepu_infant_infantbirthexam')

        # Deleting model 'InfantBirthArvAudit'
        db.delete_table('mpepu_infant_infantbirtharv_audit')

        # Deleting model 'InfantBirthArv'
        db.delete_table('mpepu_infant_infantbirtharv')

        # Deleting model 'InfantBirthFeedAudit'
        db.delete_table('mpepu_infant_infantbirthfeed_audit')

        # Deleting model 'InfantBirthFeed'
        db.delete_table('mpepu_infant_infantbirthfeed')

        # Removing M2M table for field vaccination on 'InfantBirthFeed'
        db.delete_table('mpepu_infant_infantbirthfeed_vaccination')

        # Deleting model 'InfantEligibilityAudit'
        db.delete_table('mpepu_infant_infanteligibility_audit')

        # Deleting model 'InfantEligibility'
        db.delete_table('mpepu_infant_infanteligibility')

        # Deleting model 'InfantArvProphAudit'
        db.delete_table('mpepu_infant_infantarvproph_audit')

        # Deleting model 'InfantArvProph'
        db.delete_table('mpepu_infant_infantarvproph')

        # Deleting model 'InfantArvProphModAudit'
        db.delete_table('mpepu_infant_infantarvprophmod_audit')

        # Deleting model 'InfantArvProphMod'
        db.delete_table('mpepu_infant_infantarvprophmod')

        # Deleting model 'InfantDeathAudit'
        db.delete_table('mpepu_infant_infantdeath_audit')

        # Deleting model 'InfantDeath'
        db.delete_table('mpepu_infant_infantdeath')

        # Deleting model 'InfantHaartAudit'
        db.delete_table('mpepu_infant_infanthaart_audit')

        # Deleting model 'InfantHaart'
        db.delete_table('mpepu_infant_infanthaart')

        # Deleting model 'InfantHaartModAudit'
        db.delete_table('mpepu_infant_infanthaartmod_audit')

        # Deleting model 'InfantHaartMod'
        db.delete_table('mpepu_infant_infanthaartmod')

        # Deleting model 'InfantOffDrugAudit'
        db.delete_table('mpepu_infant_infantoffdrug_audit')

        # Deleting model 'InfantOffDrug'
        db.delete_table('mpepu_infant_infantoffdrug')

        # Deleting model 'InfantSurvivalAudit'
        db.delete_table('mpepu_infant_infantsurvival_audit')

        # Deleting model 'InfantSurvival'
        db.delete_table('mpepu_infant_infantsurvival')

        # Deleting model 'InfantNvpAdherenceAudit'
        db.delete_table('mpepu_infant_infantnvpadherence_audit')

        # Deleting model 'InfantNvpAdherence'
        db.delete_table('mpepu_infant_infantnvpadherence')

        # Deleting model 'InfantPrerandoLossAudit'
        db.delete_table('mpepu_infant_infantprerandoloss_audit')

        # Deleting model 'InfantPrerandoLoss'
        db.delete_table('mpepu_infant_infantprerandoloss')

        # Deleting model 'InfantStudyDrugInitAudit'
        db.delete_table('mpepu_infant_infantstudydruginit_audit')

        # Deleting model 'InfantStudyDrugInit'
        db.delete_table('mpepu_infant_infantstudydruginit')

        # Deleting model 'InfantStudyDrugAudit'
        db.delete_table('mpepu_infant_infantstudydrug_audit')

        # Deleting model 'InfantStudyDrug'
        db.delete_table('mpepu_infant_infantstudydrug')

        # Deleting model 'InfantStudyDrugItemsAudit'
        db.delete_table('mpepu_infant_infantstudydrugitems_audit')

        # Deleting model 'InfantStudyDrugItems'
        db.delete_table('mpepu_infant_infantstudydrugitems')

        # Deleting model 'InfantCtxPlaceboAdhAudit'
        db.delete_table('mpepu_infant_infantctxplaceboadh_audit')

        # Deleting model 'InfantCtxPlaceboAdh'
        db.delete_table('mpepu_infant_infantctxplaceboadh')

        # Deleting model 'InfantFuAudit'
        db.delete_table('mpepu_infant_infantfu_audit')

        # Deleting model 'InfantFu'
        db.delete_table('mpepu_infant_infantfu')

        # Deleting model 'InfantFuPhysicalAudit'
        db.delete_table('mpepu_infant_infantfuphysical_audit')

        # Deleting model 'InfantFuPhysical'
        db.delete_table('mpepu_infant_infantfuphysical')

        # Deleting model 'InfantFuDxAudit'
        db.delete_table('mpepu_infant_infantfudx_audit')

        # Deleting model 'InfantFuDx'
        db.delete_table('mpepu_infant_infantfudx')

        # Deleting model 'InfantFuDxItemsAudit'
        db.delete_table('mpepu_infant_infantfudxitems_audit')

        # Deleting model 'InfantFuDxItems'
        db.delete_table('mpepu_infant_infantfudxitems')

        # Deleting model 'InfantFuDx2ProphAudit'
        db.delete_table('mpepu_infant_infantfudx2proph_audit')

        # Deleting model 'InfantFuDx2Proph'
        db.delete_table('mpepu_infant_infantfudx2proph')

        # Removing M2M table for field wcs_dx_ped on 'InfantFuDx2Proph'
        db.delete_table('mpepu_infant_infantfudx2proph_wcs_dx_ped')

        # Deleting model 'InfantFuDx2ProphItemsAudit'
        db.delete_table('mpepu_infant_infantfudx2prophitems_audit')

        # Deleting model 'InfantFuDx2ProphItems'
        db.delete_table('mpepu_infant_infantfudx2prophitems')

        # Deleting model 'InfantFuDAudit'
        db.delete_table('mpepu_infant_infantfud_audit')

        # Deleting model 'InfantFuD'
        db.delete_table('mpepu_infant_infantfud')

        # Deleting model 'InfantFuMedAudit'
        db.delete_table('mpepu_infant_infantfumed_audit')

        # Deleting model 'InfantFuMed'
        db.delete_table('mpepu_infant_infantfumed')

        # Removing M2M table for field vaccination on 'InfantFuMed'
        db.delete_table('mpepu_infant_infantfumed_vaccination')

        # Deleting model 'InfantFuNewMedAudit'
        db.delete_table('mpepu_infant_infantfunewmed_audit')

        # Deleting model 'InfantFuNewMed'
        db.delete_table('mpepu_infant_infantfunewmed')

        # Deleting model 'InfantFuNewMedItemsAudit'
        db.delete_table('mpepu_infant_infantfunewmeditems_audit')

        # Deleting model 'InfantFuNewMedItems'
        db.delete_table('mpepu_infant_infantfunewmeditems')

        # Deleting model 'InfantFeedingAudit'
        db.delete_table('mpepu_infant_infantfeeding_audit')

        # Deleting model 'InfantFeeding'
        db.delete_table('mpepu_infant_infantfeeding')

        # Deleting model 'InfantOffStudyAudit'
        db.delete_table('mpepu_infant_infantoffstudy_audit')

        # Deleting model 'InfantOffStudy'
        db.delete_table('mpepu_infant_infantoffstudy')

        # Deleting model 'InfantVerbalAutopsyAudit'
        db.delete_table('mpepu_infant_infantverbalautopsy_audit')

        # Deleting model 'InfantVerbalAutopsy'
        db.delete_table('mpepu_infant_infantverbalautopsy')


    models = {
        'bhp_adverse.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathcauseinfo': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathmedicalresponsibility': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathMedicalResponsibility'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathreasonhospitalized': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathReasonHospitalized'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'unique_together': "[('registered_subject', 'visit_definition', 'visit_instance')]", 'object_name': 'Appointment', 'db_table': "'bhp_form_appointment'"},
            'appt_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'appt_reason': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'appt_status': ('django.db.models.fields.CharField', [], {'default': "'NEW'", 'max_length': '25'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_visit.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'bhp_code_lists.dxcode': {
            'Meta': {'object_name': 'DxCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_code_lists.wcsdxped': {
            'Meta': {'object_name': 'WcsDxPed'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_common.contenttypemap': {
            'Meta': {'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_registration.registeredsubject': {
            'Meta': {'object_name': 'RegisteredSubject'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_visit.membershipform': {
            'Meta': {'object_name': 'MembershipForm', 'db_table': "'bhp_form_membershipform'"},
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '25', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_common.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hide_from_dashboard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_visit.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup', 'db_table': "'bhp_form_schedulegroup'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'membership_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_visit.MembershipForm']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_visit.visitdefinition': {
            'Meta': {'ordering': "['code', 'time_point']", 'object_name': 'VisitDefinition', 'db_table': "'bhp_form_visitdefinition'"},
            'base_interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_interval_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'lower_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lower_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'schedule_group': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_visit.ScheduleGroup']", 'symmetrical': 'False'}),
            'time_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'upper_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upper_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mpepu_infant.infantarvproph': {
            'Meta': {'object_name': 'InfantArvProph'},
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prophylatic_nvp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantarvprophaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantArvProphAudit', 'db_table': "'mpepu_infant_infantarvproph_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantarvproph'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prophylatic_nvp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantarvprophmod': {
            'Meta': {'object_name': 'InfantArvProphMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantArvProph']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantarvprophmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantArvProphModAudit', 'db_table': "'mpepu_infant_infantarvprophmod_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantarvprophmod'", 'to': "orm['mpepu_infant.InfantArvProph']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirth': {
            'Meta': {'unique_together': "(['initials', 'maternal_lab_del'],)", 'object_name': 'InfantBirth'},
            'birth_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirtharv': {
            'Meta': {'object_name': 'InfantBirthArv'},
            'additional_nvp_doses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_additional_dose': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nvp_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sdnvp_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirtharvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthArvAudit', 'db_table': "'mpepu_infant_infantbirtharv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'additional_nvp_doses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_additional_dose': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_arv_comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirtharv'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirtharv'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nvp_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sdnvp_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirthaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthAudit', 'db_table': "'mpepu_infant_infantbirth_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'birth_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirth'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirth'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirthdata': {
            'Meta': {'object_name': 'InfantBirthData'},
            'apgar_score': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'apgar_score_min_1': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'apgar_score_min_10': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'apgar_score_min_5': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalities': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'head_circumference': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_birth_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'infant_length': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_birth_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirthdataaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthDataAudit', 'db_table': "'mpepu_infant_infantbirthdata_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'apgar_score': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'apgar_score_min_1': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'apgar_score_min_10': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'apgar_score_min_5': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalities': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'head_circumference': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthdata'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_birth_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'infant_length': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthdata'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_birth_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirthexam': {
            'Meta': {'object_name': 'InfantBirthExam'},
            'abdominal_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'abdominal_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'abnormal_activity': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cardiac_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'cardiac_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'general_activity': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'heent_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'heent_no_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_exam_date': ('django.db.models.fields.DateField', [], {}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'macular_papular_rash': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'neuro_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neurologic_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'other_exam_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'physical_exam_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'resp_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'resp_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skin_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'skin_exam_other': ('django.db.models.fields.TextField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirthexamaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthExamAudit', 'db_table': "'mpepu_infant_infantbirthexam_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'abdominal_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'abdominal_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'abnormal_activity': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cardiac_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'cardiac_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'general_activity': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'heent_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'heent_no_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthexam'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_exam_date': ('django.db.models.fields.DateField', [], {}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthexam'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'macular_papular_rash': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'neuro_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neurologic_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'other_exam_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'physical_exam_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'resp_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'resp_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'skin_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'skin_exam_other': ('django.db.models.fields.TextField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantbirthfeed': {
            'Meta': {'object_name': 'InfantBirthFeed'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_after_delivery': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vaccination': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.InfantVaccines']", 'symmetrical': 'False'})
        },
        'mpepu_infant.infantbirthfeedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthFeedAudit', 'db_table': "'mpepu_infant_infantbirthfeed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_after_delivery': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthfeed'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthfeed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantctxplaceboadh': {
            'Meta': {'object_name': 'InfantCtxPlaceboAdh'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'day_missed_drug': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'reason_missed_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantctxplaceboadhaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantCtxPlaceboAdhAudit', 'db_table': "'mpepu_infant_infantctxplaceboadh_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'day_missed_drug': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantctxplaceboadh'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'reason_missed_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantdeath': {
            'Meta': {'object_name': 'InfantDeath'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {}),
            'death_cause': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathReasonHospitalized']"}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_code_lists.DxCode']", 'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantdeathaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantDeathAudit', 'db_table': "'mpepu_infant_infantdeath_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {}),
            'death_cause': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathReasonHospitalized']"}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'max_length': '25', 'to': "orm['bhp_code_lists.DxCode']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infanteligibility': {
            'Meta': {'object_name': 'InfantEligibility'},
            'congen_anomaly': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx_contra': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'maternal_art_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'maternal_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_site': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infanteligibilityaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantEligibilityAudit', 'db_table': "'mpepu_infant_infanteligibility_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'congen_anomaly': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx_contra': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanteligibility'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'maternal_art_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'maternal_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_site': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanteligibility'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfeeding': {
            'Meta': {'object_name': 'InfantFeeding'},
            'cereal_porridge': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '12'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complete_weaning': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'cow_milk': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'cow_milk_yes': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ever_breastfeed': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'formula': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'formula_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'formula_intro_occur': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'fruits_veg': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'juice': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'last_att_sche_visit': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'milk_boiled': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'most_recent_bm': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'other_feeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'other_milk': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'other_milk_animal': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'reason_rcv_fm_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_rcv_formula': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'rehydration_salts': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'solid_liquid': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'times_breastfed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'water': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'water_used': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'water_used_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'weaned_completely': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'})
        },
        'mpepu_infant.infantfeedingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFeedingAudit', 'db_table': "'mpepu_infant_infantfeeding_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cereal_porridge': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '12'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'complete_weaning': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'cow_milk': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'cow_milk_yes': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ever_breastfeed': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'formula': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'formula_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'formula_intro_occur': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'fruits_veg': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfeeding'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'juice': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'last_att_sche_visit': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'milk_boiled': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'most_recent_bm': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'other_feeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'other_milk': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'other_milk_animal': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'reason_rcv_fm_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_rcv_formula': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'rehydration_salts': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'}),
            'solid_liquid': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'times_breastfed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'water': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'water_used': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'water_used_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'weaned_completely': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'})
        },
        'mpepu_infant.infantfu': {
            'Meta': {'object_name': 'InfantFu'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_illness': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_assessment': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfuaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuAudit', 'db_table': "'mpepu_infant_infantfu_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_illness': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfu'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_assessment': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfud': {
            'Meta': {'object_name': 'InfantFuD'},
            'bloody_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_episodes': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diarrhea_grade': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'fever_present': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfudaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDAudit', 'db_table': "'mpepu_infant_infantfud_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bloody_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_episodes': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diarrhea_grade': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'fever_present': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfud'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfud'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfudx': {
            'Meta': {'object_name': 'InfantFuDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfudx2proph': {
            'Meta': {'object_name': 'InfantFuDx2Proph'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'wcs_dx_ped': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_code_lists.WcsDxPed']", 'symmetrical': 'False'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfudx2prophaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDx2ProphAudit', 'db_table': "'mpepu_infant_infantfudx2proph_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2proph'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2proph'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfudx2prophitems': {
            'Meta': {'object_name': 'InfantFuDx2ProphItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuDx2Proph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfudx2prophitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDx2ProphItemsAudit', 'db_table': "'mpepu_infant_infantfudx2prophitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2prophitems'", 'to': "orm['mpepu_infant.InfantFuDx2Proph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfudxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDxAudit', 'db_table': "'mpepu_infant_infantfudx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfudxitems': {
            'Meta': {'object_name': 'InfantFuDxItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fu_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'was_hosptalized': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_infant.infantfudxitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDxItemsAudit', 'db_table': "'mpepu_infant_infantfudxitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'fu_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudxitems'", 'to': "orm['mpepu_infant.InfantFuDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'was_hosptalized': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_infant.infantfumed': {
            'Meta': {'object_name': 'InfantFuMed'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vaccination': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.InfantVaccines']", 'symmetrical': 'False'}),
            'vaccines_received': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfumedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuMedAudit', 'db_table': "'mpepu_infant_infantfumed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfumed'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfumed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vaccines_received': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfunewmed': {
            'Meta': {'object_name': 'InfantFuNewMed'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'new_medications': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_medications': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfunewmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuNewMedAudit', 'db_table': "'mpepu_infant_infantfunewmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmed'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'new_medications': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_medications': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfunewmeditems': {
            'Meta': {'object_name': 'InfantFuNewMedItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_route': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_med': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuNewMed']"}),
            'medication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfunewmeditemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuNewMedItemsAudit', 'db_table': "'mpepu_infant_infantfunewmeditems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_route': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu_med': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmeditems'", 'to': "orm['mpepu_infant.InfantFuNewMed']"}),
            'medication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantfuphysical': {
            'Meta': {'object_name': 'InfantFuPhysical'},
            'abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'mpepu_infant.infantfuphysicalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuPhysicalAudit', 'db_table': "'mpepu_infant_infantfuphysical_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfuphysical'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfuphysical'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'mpepu_infant.infanthaart': {
            'Meta': {'object_name': 'InfantHaart'},
            'arv_status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'haart_initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hiv_positive_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infanthaartaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHaartAudit', 'db_table': "'mpepu_infant_infanthaart_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'haart_initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hiv_positive_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthaart'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infanthaartmod': {
            'Meta': {'object_name': 'InfantHaartMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_haart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantHaart']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infanthaartmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHaartModAudit', 'db_table': "'mpepu_infant_infanthaartmod_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_haart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthaartmod'", 'to': "orm['mpepu_infant.InfantHaart']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantnvpadherence': {
            'Meta': {'object_name': 'InfantNvpAdherence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_missed': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantArvProph']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'reason_missed_other': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantnvpadherenceaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantNvpAdherenceAudit', 'db_table': "'mpepu_infant_infantnvpadherence_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_missed': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantnvpadherence'", 'to': "orm['mpepu_infant.InfantArvProph']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantnvpadherence'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'reason_missed_other': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantoffdrug': {
            'Meta': {'object_name': 'InfantOffDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'last_dose_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_off': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_off_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantoffdrugaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantOffDrugAudit', 'db_table': "'mpepu_infant_infantoffdrug_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'last_dose_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_off': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_off_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffdrug'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantoffstudy': {
            'Meta': {'object_name': 'InfantOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantoffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantOffStudyAudit', 'db_table': "'mpepu_infant_infantoffstudy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffstudy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantprerandoloss': {
            'Meta': {'object_name': 'InfantPrerandoLoss'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'loss_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_loss': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'reason_loss_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantprerandolossaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantPrerandoLossAudit', 'db_table': "'mpepu_infant_infantprerandoloss_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'loss_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_loss': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'reason_loss_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantprerandoloss'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantstudydrug': {
            'Meta': {'object_name': 'InfantStudyDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_placebo_status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantstudydrugaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugAudit', 'db_table': "'mpepu_infant_infantstudydrug_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydrug'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_placebo_status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantstudydruginit': {
            'Meta': {'object_name': 'InfantStudyDrugInit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_not_init': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'reason_not_init_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_not_survive': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantstudydruginitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugInitAudit', 'db_table': "'mpepu_infant_infantstudydruginit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydruginit'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_not_init': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'reason_not_init_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_not_survive': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantstudydrugitems': {
            'Meta': {'object_name': 'InfantStudyDrugItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'igestion_date': ('django.db.models.fields.DateField', [], {}),
            'inf_study_drug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantStudyDrug']"}),
            'modification_reason': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantstudydrugitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugItemsAudit', 'db_table': "'mpepu_infant_infantstudydrugitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'igestion_date': ('django.db.models.fields.DateField', [], {}),
            'inf_study_drug': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydrugitems'", 'to': "orm['mpepu_infant.InfantStudyDrug']"}),
            'modification_reason': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantsurvival': {
            'Meta': {'object_name': 'InfantSurvival'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_survival_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantsurvivalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantSurvivalAudit', 'db_table': "'mpepu_infant_infantsurvival_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_survival_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantsurvival'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantverbalautopsy': {
            'Meta': {'object_name': 'InfantVerbalAutopsy'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_sign': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prop_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_registration.RegisteredSubject']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantverbalautopsyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantVerbalAutopsyAudit', 'db_table': "'mpepu_infant_infantverbalautopsy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_sign': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prop_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantverbalautopsy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantvisit': {
            'Meta': {'object_name': 'InfantVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'information_provider': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'information_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'study_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_infant.infantvisitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantVisitAudit', 'db_table': "'mpepu_infant_infantvisit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantvisit'", 'to': "orm['bhp_appointment.Appointment']"}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'information_provider': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'information_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'study_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_list.delcomp': {
            'Meta': {'object_name': 'DelComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.infantvaccines': {
            'Meta': {'object_name': 'InfantVaccines'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_maternal.maternallabdel': {
            'Meta': {'object_name': 'MaternalLabDel'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'del_comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'del_comp': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.DelComp']", 'symmetrical': 'False'}),
            'del_comp_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'del_hosp': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'del_hosp_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'del_mode': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'del_time_is_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'delivery_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'has_chorioamnionitis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_del_comp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_urine_tender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'labour_hrs': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'labr_max_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'live_infants': ('django.db.models.fields.IntegerField', [], {}),
            'live_infants_to_register': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'still_born_congen_abn': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'still_born_has_congen_abn': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'still_borns': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalvisit': {
            'Meta': {'object_name': 'MaternalVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        }
    }

    complete_apps = ['mpepu_infant']
