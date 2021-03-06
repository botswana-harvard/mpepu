# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'InfantVitalStatusAudit'
#         db.delete_table('mpepu_infant_infantvitalstatus_audit')

        # Deleting model 'InfantVitalStatus'
#         db.delete_table(u'mpepu_infant_infantvitalstatus')

        # Adding model 'InfantStoolCollection'
#         db.create_table(u'mpepu_infant_infantstoolcollection', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0))),
#             ('infant_visit', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True)),
#             ('sample_obtained', self.gf('django.db.models.fields.CharField')(max_length=3)),
#             ('axi_temp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
#             ('past_diarrhea', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
#             ('diarrhea_past_24hrs', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
#             ('antibiotics_7days', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
#             ('antibiotic_dose_24hrs', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
#         ))
#         db.send_create_signal('mpepu_infant', ['InfantStoolCollection'])

        # Adding model 'InfantStoolCollectionAudit'
#         db.create_table(u'mpepu_infant_infantstoolcollection_audit', (
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='s007', max_length=50, db_index=True, blank=True)),
#             ('revision', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
#             ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
#             ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0))),
#             ('sample_obtained', self.gf('django.db.models.fields.CharField')(max_length=3)),
#             ('axi_temp', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=3, decimal_places=1, blank=True)),
#             ('past_diarrhea', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
#             ('diarrhea_past_24hrs', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
#             ('antibiotics_7days', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
#             ('antibiotic_dose_24hrs', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
#             ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, db_index=True, blank=True)),
#             ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36)),
#             ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantstoolcollection', to=orm['mpepu_infant.InfantVisit'])),
#         ))
#         db.send_create_signal('mpepu_infant', ['InfantStoolCollectionAudit'])

        # Adding field 'InfantMouthUpGastrointestinalItems.revision'
        db.add_column(u'mpepu_infant_infantmouthupgastrointestinalitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantMouthUpGastrointestinalItems.report_datetime'
        db.add_column(u'mpepu_infant_infantmouthupgastrointestinalitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuMed.revision'
        db.add_column(u'mpepu_infant_infantfumed', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuMed.report_datetime'
        db.add_column(u'mpepu_infant_infantfumed', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantFuMed.infant_visit'
        db.alter_column(u'mpepu_infant_infantfumed', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFuMed', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfumed', ['infant_visit_id'])

        # Adding field 'InfantHaartAudit.revision'
        db.add_column(u'mpepu_infant_infanthaart_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantHaartAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infanthaart_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantFuMedAudit.revision'
        db.add_column(u'mpepu_infant_infantfumed_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuMedAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfumed_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOffStudyAudit.revision'
        db.add_column(u'mpepu_infant_infantoffstudy_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantOffStudyAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantoffstudy_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOffStudyAudit.infant_visit'
        db.add_column(u'mpepu_infant_infantoffstudy_audit', 'infant_visit',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='_audit_infantoffstudy', to=orm['mpepu_infant.InfantVisit']),
                      keep_default=False)


        # Changing field 'InfantOffStudyAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantoffstudy_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantBirth.revision'
        db.add_column(u'mpepu_infant_infantbirth', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantBirth.registered_subject'
        db.alter_column(u'mpepu_infant_infantbirth', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantSkinAbnormalItems.revision'
        db.add_column(u'mpepu_infant_infantskinabnormalitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantSkinAbnormalItems.report_datetime'
        db.add_column(u'mpepu_infant_infantskinabnormalitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOffStudy.revision'
        db.add_column(u'mpepu_infant_infantoffstudy', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantOffStudy.infant_visit'
        db.add_column(u'mpepu_infant_infantoffstudy', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)

        # Adding field 'InfantOffStudy.report_datetime'
        db.add_column(u'mpepu_infant_infantoffstudy', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantOffStudy.registered_subject'
        db.alter_column(u'mpepu_infant_infantoffstudy', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantRandoDeferralAudit.revision'
        db.add_column(u'mpepu_infant_infantrandodeferral_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantRandoDeferralAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantrandodeferral_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantFuPhysical.revision'
        db.add_column(u'mpepu_infant_infantfuphysical', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuPhysical.report_datetime'
        db.add_column(u'mpepu_infant_infantfuphysical', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuPhysical.head_circumference'
        db.add_column(u'mpepu_infant_infantfuphysical', 'head_circumference',
                      self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=5, decimal_places=2),
                      keep_default=False)


        # Changing field 'InfantFuPhysical.infant_visit'
        db.alter_column(u'mpepu_infant_infantfuphysical', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFuPhysical', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfuphysical', ['infant_visit_id'])

        # Adding field 'InfantFemaleGenitalAnomalyItems.revision'
        db.add_column(u'mpepu_infant_infantfemalegenitalanomalyitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFemaleGenitalAnomalyItems.report_datetime'
        db.add_column(u'mpepu_infant_infantfemalegenitalanomalyitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuDAudit.revision'
        db.add_column(u'mpepu_infant_infantfud_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfud_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuDAudit.d_onset_date'
        db.add_column(u'mpepu_infant_infantfud_audit', 'd_onset_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuD.revision'
        db.add_column(u'mpepu_infant_infantfud', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuD.report_datetime'
        db.add_column(u'mpepu_infant_infantfud', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuD.d_onset_date'
        db.add_column(u'mpepu_infant_infantfud', 'd_onset_date',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantFuD.infant_visit'
        db.alter_column(u'mpepu_infant_infantfud', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFuD', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfud', ['infant_visit_id'])

        # Adding field 'InfantFu.revision'
        db.add_column(u'mpepu_infant_infantfu', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFu.report_datetime'
        db.add_column(u'mpepu_infant_infantfu', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantFu.infant_visit'
        db.alter_column(u'mpepu_infant_infantfu', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFu', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfu', ['infant_visit_id'])

        # Adding field 'InfantFuDxItemsAudit.revision'
        db.add_column(u'mpepu_infant_infantfudxitems_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugItemsAudit.revision'
        db.add_column(u'mpepu_infant_infantstudydrugitems_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugItemsAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantstudydrugitems_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantCongenitalAnomalies.revision'
        db.add_column(u'mpepu_infant_infantcongenitalanomalies', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCongenitalAnomalies.infant_visit'
        db.add_column(u'mpepu_infant_infantcongenitalanomalies', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)


        # Changing field 'InfantCongenitalAnomalies.registered_subject'
        db.alter_column(u'mpepu_infant_infantcongenitalanomalies', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantCardiovascularDisorderItems.revision'
        db.add_column(u'mpepu_infant_infantcardiovasculardisorderitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCardiovascularDisorderItems.report_datetime'
        db.add_column(u'mpepu_infant_infantcardiovasculardisorderitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantArvProph.revision'
        db.add_column(u'mpepu_infant_infantarvproph', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantArvProph.report_datetime'
        db.add_column(u'mpepu_infant_infantarvproph', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantArvProph.infant_visit'
        db.alter_column(u'mpepu_infant_infantarvproph', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantArvProph', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantarvproph', ['infant_visit_id'])

        # Adding field 'InfantStudyDrugAudit.revision'
        db.add_column(u'mpepu_infant_infantstudydrug_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantstudydrug_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantHivStatusAudit.revision'
        db.add_column(u'mpepu_infant_infanthivstatus_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantHivStatusAudit.report_datetime'
        db.add_column(u'mpepu_infant_infanthivstatus_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantArvProphAudit.revision'
        db.add_column(u'mpepu_infant_infantarvproph_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantArvProphAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantarvproph_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuNewMedItems.revision'
        db.add_column(u'mpepu_infant_infantfunewmeditems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuNewMedItems.report_datetime'
        db.add_column(u'mpepu_infant_infantfunewmeditems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantHaart.revision'
        db.add_column(u'mpepu_infant_infanthaart', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantHaart.registered_subject'
        db.alter_column(u'mpepu_infant_infanthaart', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantLowerGastrointestinalItems.revision'
        db.add_column(u'mpepu_infant_infantlowergastrointestinalitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantLowerGastrointestinalItems.report_datetime'
        db.add_column(u'mpepu_infant_infantlowergastrointestinalitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantMaleGenitalAnomalyItems.revision'
        db.add_column(u'mpepu_infant_infantmalegenitalanomalyitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantMaleGenitalAnomalyItems.report_datetime'
        db.add_column(u'mpepu_infant_infantmalegenitalanomalyitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantStudyDrugInit.revision'
        db.add_column(u'mpepu_infant_infantstudydruginit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugInit.report_datetime'
        db.add_column(u'mpepu_infant_infantstudydruginit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantStudyDrugInit.infant_visit'
        db.alter_column(u'mpepu_infant_infantstudydruginit', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantStudyDrugInit', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantstudydruginit', ['infant_visit_id'])

        # Adding field 'InfantHaartModAudit.revision'
        db.add_column(u'mpepu_infant_infanthaartmod_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx2ProphItemsAudit.revision'
        db.add_column(u'mpepu_infant_infantfudx2prophitems_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx2ProphItemsAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfudx2prophitems_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantNvpAdherenceAudit.revision'
        db.add_column(u'mpepu_infant_infantnvpadherence_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantNvpAdherenceAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantnvpadherence_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuNewMedItemsAudit.revision'
        db.add_column(u'mpepu_infant_infantfunewmeditems_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuNewMedItemsAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfunewmeditems_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantMusculoskeletalAbnormalItems.revision'
        db.add_column(u'mpepu_infant_infantmusculoskeletalabnormalitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantMusculoskeletalAbnormalItems.report_datetime'
        db.add_column(u'mpepu_infant_infantmusculoskeletalabnormalitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantHivStatus.revision'
        db.add_column(u'mpepu_infant_infanthivstatus', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantHivStatus.report_datetime'
        db.add_column(u'mpepu_infant_infanthivstatus', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantHivStatus.infant_visit'
        db.alter_column(u'mpepu_infant_infanthivstatus', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantHivStatus', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infanthivstatus', ['infant_visit_id'])

        # Adding field 'InfantDeath.revision'
        db.add_column(u'mpepu_infant_infantdeath', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantDeath.infant_visit'
        db.add_column(u'mpepu_infant_infantdeath', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)


        # Changing field 'InfantDeath.dx_code'
        db.alter_column(u'mpepu_infant_infantdeath', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['code_lists.DxCode'], max_length=25))

        # Changing field 'InfantDeath.death_cause_category'
        db.alter_column(u'mpepu_infant_infantdeath', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseCategory']))

        # Changing field 'InfantDeath.registered_subject'
        db.alter_column(u'mpepu_infant_infantdeath', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))

        # Changing field 'InfantDeath.death_reason_hospitalized'
        db.alter_column(u'mpepu_infant_infantdeath', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathReasonHospitalized'], null=True))

        # Changing field 'InfantDeath.death_cause_info'
        db.alter_column(u'mpepu_infant_infantdeath', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseInfo']))

        # Changing field 'InfantDeath.death_medical_responsibility'
        db.alter_column(u'mpepu_infant_infantdeath', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathMedicalResponsibility']))
        # Adding field 'InfantSurvival.revision'
        db.add_column(u'mpepu_infant_infantsurvival', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantSurvival.infant_visit'
        db.add_column(u'mpepu_infant_infantsurvival', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)


        # Changing field 'InfantSurvival.registered_subject'
        db.alter_column(u'mpepu_infant_infantsurvival', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantFuAudit.revision'
        db.add_column(u'mpepu_infant_infantfu_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfu_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantBirthFeed.revision'
        db.add_column(u'mpepu_infant_infantbirthfeed', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthFeed.report_datetime'
        db.add_column(u'mpepu_infant_infantbirthfeed', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantBirthFeed.infant_visit'
        db.alter_column(u'mpepu_infant_infantbirthfeed', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantBirthFeed', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantbirthfeed', ['infant_visit_id'])

        # Adding field 'InfantEligibilityAudit.revision'
        db.add_column(u'mpepu_infant_infanteligibility_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantEligibilityAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infanteligibility_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantStudyDrug.revision'
        db.add_column(u'mpepu_infant_infantstudydrug', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrug.report_datetime'
        db.add_column(u'mpepu_infant_infantstudydrug', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantStudyDrug.infant_visit'
        db.alter_column(u'mpepu_infant_infantstudydrug', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantStudyDrug', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantstudydrug', ['infant_visit_id'])

        # Adding field 'InfantRandoDeferral.revision'
        db.add_column(u'mpepu_infant_infantrandodeferral', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantRandoDeferral.registered_subject'
        db.alter_column(u'mpepu_infant_infantrandodeferral', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantBirthExamAudit.revision'
        db.add_column(u'mpepu_infant_infantbirthexam_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthExamAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantbirthexam_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOffDrug.revision'
        db.add_column(u'mpepu_infant_infantoffdrug', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantOffDrug.report_datetime'
        db.add_column(u'mpepu_infant_infantoffdrug', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOffDrug.infant_visit'
        db.add_column(u'mpepu_infant_infantoffdrug', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)


        # Changing field 'InfantOffDrug.registered_subject'
        db.alter_column(u'mpepu_infant_infantoffdrug', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantFeeding.revision'
        db.add_column(u'mpepu_infant_infantfeeding', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFeeding.report_datetime'
        db.add_column(u'mpepu_infant_infantfeeding', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantFeeding.infant_visit'
        db.alter_column(u'mpepu_infant_infantfeeding', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFeeding', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfeeding', ['infant_visit_id'])

        # Adding field 'InfantFeedingAudit.revision'
        db.add_column(u'mpepu_infant_infantfeeding_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFeedingAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfeeding_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantDeathAudit.revision'
        db.add_column(u'mpepu_infant_infantdeath_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantDeathAudit.infant_visit'
        db.add_column(u'mpepu_infant_infantdeath_audit', 'infant_visit',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='_audit_infantdeath', to=orm['mpepu_infant.InfantVisit']),
                      keep_default=False)


        # Changing field 'InfantDeathAudit.dx_code'
        db.alter_column(u'mpepu_infant_infantdeath_audit', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(max_length=25, to=orm['code_lists.DxCode']))

        # Changing field 'InfantDeathAudit.death_cause_category'
        db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseCategory']))

        # Changing field 'InfantDeathAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantdeath_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))

        # Changing field 'InfantDeathAudit.death_reason_hospitalized'
        db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['adverse_event.DeathReasonHospitalized']))

        # Changing field 'InfantDeathAudit.death_cause_info'
        db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseInfo']))

        # Changing field 'InfantDeathAudit.death_medical_responsibility'
        db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathMedicalResponsibility']))
        # Adding field 'InfantFacialDefectItems.revision'
        db.add_column(u'mpepu_infant_infantfacialdefectitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFacialDefectItems.report_datetime'
        db.add_column(u'mpepu_infant_infantfacialdefectitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantBirthArv.revision'
        db.add_column(u'mpepu_infant_infantbirtharv', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthArv.report_datetime'
        db.add_column(u'mpepu_infant_infantbirtharv', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantBirthArv.infant_visit'
        db.alter_column(u'mpepu_infant_infantbirtharv', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantBirthArv', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantbirtharv', ['infant_visit_id'])

        # Adding field 'InfantRespiratoryDefectItems.revision'
        db.add_column(u'mpepu_infant_infantrespiratorydefectitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantRespiratoryDefectItems.report_datetime'
        db.add_column(u'mpepu_infant_infantrespiratorydefectitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOtherAbnormalityItems.revision'
        db.add_column(u'mpepu_infant_infantotherabnormalityitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantOtherAbnormalityItems.report_datetime'
        db.add_column(u'mpepu_infant_infantotherabnormalityitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantPreEligibility.revision'
        db.add_column(u'mpepu_infant_infantpreeligibility', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantPreEligibility.registered_subject'
        db.alter_column(u'mpepu_infant_infantpreeligibility', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantSurvivalAudit.revision'
        db.add_column(u'mpepu_infant_infantsurvival_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantSurvivalAudit.infant_visit'
        db.add_column(u'mpepu_infant_infantsurvival_audit', 'infant_visit',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='_audit_infantsurvival', to=orm['mpepu_infant.InfantVisit']),
                      keep_default=False)


        # Changing field 'InfantSurvivalAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantsurvival_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantCnsAbnormalityItems.revision'
        db.add_column(u'mpepu_infant_infantcnsabnormalityitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCnsAbnormalityItems.report_datetime'
        db.add_column(u'mpepu_infant_infantcnsabnormalityitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantHaartMod.revision'
        db.add_column(u'mpepu_infant_infanthaartmod', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCtxPlaceboAdhAudit.revision'
        db.add_column(u'mpepu_infant_infantctxplaceboadh_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCtxPlaceboAdhAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantctxplaceboadh_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantArvProphModAudit.revision'
        db.add_column(u'mpepu_infant_infantarvprophmod_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantArvProphModAudit.other_reason'
        db.add_column(u'mpepu_infant_infantarvprophmod_audit', 'other_reason',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCleftDisorderItems.revision'
        db.add_column(u'mpepu_infant_infantcleftdisorderitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCleftDisorderItems.report_datetime'
        db.add_column(u'mpepu_infant_infantcleftdisorderitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuDx2Proph.revision'
        db.add_column(u'mpepu_infant_infantfudx2proph', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx2Proph.report_datetime'
        db.add_column(u'mpepu_infant_infantfudx2proph', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantFuDx2Proph.infant_visit'
        db.alter_column(u'mpepu_infant_infantfudx2proph', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFuDx2Proph', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfudx2proph', ['infant_visit_id'])

        # Adding field 'InfantBirthData.revision'
        db.add_column(u'mpepu_infant_infantbirthdata', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthData.report_datetime'
        db.add_column(u'mpepu_infant_infantbirthdata', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantBirthData.infant_visit'
        db.alter_column(u'mpepu_infant_infantbirthdata', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantBirthData', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantbirthdata', ['infant_visit_id'])

        # Adding field 'InfantStudyDrugInitAudit.revision'
        db.add_column(u'mpepu_infant_infantstudydruginit_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugInitAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantstudydruginit_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantVisit.revision'
        db.add_column('mpepu_infant_infantvisit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantVisit.subject_identifier'
        db.add_column('mpepu_infant_infantvisit', 'subject_identifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'InfantVisit.appointment'
        db.alter_column('mpepu_infant_infantvisit', 'appointment_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appointment.Appointment'], unique=True))
        # Adding field 'InfantFuDx2ProphItems.revision'
        db.add_column(u'mpepu_infant_infantfudx2prophitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx2ProphItems.report_datetime'
        db.add_column(u'mpepu_infant_infantfudx2prophitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuNewMed.revision'
        db.add_column(u'mpepu_infant_infantfunewmed', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuNewMed.report_datetime'
        db.add_column(u'mpepu_infant_infantfunewmed', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantFuNewMed.infant_visit'
        db.alter_column(u'mpepu_infant_infantfunewmed', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFuNewMed', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfunewmed', ['infant_visit_id'])

        # Adding field 'InfantRenalAnomalyItems.revision'
        db.add_column(u'mpepu_infant_infantrenalanomalyitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantRenalAnomalyItems.report_datetime'
        db.add_column(u'mpepu_infant_infantrenalanomalyitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantBirthArvAudit.revision'
        db.add_column(u'mpepu_infant_infantbirtharv_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthArvAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantbirtharv_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuNewMedAudit.revision'
        db.add_column(u'mpepu_infant_infantfunewmed_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuNewMedAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfunewmed_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantBirthExam.revision'
        db.add_column(u'mpepu_infant_infantbirthexam', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthExam.report_datetime'
        db.add_column(u'mpepu_infant_infantbirthexam', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantBirthExam.infant_visit'
        db.alter_column(u'mpepu_infant_infantbirthexam', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantBirthExam', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantbirthexam', ['infant_visit_id'])

        # Adding field 'InfantTrisomiesChromosomeItems.revision'
        db.add_column(u'mpepu_infant_infanttrisomieschromosomeitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantTrisomiesChromosomeItems.report_datetime'
        db.add_column(u'mpepu_infant_infanttrisomieschromosomeitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantBirthFeedAudit.revision'
        db.add_column(u'mpepu_infant_infantbirthfeed_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthFeedAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantbirthfeed_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuDx2ProphAudit.revision'
        db.add_column(u'mpepu_infant_infantfudx2proph_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx2ProphAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfudx2proph_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantPreEligibilityAudit.revision'
        db.add_column(u'mpepu_infant_infantpreeligibility_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantPreEligibilityAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantpreeligibility_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantCtxPlaceboAdh.revision'
        db.add_column(u'mpepu_infant_infantctxplaceboadh', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantCtxPlaceboAdh.report_datetime'
        db.add_column(u'mpepu_infant_infantctxplaceboadh', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantCtxPlaceboAdh.infant_visit'
        db.alter_column(u'mpepu_infant_infantctxplaceboadh', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantCtxPlaceboAdh', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantctxplaceboadh', ['infant_visit_id'])

        # Adding field 'InfantFuPhysicalAudit.revision'
        db.add_column(u'mpepu_infant_infantfuphysical_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuPhysicalAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfuphysical_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuPhysicalAudit.head_circumference'
        db.add_column(u'mpepu_infant_infantfuphysical_audit', 'head_circumference',
                      self.gf('django.db.models.fields.DecimalField')(default=-1, max_digits=5, decimal_places=2),
                      keep_default=False)

        # Adding field 'InfantFuDxAudit.revision'
        db.add_column(u'mpepu_infant_infantfudx_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDxAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantfudx_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantFuDxItems.revision'
        db.add_column(u'mpepu_infant_infantfudxitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugItems.revision'
        db.add_column(u'mpepu_infant_infantstudydrugitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantStudyDrugItems.report_datetime'
        db.add_column(u'mpepu_infant_infantstudydrugitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantBirthDataAudit.revision'
        db.add_column(u'mpepu_infant_infantbirthdata_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantBirthDataAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantbirthdata_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantVerbalAutopsy.revision'
        db.add_column(u'mpepu_infant_infantverbalautopsy', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantVerbalAutopsy.infant_visit'
        db.add_column(u'mpepu_infant_infantverbalautopsy', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)


        # Changing field 'InfantVerbalAutopsy.registered_subject'
        db.alter_column(u'mpepu_infant_infantverbalautopsy', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantVerbalAutopsyItems.revision'
        db.add_column(u'mpepu_infant_infantverbalautopsyitems', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantVerbalAutopsyItems.report_datetime'
        db.add_column(u'mpepu_infant_infantverbalautopsyitems', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantEligibility.revision'
        db.add_column(u'mpepu_infant_infanteligibility', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantEligibility.registered_subject'
        db.alter_column(u'mpepu_infant_infanteligibility', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantPrerandoLoss.revision'
        db.add_column(u'mpepu_infant_infantprerandoloss', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantPrerandoLoss.infant_visit'
        db.add_column(u'mpepu_infant_infantprerandoloss', 'infant_visit',
                      self.gf('django.db.models.fields.related.OneToOneField')(null=True, blank=True, to=orm['mpepu_infant.InfantVisit'], unique=True),
                      keep_default=False)


        # Changing field 'InfantPrerandoLoss.registered_subject'
        db.alter_column(u'mpepu_infant_infantprerandoloss', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'InfantOffDrugAudit.revision'
        db.add_column(u'mpepu_infant_infantoffdrug_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantOffDrugAudit.report_datetime'
        db.add_column(u'mpepu_infant_infantoffdrug_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)

        # Adding field 'InfantOffDrugAudit.infant_visit'
        db.add_column(u'mpepu_infant_infantoffdrug_audit', 'infant_visit',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='_audit_infantoffdrug', to=orm['mpepu_infant.InfantVisit']),
                      keep_default=False)


        # Changing field 'InfantOffDrugAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantoffdrug_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantNvpAdherence.revision'
        db.add_column(u'mpepu_infant_infantnvpadherence', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantNvpAdherence.report_datetime'
        db.add_column(u'mpepu_infant_infantnvpadherence', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantNvpAdherence.infant_visit'
        db.alter_column(u'mpepu_infant_infantnvpadherence', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantNvpAdherence', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantnvpadherence', ['infant_visit_id'])

        # Adding field 'InfantVisitAudit.revision'
        db.add_column('mpepu_infant_infantvisit_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantVisitAudit.subject_identifier'
        db.add_column('mpepu_infant_infantvisit_audit', 'subject_identifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'InfantVisitAudit.appointment'
        db.alter_column('mpepu_infant_infantvisit_audit', 'appointment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appointment.Appointment']))
        # Adding field 'InfantPrerandoLossAudit.revision'
        db.add_column(u'mpepu_infant_infantprerandoloss_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantPrerandoLossAudit.infant_visit'
        db.add_column(u'mpepu_infant_infantprerandoloss_audit', 'infant_visit',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='_audit_infantprerandoloss', to=orm['mpepu_infant.InfantVisit']),
                      keep_default=False)


        # Changing field 'InfantPrerandoLossAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantprerandoloss_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantVerbalAutopsyAudit.revision'
        db.add_column(u'mpepu_infant_infantverbalautopsy_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantVerbalAutopsyAudit.infant_visit'
        db.add_column(u'mpepu_infant_infantverbalautopsy_audit', 'infant_visit',
                      self.gf('django.db.models.fields.related.ForeignKey')(null=True, blank=True, related_name='_audit_infantverbalautopsy', to=orm['mpepu_infant.InfantVisit']),
                      keep_default=False)


        # Changing field 'InfantVerbalAutopsyAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantverbalautopsy_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'InfantArvProphMod.revision'
        db.add_column(u'mpepu_infant_infantarvprophmod', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantArvProphMod.other_reason'
        db.add_column(u'mpepu_infant_infantarvprophmod', 'other_reason',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx.revision'
        db.add_column(u'mpepu_infant_infantfudx', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'InfantFuDx.report_datetime'
        db.add_column(u'mpepu_infant_infantfudx', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 5, 5, 0, 0)),
                      keep_default=False)


        # Changing field 'InfantFuDx.infant_visit'
        db.alter_column(u'mpepu_infant_infantfudx', 'infant_visit_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['mpepu_infant.InfantVisit'], unique=True))
        # Adding unique constraint on 'InfantFuDx', fields ['infant_visit']
#         db.create_unique(u'mpepu_infant_infantfudx', ['infant_visit_id'])

        # Adding field 'InfantBirthAudit.revision'
        db.add_column(u'mpepu_infant_infantbirth_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'InfantBirthAudit.registered_subject'
        db.alter_column(u'mpepu_infant_infantbirth_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))

    def backwards(self, orm):
        pass
        # Removing unique constraint on 'InfantFuDx', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfudx', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantNvpAdherence', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantnvpadherence', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantCtxPlaceboAdh', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantctxplaceboadh', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantBirthExam', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantbirthexam', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFuNewMed', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfunewmed', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantBirthData', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantbirthdata', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFuDx2Proph', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfudx2proph', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantBirthArv', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantbirtharv', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFeeding', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfeeding', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantStudyDrug', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantstudydrug', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantBirthFeed', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantbirthfeed', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantHivStatus', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infanthivstatus', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantStudyDrugInit', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantstudydruginit', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantArvProph', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantarvproph', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFu', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfu', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFuD', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfud', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFuPhysical', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfuphysical', ['infant_visit_id'])
# 
#         # Removing unique constraint on 'InfantFuMed', fields ['infant_visit']
#         db.delete_unique(u'mpepu_infant_infantfumed', ['infant_visit_id'])
# 
#         # Adding model 'InfantVitalStatusAudit'
#         db.create_table('mpepu_infant_infantvitalstatus_audit', (
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True)),
#             ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantvitalstatus', null=True, to=orm['mpepu_infant.InfantVisit'])),
#             ('_audit_change_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True)),
#             ('registered_subject', self.gf('django.db.models.fields.related.ForeignKey')(related_name='_audit_infantvitalstatus', to=orm['bhp_registration.RegisteredSubject'])),
#             ('_audit_id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('_audit_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True, db_index=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, blank=True)),
#             ('_audit_subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#         ))
#         db.send_create_signal('mpepu_infant', ['InfantVitalStatusAudit'])
# 
#         # Adding model 'InfantVitalStatus'
#         db.create_table(u'mpepu_infant_infantvitalstatus', (
#             ('hostname_created', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True)),
#             ('infant_visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit'], null=True)),
#             ('hostname_modified', self.gf('django.db.models.fields.CharField')(default='mac.local', max_length=50, blank=True, db_index=True)),
#             ('registered_subject', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True)),
#             ('user_created', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('report_datetime', self.gf('django.db.models.fields.DateTimeField')(null=True)),
#             ('id', self.gf('django.db.models.fields.CharField')(max_length=36, primary_key=True)),
#             ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#             ('user_modified', self.gf('django.db.models.fields.CharField')(default='', max_length=250, db_index=True)),
#             ('modified', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
#         ))
#         db.send_create_signal('mpepu_infant', ['InfantVitalStatus'])
# 
#         # Deleting model 'InfantStoolCollection'
#         db.delete_table(u'mpepu_infant_infantstoolcollection')
# 
#         # Deleting model 'InfantStoolCollectionAudit'
#         db.delete_table(u'mpepu_infant_infantstoolcollection_audit')
# 
#         # Deleting field 'InfantMouthUpGastrointestinalItems.revision'
#         db.delete_column(u'mpepu_infant_infantmouthupgastrointestinalitems', 'revision')
# 
#         # Deleting field 'InfantMouthUpGastrointestinalItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantmouthupgastrointestinalitems', 'report_datetime')
# 
#         # Deleting field 'InfantFuMed.revision'
#         db.delete_column(u'mpepu_infant_infantfumed', 'revision')
# 
#         # Deleting field 'InfantFuMed.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfumed', 'report_datetime')
# 
# 
#         # Changing field 'InfantFuMed.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfumed', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantHaartAudit.revision'
#         db.delete_column(u'mpepu_infant_infanthaart_audit', 'revision')
# 
# 
#         # Changing field 'InfantHaartAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infanthaart_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantFuMedAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfumed_audit', 'revision')
# 
#         # Deleting field 'InfantFuMedAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfumed_audit', 'report_datetime')
# 
#         # Deleting field 'InfantOffStudyAudit.revision'
#         db.delete_column(u'mpepu_infant_infantoffstudy_audit', 'revision')
# 
#         # Deleting field 'InfantOffStudyAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantoffstudy_audit', 'report_datetime')
# 
#         # Deleting field 'InfantOffStudyAudit.infant_visit'
#         db.delete_column(u'mpepu_infant_infantoffstudy_audit', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantOffStudyAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantoffstudy_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantBirth.revision'
#         db.delete_column(u'mpepu_infant_infantbirth', 'revision')
# 
# 
#         # Changing field 'InfantBirth.registered_subject'
#         db.alter_column(u'mpepu_infant_infantbirth', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantSkinAbnormalItems.revision'
#         db.delete_column(u'mpepu_infant_infantskinabnormalitems', 'revision')
# 
#         # Deleting field 'InfantSkinAbnormalItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantskinabnormalitems', 'report_datetime')
# 
#         # Deleting field 'InfantOffStudy.revision'
#         db.delete_column(u'mpepu_infant_infantoffstudy', 'revision')
# 
#         # Deleting field 'InfantOffStudy.infant_visit'
#         db.delete_column(u'mpepu_infant_infantoffstudy', 'infant_visit_id')
# 
#         # Deleting field 'InfantOffStudy.report_datetime'
#         db.delete_column(u'mpepu_infant_infantoffstudy', 'report_datetime')
# 
# 
#         # Changing field 'InfantOffStudy.registered_subject'
#         db.alter_column(u'mpepu_infant_infantoffstudy', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantRandoDeferralAudit.revision'
#         db.delete_column(u'mpepu_infant_infantrandodeferral_audit', 'revision')
# 
# 
#         # Changing field 'InfantRandoDeferralAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantrandodeferral_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantFuPhysical.revision'
#         db.delete_column(u'mpepu_infant_infantfuphysical', 'revision')
# 
#         # Deleting field 'InfantFuPhysical.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfuphysical', 'report_datetime')
# 
#         # Deleting field 'InfantFuPhysical.head_circumference'
#         db.delete_column(u'mpepu_infant_infantfuphysical', 'head_circumference')
# 
# 
#         # Changing field 'InfantFuPhysical.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfuphysical', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantFemaleGenitalAnomalyItems.revision'
#         db.delete_column(u'mpepu_infant_infantfemalegenitalanomalyitems', 'revision')
# 
#         # Deleting field 'InfantFemaleGenitalAnomalyItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfemalegenitalanomalyitems', 'report_datetime')
# 
#         # Deleting field 'InfantFuDAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfud_audit', 'revision')
# 
#         # Deleting field 'InfantFuDAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfud_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuDAudit.d_onset_date'
#         db.delete_column(u'mpepu_infant_infantfud_audit', 'd_onset_date')
# 
#         # Deleting field 'InfantFuD.revision'
#         db.delete_column(u'mpepu_infant_infantfud', 'revision')
# 
#         # Deleting field 'InfantFuD.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfud', 'report_datetime')
# 
#         # Deleting field 'InfantFuD.d_onset_date'
#         db.delete_column(u'mpepu_infant_infantfud', 'd_onset_date')
# 
# 
#         # Changing field 'InfantFuD.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfud', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantFu.revision'
#         db.delete_column(u'mpepu_infant_infantfu', 'revision')
# 
#         # Deleting field 'InfantFu.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfu', 'report_datetime')
# 
# 
#         # Changing field 'InfantFu.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfu', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantFuDxItemsAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfudxitems_audit', 'revision')
# 
#         # Deleting field 'InfantStudyDrugItemsAudit.revision'
#         db.delete_column(u'mpepu_infant_infantstudydrugitems_audit', 'revision')
# 
#         # Deleting field 'InfantStudyDrugItemsAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantstudydrugitems_audit', 'report_datetime')
# 
#         # Deleting field 'InfantCongenitalAnomalies.revision'
#         db.delete_column(u'mpepu_infant_infantcongenitalanomalies', 'revision')
# 
#         # Deleting field 'InfantCongenitalAnomalies.infant_visit'
#         db.delete_column(u'mpepu_infant_infantcongenitalanomalies', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantCongenitalAnomalies.registered_subject'
#         db.alter_column(u'mpepu_infant_infantcongenitalanomalies', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantCardiovascularDisorderItems.revision'
#         db.delete_column(u'mpepu_infant_infantcardiovasculardisorderitems', 'revision')
# 
#         # Deleting field 'InfantCardiovascularDisorderItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantcardiovasculardisorderitems', 'report_datetime')
# 
#         # Deleting field 'InfantArvProph.revision'
#         db.delete_column(u'mpepu_infant_infantarvproph', 'revision')
# 
#         # Deleting field 'InfantArvProph.report_datetime'
#         db.delete_column(u'mpepu_infant_infantarvproph', 'report_datetime')
# 
# 
#         # Changing field 'InfantArvProph.infant_visit'
#         db.alter_column(u'mpepu_infant_infantarvproph', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantStudyDrugAudit.revision'
#         db.delete_column(u'mpepu_infant_infantstudydrug_audit', 'revision')
# 
#         # Deleting field 'InfantStudyDrugAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantstudydrug_audit', 'report_datetime')
# 
#         # Deleting field 'InfantHivStatusAudit.revision'
#         db.delete_column(u'mpepu_infant_infanthivstatus_audit', 'revision')
# 
#         # Deleting field 'InfantHivStatusAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infanthivstatus_audit', 'report_datetime')
# 
#         # Deleting field 'InfantArvProphAudit.revision'
#         db.delete_column(u'mpepu_infant_infantarvproph_audit', 'revision')
# 
#         # Deleting field 'InfantArvProphAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantarvproph_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuNewMedItems.revision'
#         db.delete_column(u'mpepu_infant_infantfunewmeditems', 'revision')
# 
#         # Deleting field 'InfantFuNewMedItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfunewmeditems', 'report_datetime')
# 
#         # Deleting field 'InfantHaart.revision'
#         db.delete_column(u'mpepu_infant_infanthaart', 'revision')
# 
# 
#         # Changing field 'InfantHaart.registered_subject'
#         db.alter_column(u'mpepu_infant_infanthaart', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantLowerGastrointestinalItems.revision'
#         db.delete_column(u'mpepu_infant_infantlowergastrointestinalitems', 'revision')
# 
#         # Deleting field 'InfantLowerGastrointestinalItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantlowergastrointestinalitems', 'report_datetime')
# 
#         # Deleting field 'InfantMaleGenitalAnomalyItems.revision'
#         db.delete_column(u'mpepu_infant_infantmalegenitalanomalyitems', 'revision')
# 
#         # Deleting field 'InfantMaleGenitalAnomalyItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantmalegenitalanomalyitems', 'report_datetime')
# 
#         # Deleting field 'InfantStudyDrugInit.revision'
#         db.delete_column(u'mpepu_infant_infantstudydruginit', 'revision')
# 
#         # Deleting field 'InfantStudyDrugInit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantstudydruginit', 'report_datetime')
# 
# 
#         # Changing field 'InfantStudyDrugInit.infant_visit'
#         db.alter_column(u'mpepu_infant_infantstudydruginit', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantHaartModAudit.revision'
#         db.delete_column(u'mpepu_infant_infanthaartmod_audit', 'revision')
# 
#         # Deleting field 'InfantFuDx2ProphItemsAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfudx2prophitems_audit', 'revision')
# 
#         # Deleting field 'InfantFuDx2ProphItemsAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfudx2prophitems_audit', 'report_datetime')
# 
#         # Deleting field 'InfantNvpAdherenceAudit.revision'
#         db.delete_column(u'mpepu_infant_infantnvpadherence_audit', 'revision')
# 
#         # Deleting field 'InfantNvpAdherenceAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantnvpadherence_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuNewMedItemsAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfunewmeditems_audit', 'revision')
# 
#         # Deleting field 'InfantFuNewMedItemsAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfunewmeditems_audit', 'report_datetime')
# 
#         # Deleting field 'InfantMusculoskeletalAbnormalItems.revision'
#         db.delete_column(u'mpepu_infant_infantmusculoskeletalabnormalitems', 'revision')
# 
#         # Deleting field 'InfantMusculoskeletalAbnormalItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantmusculoskeletalabnormalitems', 'report_datetime')
# 
#         # Deleting field 'InfantHivStatus.revision'
#         db.delete_column(u'mpepu_infant_infanthivstatus', 'revision')
# 
#         # Deleting field 'InfantHivStatus.report_datetime'
#         db.delete_column(u'mpepu_infant_infanthivstatus', 'report_datetime')
# 
# 
#         # Changing field 'InfantHivStatus.infant_visit'
#         db.alter_column(u'mpepu_infant_infanthivstatus', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantDeath.revision'
#         db.delete_column(u'mpepu_infant_infantdeath', 'revision')
# 
#         # Deleting field 'InfantDeath.infant_visit'
#         db.delete_column(u'mpepu_infant_infantdeath', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantDeath.dx_code'
#         db.alter_column(u'mpepu_infant_infantdeath', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_code_lists.DxCode'], max_length=25))
# 
#         # Changing field 'InfantDeath.death_cause_category'
#         db.alter_column(u'mpepu_infant_infantdeath', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseCategory']))
# 
#         # Changing field 'InfantDeath.registered_subject'
#         db.alter_column(u'mpepu_infant_infantdeath', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
# 
#         # Changing field 'InfantDeath.death_reason_hospitalized'
#         db.alter_column(u'mpepu_infant_infantdeath', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathReasonHospitalized'], null=True))
# 
#         # Changing field 'InfantDeath.death_cause_info'
#         db.alter_column(u'mpepu_infant_infantdeath', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseInfo']))
# 
#         # Changing field 'InfantDeath.death_medical_responsibility'
#         db.alter_column(u'mpepu_infant_infantdeath', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathMedicalResponsibility']))
#         # Deleting field 'InfantSurvival.revision'
#         db.delete_column(u'mpepu_infant_infantsurvival', 'revision')
# 
#         # Deleting field 'InfantSurvival.infant_visit'
#         db.delete_column(u'mpepu_infant_infantsurvival', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantSurvival.registered_subject'
#         db.alter_column(u'mpepu_infant_infantsurvival', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantFuAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfu_audit', 'revision')
# 
#         # Deleting field 'InfantFuAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfu_audit', 'report_datetime')
# 
#         # Deleting field 'InfantBirthFeed.revision'
#         db.delete_column(u'mpepu_infant_infantbirthfeed', 'revision')
# 
#         # Deleting field 'InfantBirthFeed.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirthfeed', 'report_datetime')
# 
# 
#         # Changing field 'InfantBirthFeed.infant_visit'
#         db.alter_column(u'mpepu_infant_infantbirthfeed', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantEligibilityAudit.revision'
#         db.delete_column(u'mpepu_infant_infanteligibility_audit', 'revision')
# 
# 
#         # Changing field 'InfantEligibilityAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infanteligibility_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantStudyDrug.revision'
#         db.delete_column(u'mpepu_infant_infantstudydrug', 'revision')
# 
#         # Deleting field 'InfantStudyDrug.report_datetime'
#         db.delete_column(u'mpepu_infant_infantstudydrug', 'report_datetime')
# 
# 
#         # Changing field 'InfantStudyDrug.infant_visit'
#         db.alter_column(u'mpepu_infant_infantstudydrug', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantRandoDeferral.revision'
#         db.delete_column(u'mpepu_infant_infantrandodeferral', 'revision')
# 
# 
#         # Changing field 'InfantRandoDeferral.registered_subject'
#         db.alter_column(u'mpepu_infant_infantrandodeferral', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantBirthExamAudit.revision'
#         db.delete_column(u'mpepu_infant_infantbirthexam_audit', 'revision')
# 
#         # Deleting field 'InfantBirthExamAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirthexam_audit', 'report_datetime')
# 
#         # Deleting field 'InfantOffDrug.revision'
#         db.delete_column(u'mpepu_infant_infantoffdrug', 'revision')
# 
#         # Deleting field 'InfantOffDrug.report_datetime'
#         db.delete_column(u'mpepu_infant_infantoffdrug', 'report_datetime')
# 
#         # Deleting field 'InfantOffDrug.infant_visit'
#         db.delete_column(u'mpepu_infant_infantoffdrug', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantOffDrug.registered_subject'
#         db.alter_column(u'mpepu_infant_infantoffdrug', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantFeeding.revision'
#         db.delete_column(u'mpepu_infant_infantfeeding', 'revision')
# 
#         # Deleting field 'InfantFeeding.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfeeding', 'report_datetime')
# 
# 
#         # Changing field 'InfantFeeding.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfeeding', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantFeedingAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfeeding_audit', 'revision')
# 
#         # Deleting field 'InfantFeedingAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfeeding_audit', 'report_datetime')
# 
#         # Deleting field 'InfantDeathAudit.revision'
#         db.delete_column(u'mpepu_infant_infantdeath_audit', 'revision')
# 
#         # Deleting field 'InfantDeathAudit.infant_visit'
#         db.delete_column(u'mpepu_infant_infantdeath_audit', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantDeathAudit.dx_code'
#         db.alter_column(u'mpepu_infant_infantdeath_audit', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(max_length=25, to=orm['bhp_code_lists.DxCode']))
# 
#         # Changing field 'InfantDeathAudit.death_cause_category'
#         db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseCategory']))
# 
#         # Changing field 'InfantDeathAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantdeath_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
# 
#         # Changing field 'InfantDeathAudit.death_reason_hospitalized'
#         db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bhp_adverse.DeathReasonHospitalized']))
# 
#         # Changing field 'InfantDeathAudit.death_cause_info'
#         db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseInfo']))
# 
#         # Changing field 'InfantDeathAudit.death_medical_responsibility'
#         db.alter_column(u'mpepu_infant_infantdeath_audit', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathMedicalResponsibility']))
#         # Deleting field 'InfantFacialDefectItems.revision'
#         db.delete_column(u'mpepu_infant_infantfacialdefectitems', 'revision')
# 
#         # Deleting field 'InfantFacialDefectItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfacialdefectitems', 'report_datetime')
# 
#         # Deleting field 'InfantBirthArv.revision'
#         db.delete_column(u'mpepu_infant_infantbirtharv', 'revision')
# 
#         # Deleting field 'InfantBirthArv.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirtharv', 'report_datetime')
# 
# 
#         # Changing field 'InfantBirthArv.infant_visit'
#         db.alter_column(u'mpepu_infant_infantbirtharv', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantRespiratoryDefectItems.revision'
#         db.delete_column(u'mpepu_infant_infantrespiratorydefectitems', 'revision')
# 
#         # Deleting field 'InfantRespiratoryDefectItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantrespiratorydefectitems', 'report_datetime')
# 
#         # Deleting field 'InfantOtherAbnormalityItems.revision'
#         db.delete_column(u'mpepu_infant_infantotherabnormalityitems', 'revision')
# 
#         # Deleting field 'InfantOtherAbnormalityItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantotherabnormalityitems', 'report_datetime')
# 
#         # Deleting field 'InfantPreEligibility.revision'
#         db.delete_column(u'mpepu_infant_infantpreeligibility', 'revision')
# 
# 
#         # Changing field 'InfantPreEligibility.registered_subject'
#         db.alter_column(u'mpepu_infant_infantpreeligibility', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantSurvivalAudit.revision'
#         db.delete_column(u'mpepu_infant_infantsurvival_audit', 'revision')
# 
#         # Deleting field 'InfantSurvivalAudit.infant_visit'
#         db.delete_column(u'mpepu_infant_infantsurvival_audit', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantSurvivalAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantsurvival_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantCnsAbnormalityItems.revision'
#         db.delete_column(u'mpepu_infant_infantcnsabnormalityitems', 'revision')
# 
#         # Deleting field 'InfantCnsAbnormalityItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantcnsabnormalityitems', 'report_datetime')
# 
#         # Deleting field 'InfantHaartMod.revision'
#         db.delete_column(u'mpepu_infant_infanthaartmod', 'revision')
# 
#         # Deleting field 'InfantCtxPlaceboAdhAudit.revision'
#         db.delete_column(u'mpepu_infant_infantctxplaceboadh_audit', 'revision')
# 
#         # Deleting field 'InfantCtxPlaceboAdhAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantctxplaceboadh_audit', 'report_datetime')
# 
#         # Deleting field 'InfantArvProphModAudit.revision'
#         db.delete_column(u'mpepu_infant_infantarvprophmod_audit', 'revision')
# 
#         # Deleting field 'InfantArvProphModAudit.other_reason'
#         db.delete_column(u'mpepu_infant_infantarvprophmod_audit', 'other_reason')
# 
#         # Deleting field 'InfantCleftDisorderItems.revision'
#         db.delete_column(u'mpepu_infant_infantcleftdisorderitems', 'revision')
# 
#         # Deleting field 'InfantCleftDisorderItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantcleftdisorderitems', 'report_datetime')
# 
#         # Deleting field 'InfantFuDx2Proph.revision'
#         db.delete_column(u'mpepu_infant_infantfudx2proph', 'revision')
# 
#         # Deleting field 'InfantFuDx2Proph.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfudx2proph', 'report_datetime')
# 
# 
#         # Changing field 'InfantFuDx2Proph.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfudx2proph', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantBirthData.revision'
#         db.delete_column(u'mpepu_infant_infantbirthdata', 'revision')
# 
#         # Deleting field 'InfantBirthData.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirthdata', 'report_datetime')
# 
# 
#         # Changing field 'InfantBirthData.infant_visit'
#         db.alter_column(u'mpepu_infant_infantbirthdata', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantStudyDrugInitAudit.revision'
#         db.delete_column(u'mpepu_infant_infantstudydruginit_audit', 'revision')
# 
#         # Deleting field 'InfantStudyDrugInitAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantstudydruginit_audit', 'report_datetime')
# 
#         # Deleting field 'InfantVisit.revision'
#         db.delete_column('mpepu_infant_infantvisit', 'revision')
# 
#         # Deleting field 'InfantVisit.subject_identifier'
#         db.delete_column('mpepu_infant_infantvisit', 'subject_identifier')
# 
# 
#         # Changing field 'InfantVisit.appointment'
#         db.alter_column('mpepu_infant_infantvisit', 'appointment_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_appointment.Appointment'], unique=True))
#         # Deleting field 'InfantFuDx2ProphItems.revision'
#         db.delete_column(u'mpepu_infant_infantfudx2prophitems', 'revision')
# 
#         # Deleting field 'InfantFuDx2ProphItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfudx2prophitems', 'report_datetime')
# 
#         # Deleting field 'InfantFuNewMed.revision'
#         db.delete_column(u'mpepu_infant_infantfunewmed', 'revision')
# 
#         # Deleting field 'InfantFuNewMed.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfunewmed', 'report_datetime')
# 
# 
#         # Changing field 'InfantFuNewMed.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfunewmed', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantRenalAnomalyItems.revision'
#         db.delete_column(u'mpepu_infant_infantrenalanomalyitems', 'revision')
# 
#         # Deleting field 'InfantRenalAnomalyItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantrenalanomalyitems', 'report_datetime')
# 
#         # Deleting field 'InfantBirthArvAudit.revision'
#         db.delete_column(u'mpepu_infant_infantbirtharv_audit', 'revision')
# 
#         # Deleting field 'InfantBirthArvAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirtharv_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuNewMedAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfunewmed_audit', 'revision')
# 
#         # Deleting field 'InfantFuNewMedAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfunewmed_audit', 'report_datetime')
# 
#         # Deleting field 'InfantBirthExam.revision'
#         db.delete_column(u'mpepu_infant_infantbirthexam', 'revision')
# 
#         # Deleting field 'InfantBirthExam.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirthexam', 'report_datetime')
# 
# 
#         # Changing field 'InfantBirthExam.infant_visit'
#         db.alter_column(u'mpepu_infant_infantbirthexam', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantTrisomiesChromosomeItems.revision'
#         db.delete_column(u'mpepu_infant_infanttrisomieschromosomeitems', 'revision')
# 
#         # Deleting field 'InfantTrisomiesChromosomeItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infanttrisomieschromosomeitems', 'report_datetime')
# 
#         # Deleting field 'InfantBirthFeedAudit.revision'
#         db.delete_column(u'mpepu_infant_infantbirthfeed_audit', 'revision')
# 
#         # Deleting field 'InfantBirthFeedAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirthfeed_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuDx2ProphAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfudx2proph_audit', 'revision')
# 
#         # Deleting field 'InfantFuDx2ProphAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfudx2proph_audit', 'report_datetime')
# 
#         # Deleting field 'InfantPreEligibilityAudit.revision'
#         db.delete_column(u'mpepu_infant_infantpreeligibility_audit', 'revision')
# 
# 
#         # Changing field 'InfantPreEligibilityAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantpreeligibility_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantCtxPlaceboAdh.revision'
#         db.delete_column(u'mpepu_infant_infantctxplaceboadh', 'revision')
# 
#         # Deleting field 'InfantCtxPlaceboAdh.report_datetime'
#         db.delete_column(u'mpepu_infant_infantctxplaceboadh', 'report_datetime')
# 
# 
#         # Changing field 'InfantCtxPlaceboAdh.infant_visit'
#         db.alter_column(u'mpepu_infant_infantctxplaceboadh', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantFuPhysicalAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfuphysical_audit', 'revision')
# 
#         # Deleting field 'InfantFuPhysicalAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfuphysical_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuPhysicalAudit.head_circumference'
#         db.delete_column(u'mpepu_infant_infantfuphysical_audit', 'head_circumference')
# 
#         # Deleting field 'InfantFuDxAudit.revision'
#         db.delete_column(u'mpepu_infant_infantfudx_audit', 'revision')
# 
#         # Deleting field 'InfantFuDxAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfudx_audit', 'report_datetime')
# 
#         # Deleting field 'InfantFuDxItems.revision'
#         db.delete_column(u'mpepu_infant_infantfudxitems', 'revision')
# 
#         # Deleting field 'InfantStudyDrugItems.revision'
#         db.delete_column(u'mpepu_infant_infantstudydrugitems', 'revision')
# 
#         # Deleting field 'InfantStudyDrugItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantstudydrugitems', 'report_datetime')
# 
#         # Deleting field 'InfantBirthDataAudit.revision'
#         db.delete_column(u'mpepu_infant_infantbirthdata_audit', 'revision')
# 
#         # Deleting field 'InfantBirthDataAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantbirthdata_audit', 'report_datetime')
# 
#         # Deleting field 'InfantVerbalAutopsy.revision'
#         db.delete_column(u'mpepu_infant_infantverbalautopsy', 'revision')
# 
#         # Deleting field 'InfantVerbalAutopsy.infant_visit'
#         db.delete_column(u'mpepu_infant_infantverbalautopsy', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantVerbalAutopsy.registered_subject'
#         db.alter_column(u'mpepu_infant_infantverbalautopsy', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantVerbalAutopsyItems.revision'
#         db.delete_column(u'mpepu_infant_infantverbalautopsyitems', 'revision')
# 
#         # Deleting field 'InfantVerbalAutopsyItems.report_datetime'
#         db.delete_column(u'mpepu_infant_infantverbalautopsyitems', 'report_datetime')
# 
#         # Deleting field 'InfantEligibility.revision'
#         db.delete_column(u'mpepu_infant_infanteligibility', 'revision')
# 
# 
#         # Changing field 'InfantEligibility.registered_subject'
#         db.alter_column(u'mpepu_infant_infanteligibility', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantPrerandoLoss.revision'
#         db.delete_column(u'mpepu_infant_infantprerandoloss', 'revision')
# 
#         # Deleting field 'InfantPrerandoLoss.infant_visit'
#         db.delete_column(u'mpepu_infant_infantprerandoloss', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantPrerandoLoss.registered_subject'
#         db.alter_column(u'mpepu_infant_infantprerandoloss', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
#         # Deleting field 'InfantOffDrugAudit.revision'
#         db.delete_column(u'mpepu_infant_infantoffdrug_audit', 'revision')
# 
#         # Deleting field 'InfantOffDrugAudit.report_datetime'
#         db.delete_column(u'mpepu_infant_infantoffdrug_audit', 'report_datetime')
# 
#         # Deleting field 'InfantOffDrugAudit.infant_visit'
#         db.delete_column(u'mpepu_infant_infantoffdrug_audit', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantOffDrugAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantoffdrug_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantNvpAdherence.revision'
#         db.delete_column(u'mpepu_infant_infantnvpadherence', 'revision')
# 
#         # Deleting field 'InfantNvpAdherence.report_datetime'
#         db.delete_column(u'mpepu_infant_infantnvpadherence', 'report_datetime')
# 
# 
#         # Changing field 'InfantNvpAdherence.infant_visit'
#         db.alter_column(u'mpepu_infant_infantnvpadherence', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantVisitAudit.revision'
#         db.delete_column('mpepu_infant_infantvisit_audit', 'revision')
# 
#         # Deleting field 'InfantVisitAudit.subject_identifier'
#         db.delete_column('mpepu_infant_infantvisit_audit', 'subject_identifier')
# 
# 
#         # Changing field 'InfantVisitAudit.appointment'
#         db.alter_column('mpepu_infant_infantvisit_audit', 'appointment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_appointment.Appointment']))
#         # Deleting field 'InfantPrerandoLossAudit.revision'
#         db.delete_column(u'mpepu_infant_infantprerandoloss_audit', 'revision')
# 
#         # Deleting field 'InfantPrerandoLossAudit.infant_visit'
#         db.delete_column(u'mpepu_infant_infantprerandoloss_audit', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantPrerandoLossAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantprerandoloss_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantVerbalAutopsyAudit.revision'
#         db.delete_column(u'mpepu_infant_infantverbalautopsy_audit', 'revision')
# 
#         # Deleting field 'InfantVerbalAutopsyAudit.infant_visit'
#         db.delete_column(u'mpepu_infant_infantverbalautopsy_audit', 'infant_visit_id')
# 
# 
#         # Changing field 'InfantVerbalAutopsyAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantverbalautopsy_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
#         # Deleting field 'InfantArvProphMod.revision'
#         db.delete_column(u'mpepu_infant_infantarvprophmod', 'revision')
# 
#         # Deleting field 'InfantArvProphMod.other_reason'
#         db.delete_column(u'mpepu_infant_infantarvprophmod', 'other_reason')
# 
#         # Deleting field 'InfantFuDx.revision'
#         db.delete_column(u'mpepu_infant_infantfudx', 'revision')
# 
#         # Deleting field 'InfantFuDx.report_datetime'
#         db.delete_column(u'mpepu_infant_infantfudx', 'report_datetime')
# 
# 
#         # Changing field 'InfantFuDx.infant_visit'
#         db.alter_column(u'mpepu_infant_infantfudx', 'infant_visit_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mpepu_infant.InfantVisit']))
#         # Deleting field 'InfantBirthAudit.revision'
#         db.delete_column(u'mpepu_infant_infantbirth_audit', 'revision')
# 
# 
#         # Changing field 'InfantBirthAudit.registered_subject'
#         db.alter_column(u'mpepu_infant_infantbirth_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))

    models = {
        'adverse_event.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory', 'db_table': "'bhp_adverse_deathcausecategory'"},
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
        'adverse_event.deathcauseinfo': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseInfo', 'db_table': "'bhp_adverse_deathcauseinfo'"},
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
        'adverse_event.deathmedicalresponsibility': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathMedicalResponsibility', 'db_table': "'bhp_adverse_deathmedicalresponsibility'"},
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
        'adverse_event.deathreasonhospitalized': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathReasonHospitalized', 'db_table': "'bhp_adverse_deathreasonhospitalized'"},
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
        'appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'unique_together': "(('registered_subject', 'visit_definition', 'visit_instance'),)", 'object_name': 'Appointment', 'db_table': "'bhp_appointment_appointment'"},
            'appt_close_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'appt_datetime': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'appt_reason': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'appt_status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '25', 'db_index': 'True'}),
            'appt_type': ('django.db.models.fields.CharField', [], {'default': "'clinic'", 'max_length': '20'}),
            'best_appt_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dashboard_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'timepoint_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['visit_schedule.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'bhp_content_type_map.contenttypemap': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap'},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
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
        'code_lists.wcsdxped': {
            'Meta': {'object_name': 'WcsDxPed', 'db_table': "'bhp_code_lists_wcsdxped'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mpepu_infant.infantarvproph': {
            'Meta': {'object_name': 'InfantArvProph'},
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prophylatic_nvp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantarvprophaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantArvProphAudit', 'db_table': "u'mpepu_infant_infantarvproph_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantarvproph'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prophylatic_nvp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantarvprophmod': {
            'Meta': {'object_name': 'InfantArvProphMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantArvProph']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_reason': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantarvprophmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantArvProphModAudit', 'db_table': "u'mpepu_infant_infantarvprophmod_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantarvprophmod'", 'to': "orm['mpepu_infant.InfantArvProph']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_reason': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirth': {
            'Meta': {'unique_together': "(['initials', 'maternal_lab_del'],)", 'object_name': 'InfantBirth'},
            'birth_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirtharv': {
            'Meta': {'object_name': 'InfantBirthArv'},
            'additional_nvp_doses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_additional_dose': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nvp_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sdnvp_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirtharvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthArvAudit', 'db_table': "u'mpepu_infant_infantbirtharv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'additional_nvp_doses': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_additional_dose': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'azt_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_arv_comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirtharv'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirtharv'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nvp_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sdnvp_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthAudit', 'db_table': "u'mpepu_infant_infantbirth_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'birth_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirth'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirth'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_birth_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'infant_length': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_birth_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthdataaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthDataAudit', 'db_table': "u'mpepu_infant_infantbirthdata_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'apgar_score': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'apgar_score_min_1': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'apgar_score_min_10': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'apgar_score_min_5': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalities': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'head_circumference': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthdata'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_birth_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'infant_length': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthdata'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_birth_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_exam_date': ('django.db.models.fields.DateField', [], {}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'macular_papular_rash': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'neuro_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neurologic_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'other_exam_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'physical_exam_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'resp_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'resp_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'skin_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'skin_exam_other': ('django.db.models.fields.TextField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthexamaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthExamAudit', 'db_table': "u'mpepu_infant_infantbirthexam_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthexam'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_exam_date': ('django.db.models.fields.DateField', [], {}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthexam'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'macular_papular_rash': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'neuro_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'neurologic_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'other_exam_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'physical_exam_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'resp_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'resp_exam_other': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'skin_exam': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '15'}),
            'skin_exam_other': ('django.db.models.fields.TextField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthfeed': {
            'Meta': {'object_name': 'InfantBirthFeed'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_after_delivery': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vaccination': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.InfantVaccines']", 'symmetrical': 'False'})
        },
        'mpepu_infant.infantbirthfeedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthFeedAudit', 'db_table': "u'mpepu_infant_infantbirthfeed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_after_delivery': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthfeed'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthfeed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantcardiovasculardisorderitems': {
            'Meta': {'object_name': 'InfantCardiovascularDisorderItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cardiovascular_disorder': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'cardiovascular_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantcleftdisorderitems': {
            'Meta': {'object_name': 'InfantCleftDisorderItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cleft_disorder': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'cleft_disorders_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantcnsabnormalityitems': {
            'Meta': {'object_name': 'InfantCnsAbnormalityItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'cns_abnormality': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'cns_abnormality_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantcongenitalanomalies': {
            'Meta': {'object_name': 'InfantCongenitalAnomalies'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantctxplaceboadh': {
            'Meta': {'object_name': 'InfantCtxPlaceboAdh'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'day_missed_drug': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'reason_missed_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantctxplaceboadhaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantCtxPlaceboAdhAudit', 'db_table': "u'mpepu_infant_infantctxplaceboadh_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'day_missed_drug': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantctxplaceboadh'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'reason_missed_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantdeath': {
            'Meta': {'object_name': 'InfantDeath'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adverse_event.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adverse_event.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adverse_event.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['adverse_event.DeathReasonHospitalized']", 'null': 'True', 'blank': 'True'}),
            'death_reason_hospitalized_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['code_lists.DxCode']", 'max_length': '25'}),
            'haart_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'infant_nvp_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_drug_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'trad_med_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantdeathaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantDeathAudit', 'db_table': "u'mpepu_infant_infantdeath_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['adverse_event.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['adverse_event.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['adverse_event.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_infantdeath'", 'null': 'True', 'to': "orm['adverse_event.DeathReasonHospitalized']"}),
            'death_reason_hospitalized_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'max_length': '25', 'to': "orm['code_lists.DxCode']"}),
            'haart_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'infant_nvp_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_drug_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'trad_med_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanteligibility': {
            'Meta': {'object_name': 'InfantEligibility'},
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'congen_anomaly': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx_contra': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hiv_result_reference': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'maternal_art_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'maternal_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'rando_bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'randomization_site': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infanteligibilityaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantEligibilityAudit', 'db_table': "u'mpepu_infant_infanteligibility_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'congen_anomaly': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx_contra': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hiv_result_reference': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanteligibility'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'maternal_art_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'maternal_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'rando_bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'randomization_site': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanteligibility'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infantfacialdefectitems': {
            'Meta': {'object_name': 'InfantFacialDefectItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'facial_defect': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'facial_defects_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
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
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'solid_liquid': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'times_breastfed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'water': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'water_used': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'water_used_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'weaned_completely': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'})
        },
        'mpepu_infant.infantfeedingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFeedingAudit', 'db_table': "u'mpepu_infant_infantfeeding_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
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
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'solid_liquid': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'times_breastfed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'water': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'water_used': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'water_used_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'weaned_completely': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'})
        },
        'mpepu_infant.infantfemalegenitalanomalyitems': {
            'Meta': {'object_name': 'InfantFemaleGenitalAnomalyItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'female_genital_anomal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'female_genital_anomal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfu': {
            'Meta': {'object_name': 'InfantFu'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_illness': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_assessment': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfuaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuAudit', 'db_table': "u'mpepu_infant_infantfu_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_illness': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfu'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_assessment': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfud': {
            'Meta': {'object_name': 'InfantFuD'},
            'bloody_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'd_onset_date': ('django.db.models.fields.DateTimeField', [], {}),
            'diarrhea_episodes': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diarrhea_grade': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'fever_present': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDAudit', 'db_table': "u'mpepu_infant_infantfud_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bloody_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'd_onset_date': ('django.db.models.fields.DateTimeField', [], {}),
            'diarrhea_episodes': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diarrhea_grade': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'fever_present': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfud'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfud'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudx': {
            'Meta': {'object_name': 'InfantFuDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudx2proph': {
            'Meta': {'object_name': 'InfantFuDx2Proph'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'wcs_dx_ped': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['code_lists.WcsDxPed']", 'symmetrical': 'False'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfudx2prophaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDx2ProphAudit', 'db_table': "u'mpepu_infant_infantfudx2proph_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2proph'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2proph'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfudx2prophitems': {
            'Meta': {'object_name': 'InfantFuDx2ProphItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuDx2Proph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudx2prophitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDx2ProphItemsAudit', 'db_table': "u'mpepu_infant_infantfudx2prophitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2prophitems'", 'to': "orm['mpepu_infant.InfantFuDx2Proph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDxAudit', 'db_table': "u'mpepu_infant_infantfudx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudxitems': {
            'Meta': {'object_name': 'InfantFuDxItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'eae_reference': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'fu_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuDx']"}),
            'is_eae_required': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_infant.infantfudxitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDxItemsAudit', 'db_table': "u'mpepu_infant_infantfudxitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'eae_reference': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'fu_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudxitems'", 'to': "orm['mpepu_infant.InfantFuDx']"}),
            'is_eae_required': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_infant.infantfumed': {
            'Meta': {'object_name': 'InfantFuMed'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vaccination': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.InfantVaccines']", 'symmetrical': 'False'}),
            'vaccines_received': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfumedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuMedAudit', 'db_table': "u'mpepu_infant_infantfumed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfumed'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfumed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vaccines_received': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfunewmed': {
            'Meta': {'object_name': 'InfantFuNewMed'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'new_medications': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_medications': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfunewmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuNewMedAudit', 'db_table': "u'mpepu_infant_infantfunewmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmed'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'new_medications': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_medications': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfunewmeditems': {
            'Meta': {'object_name': 'InfantFuNewMedItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_route': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_med': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuNewMed']"}),
            'medication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfunewmeditemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuNewMedItemsAudit', 'db_table': "u'mpepu_infant_infantfunewmeditems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_route': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu_med': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmeditems'", 'to': "orm['mpepu_infant.InfantFuNewMed']"}),
            'medication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfuphysical': {
            'Meta': {'object_name': 'InfantFuPhysical'},
            'abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'head_circumference': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'mpepu_infant.infantfuphysicalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuPhysicalAudit', 'db_table': "u'mpepu_infant_infantfuphysical_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'head_circumference': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfuphysical'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfuphysical'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthaartaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHaartAudit', 'db_table': "u'mpepu_infant_infanthaart_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'haart_initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hiv_positive_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthaart'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthaartmod': {
            'Meta': {'object_name': 'InfantHaartMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_haart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantHaart']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthaartmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHaartModAudit', 'db_table': "u'mpepu_infant_infanthaartmod_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_haart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthaartmod'", 'to': "orm['mpepu_infant.InfantHaart']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthivstatus': {
            'Meta': {'object_name': 'InfantHivStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_first_pos': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_haart': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'infant_haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'recent_hiv_date': ('django.db.models.fields.DateField', [], {}),
            'recent_hiv_date_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'recent_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'result_record': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'test_place': ('django.db.models.fields.TextField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthivstatusaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHivStatusAudit', 'db_table': "u'mpepu_infant_infanthivstatus_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_first_pos': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_haart': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'infant_haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthivstatus'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'recent_hiv_date': ('django.db.models.fields.DateField', [], {}),
            'recent_hiv_date_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'recent_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'result_record': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'test_place': ('django.db.models.fields.TextField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantlowergastrointestinalitems': {
            'Meta': {'object_name': 'InfantLowerGastrointestinalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lower_gastrointestinal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'lower_gastrointestinal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantmalegenitalanomalyitems': {
            'Meta': {'object_name': 'InfantMaleGenitalAnomalyItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'male_genital_anomal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'male_genital_anomal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantmouthupgastrointestinalitems': {
            'Meta': {'object_name': 'InfantMouthUpGastrointestinalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mouth_up_gastrointest': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'mouth_up_gastrointest_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantmusculoskeletalabnormalitems': {
            'Meta': {'object_name': 'InfantMusculoskeletalAbnormalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'musculo_skeletal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'musculo_skeletal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantnvpadherence': {
            'Meta': {'object_name': 'InfantNvpAdherence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_missed': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantArvProph']"}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'reason_missed_other': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantnvpadherenceaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantNvpAdherenceAudit', 'db_table': "u'mpepu_infant_infantnvpadherence_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_missed': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantnvpadherence'", 'to': "orm['mpepu_infant.InfantArvProph']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantnvpadherence'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'reason_missed_other': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffdrug': {
            'Meta': {'object_name': 'InfantOffDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'last_dose_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_off': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_off_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffdrugaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantOffDrugAudit', 'db_table': "u'mpepu_infant_infantoffdrug_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffdrug'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'last_dose_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_off': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_off_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffdrug'", 'to': "orm['registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffstudy': {
            'Meta': {'object_name': 'InfantOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_scheduled_data': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantOffStudyAudit', 'db_table': "u'mpepu_infant_infantoffstudy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_scheduled_data': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffstudy'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffstudy'", 'to': "orm['registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantotherabnormalityitems': {
            'Meta': {'object_name': 'InfantOtherAbnormalityItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'other_abnormalities_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantpreeligibility': {
            'Meta': {'object_name': 'InfantPreEligibility'},
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infantpreeligibilityaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantPreEligibilityAudit', 'db_table': "u'mpepu_infant_infantpreeligibility_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantpreeligibility'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantpreeligibility'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infantprerandoloss': {
            'Meta': {'object_name': 'InfantPrerandoLoss'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'loss_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_loss': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'reason_loss_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantprerandolossaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantPrerandoLossAudit', 'db_table': "u'mpepu_infant_infantprerandoloss_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantprerandoloss'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'loss_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_loss': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'reason_loss_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantprerandoloss'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantrandodeferral': {
            'Meta': {'object_name': 'InfantRandoDeferral'},
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        'mpepu_infant.infantrandodeferralaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantRandoDeferralAudit', 'db_table': "u'mpepu_infant_infantrandodeferral_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrandodeferral'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrandodeferral'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        'mpepu_infant.infantrenalanomalyitems': {
            'Meta': {'object_name': 'InfantRenalAnomalyItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'renal_amomalies': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'renal_amomalies_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantrespiratorydefectitems': {
            'Meta': {'object_name': 'InfantRespiratoryDefectItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'respiratory_defect': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'respiratory_defects_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantskinabnormalitems': {
            'Meta': {'object_name': 'InfantSkinAbnormalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'skin_abnormality': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'skin_abnormality_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstoolcollection': {
            'Meta': {'object_name': 'InfantStoolCollection'},
            'antibiotic_dose_24hrs': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'antibiotics_7days': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'axi_temp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_past_24hrs': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'past_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sample_obtained': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstoolcollectionaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStoolCollectionAudit', 'db_table': "u'mpepu_infant_infantstoolcollection_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'antibiotic_dose_24hrs': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'antibiotics_7days': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'axi_temp': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '1', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_past_24hrs': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstoolcollection'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'past_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sample_obtained': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrug': {
            'Meta': {'object_name': 'InfantStudyDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_status': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_placebo_status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrugaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugAudit', 'db_table': "u'mpepu_infant_infantstudydrug_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_status': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydrug'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_placebo_status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydruginit': {
            'Meta': {'object_name': 'InfantStudyDrugInit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_not_init': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'reason_not_init_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_not_survive': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydruginitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugInitAudit', 'db_table': "u'mpepu_infant_infantstudydruginit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydruginit'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_not_init': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'reason_not_init_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_not_survive': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrugitems': {
            'Meta': {'ordering': "['ingestion_date']", 'object_name': 'InfantStudyDrugItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'inf_study_drug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantStudyDrug']"}),
            'ingestion_date': ('django.db.models.fields.DateField', [], {}),
            'modification_reason': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrugitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugItemsAudit', 'db_table': "u'mpepu_infant_infantstudydrugitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'inf_study_drug': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydrugitems'", 'to': "orm['mpepu_infant.InfantStudyDrug']"}),
            'ingestion_date': ('django.db.models.fields.DateField', [], {}),
            'modification_reason': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantsurvival': {
            'Meta': {'object_name': 'InfantSurvival'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_survival_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'info_provider': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantsurvivalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantSurvivalAudit', 'db_table': "u'mpepu_infant_infantsurvival_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_survival_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantsurvival'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'info_provider': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantsurvival'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanttrisomieschromosomeitems': {
            'Meta': {'object_name': 'InfantTrisomiesChromosomeItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'triso_chromo_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'triso_chromo_abnormal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantverbalautopsy': {
            'Meta': {'object_name': 'InfantVerbalAutopsy'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_sign': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prop_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sign_symptoms': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.AutopsyInfoSource']", 'max_length': '50', 'symmetrical': 'False'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantverbalautopsyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantVerbalAutopsyAudit', 'db_table': "u'mpepu_infant_infantverbalautopsy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_sign': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantverbalautopsy'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prop_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantverbalautopsy'", 'to': "orm['registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sign_symptoms': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantverbalautopsyitems': {
            'Meta': {'object_name': 'InfantVerbalAutopsyItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'sign_symptom': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'verbal_autopsy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVerbalAutopsy']"})
        },
        'mpepu_infant.infantvisit': {
            'Meta': {'object_name': 'InfantVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'information_provider': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'information_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantvisitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantVisitAudit', 'db_table': "'mpepu_infant_infantvisit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantvisit'", 'to': "orm['appointment.Appointment']"}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'information_provider': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'information_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
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
            'ga': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_chorioamnionitis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_del_comp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_ga': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'has_urine_tender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'labour_hrs': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'labr_max_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'live_infants': ('django.db.models.fields.IntegerField', [], {}),
            'live_infants_to_register': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 5, 5, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'still_born_congen_abn': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'still_born_has_congen_abn': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'still_borns': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalvisit': {
            'Meta': {'object_name': 'MaternalVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'unique_together': "(('first_name', 'dob', 'initials'),)", 'object_name': 'RegisteredSubject', 'db_table': "'bhp_registration_registeredsubject'"},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'subject_identifier_as_pk': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'visit_schedule.membershipform': {
            'Meta': {'object_name': 'MembershipForm', 'db_table': "'bhp_visit_membershipform'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '35', 'unique': 'True', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'visit_schedule.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup', 'db_table': "'bhp_visit_schedulegroup'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'membership_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['visit_schedule.MembershipForm']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'visit_schedule.visitdefinition': {
            'Meta': {'ordering': "['code', 'time_point']", 'object_name': 'VisitDefinition', 'db_table': "'bhp_visit_visitdefinition'"},
            'base_interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_interval_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'s007'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'lower_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lower_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'schedule_group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['visit_schedule.ScheduleGroup']", 'null': 'True', 'blank': 'True'}),
            'time_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_index': 'True'}),
            'upper_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upper_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit_tracking_content_type_map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_content_type_map.ContentTypeMap']", 'null': 'True'})
        }
    }

    complete_apps = ['mpepu_infant']