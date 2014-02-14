# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MaternalEnrollDemAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenrolldem_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollDemAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenrolldem_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollDemAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrolldem_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalArvPregHistoryAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarvpreghistory_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvPregHistoryAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarvpreghistory_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPregHistoryAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpreghistory_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalArvPregAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarvpreg_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvPregAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarvpreg_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPregAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpreg_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalVisit.revision'
        db.add_column('mpepu_maternal_maternalvisit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalVisit.subject_identifier'
        db.add_column('mpepu_maternal_maternalvisit', 'subject_identifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'MaternalVisit.appointment'
        db.alter_column('mpepu_maternal_maternalvisit', 'appointment_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appointment.Appointment'], unique=True))
        # Deleting field 'MaternalLabDelMedAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternallabdelmed_audit', '_audit_subject_identifier')

        # Adding field 'MaternalLabDelMedAudit.revision'
        db.add_column(u'mpepu_maternal_maternallabdelmed_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelMedAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdelmed_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalConsentAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalconsent_audit', '_audit_subject_identifier')

        # Adding field 'MaternalConsentAudit.revision'
        db.add_column(u'mpepu_maternal_maternalconsent_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalConsentAudit.language'
        db.add_column(u'mpepu_maternal_maternalconsent_audit', 'language',
                      self.gf('django.db.models.fields.CharField')(default='not specified', max_length=25),
                      keep_default=False)


        # Changing field 'MaternalConsentAudit.study_site'
        db.alter_column(u'mpepu_maternal_maternalconsent_audit', 'study_site_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bhp_variables.StudySite']))

        # Changing field 'MaternalConsentAudit.initials'
        db.alter_column(u'mpepu_maternal_maternalconsent_audit', 'initials', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))
        # Deleting field 'MaternalVisitAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalvisit_audit', '_audit_subject_identifier')

        # Adding field 'MaternalVisitAudit.revision'
        db.add_column('mpepu_maternal_maternalvisit_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalVisitAudit.subject_identifier'
        db.add_column('mpepu_maternal_maternalvisit_audit', 'subject_identifier',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'MaternalVisitAudit.appointment'
        db.alter_column('mpepu_maternal_maternalvisit_audit', 'appointment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appointment.Appointment']))
        # Deleting field 'MaternalLabDelDxAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternallabdeldx_audit', '_audit_subject_identifier')

        # Adding field 'MaternalLabDelDxAudit.revision'
        db.add_column(u'mpepu_maternal_maternallabdeldx_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelDxAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdeldx_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalArv.revision'
        db.add_column(u'mpepu_maternal_maternalarv', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoice.revision'
        db.add_column(u'mpepu_maternal_feedingchoice', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoice.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoice', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalDeathAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternaldeath_audit', '_audit_subject_identifier')

        # Adding field 'MaternalDeathAudit.revision'
        db.add_column(u'mpepu_maternal_maternaldeath_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalDeathAudit.dx_code'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(max_length=25, to=orm['code_lists.DxCode']))

        # Changing field 'MaternalDeathAudit.death_cause_category'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseCategory']))

        # Changing field 'MaternalDeathAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))

        # Changing field 'MaternalDeathAudit.death_reason_hospitalized'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['adverse_event.DeathReasonHospitalized']))

        # Changing field 'MaternalDeathAudit.death_cause_info'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseInfo']))

        # Changing field 'MaternalDeathAudit.death_medical_responsibility'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathMedicalResponsibility']))
        # Deleting field 'MaternalPostFuAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalpostfu_audit', '_audit_subject_identifier')

        # Adding field 'MaternalPostFuAudit.revision'
        db.add_column(u'mpepu_maternal_maternalpostfu_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFuAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalpostfu_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'FeedingChoiceAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_feedingchoice_audit', '_audit_subject_identifier')

        # Adding field 'FeedingChoiceAudit.revision'
        db.add_column(u'mpepu_maternal_feedingchoice_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceAudit.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoice_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalLabDelDx.revision'
        db.add_column(u'mpepu_maternal_maternallabdeldx', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelDx.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdeldx', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalArvPregHistory.revision'
        db.add_column(u'mpepu_maternal_maternalarvpreghistory', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPregHistory.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpreghistory', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalArvPostAdh.revision'
        db.add_column(u'mpepu_maternal_maternalarvpostadh', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPostAdh.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpostadh', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'PostNatalInfantFeedingSurveyAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_postnatalinfantfeedingsurvey_audit', '_audit_subject_identifier')

        # Adding field 'PostNatalInfantFeedingSurveyAudit.revision'
        db.add_column(u'mpepu_maternal_postnatalinfantfeedingsurvey_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PostNatalInfantFeedingSurveyAudit.report_datetime'
        db.add_column(u'mpepu_maternal_postnatalinfantfeedingsurvey_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


        # Changing field 'PostNatalInfantFeedingSurveyAudit.feeding_duration'
        db.alter_column(u'mpepu_maternal_postnatalinfantfeedingsurvey_audit', 'feeding_duration', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))
        # Deleting field 'MaternalEligibilityPostAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternaleligibilitypost_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEligibilityPostAudit.revision'
        db.add_column(u'mpepu_maternal_maternaleligibilitypost_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalEligibilityPostAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilitypost_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Adding field 'MaternalEnrollOb.revision'
        db.add_column(u'mpepu_maternal_maternalenrollob', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollOb.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollob', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionOne.revision'
        db.add_column(u'mpepu_maternal_feedingchoicesectionone', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionOne.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoicesectionone', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalEnrollArv.revision'
        db.add_column(u'mpepu_maternal_maternalenrollarv', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollArv.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollarv', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionTwo.revision'
        db.add_column(u'mpepu_maternal_feedingchoicesectiontwo', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionTwo.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoicesectiontwo', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalEligibilityAnteAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternaleligibilityante_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEligibilityAnteAudit.revision'
        db.add_column(u'mpepu_maternal_maternaleligibilityante_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalEligibilityAnteAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilityante_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Deleting field 'MaternalLabDelDxTAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternallabdeldxt_audit', '_audit_subject_identifier')

        # Adding field 'MaternalLabDelDxTAudit.revision'
        db.add_column(u'mpepu_maternal_maternallabdeldxt_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelDxTAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdeldxt_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'PostNatalInfantFeedingSurvey.revision'
        db.add_column(u'mpepu_maternal_postnatalinfantfeedingsurvey', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'PostNatalInfantFeedingSurvey.report_datetime'
        db.add_column(u'mpepu_maternal_postnatalinfantfeedingsurvey', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


        # Changing field 'PostNatalInfantFeedingSurvey.feeding_duration'
        db.alter_column(u'mpepu_maternal_postnatalinfantfeedingsurvey', 'feeding_duration', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))
        # Deleting field 'FeedingChoiceSectionTwoAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_feedingchoicesectiontwo_audit', '_audit_subject_identifier')

        # Adding field 'FeedingChoiceSectionTwoAudit.revision'
        db.add_column(u'mpepu_maternal_feedingchoicesectiontwo_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionTwoAudit.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoicesectiontwo_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalEnrollAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenroll_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenroll_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenroll_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalEnrollAudit.recruitment_clinic'
        db.add_column(u'mpepu_maternal_maternalenroll_audit', 'recruitment_clinic',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'MaternalEnrollAudit.recruitment_clinic_other'
        db.add_column(u'mpepu_maternal_maternalenroll_audit', 'recruitment_clinic_other',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollAudit.bp'
        db.add_column(u'mpepu_maternal_maternalenroll_audit', 'bp',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=7),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionThree.revision'
        db.add_column(u'mpepu_maternal_feedingchoicesectionthree', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionThree.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoicesectionthree', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalOffStudy.revision'
        db.add_column(u'mpepu_maternal_maternaloffstudy', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalOffStudy.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaloffstudy', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'MaternalEligibilityPost.revision'
        db.add_column(u'mpepu_maternal_maternaleligibilitypost', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalEligibilityPost.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilitypost', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'MaternalArvPostMod.revision'
        db.add_column(u'mpepu_maternal_maternalarvpostmod', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'MaternalOffStudyAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternaloffstudy_audit', '_audit_subject_identifier')

        # Adding field 'MaternalOffStudyAudit.revision'
        db.add_column(u'mpepu_maternal_maternaloffstudy_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalOffStudyAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaloffstudy_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Deleting field 'FeedingChoiceSectionOneAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_feedingchoicesectionone_audit', '_audit_subject_identifier')

        # Adding field 'FeedingChoiceSectionOneAudit.revision'
        db.add_column(u'mpepu_maternal_feedingchoicesectionone_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionOneAudit.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoicesectionone_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalLabDelClinicAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternallabdelclinic_audit', '_audit_subject_identifier')

        # Adding field 'MaternalLabDelClinicAudit.revision'
        db.add_column(u'mpepu_maternal_maternallabdelclinic_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelClinicAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdelclinic_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalDeath.revision'
        db.add_column(u'mpepu_maternal_maternaldeath', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalDeath.dx_code'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['code_lists.DxCode'], max_length=25))

        # Changing field 'MaternalDeath.death_cause_category'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseCategory']))

        # Changing field 'MaternalDeath.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))

        # Changing field 'MaternalDeath.death_reason_hospitalized'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathReasonHospitalized'], null=True))

        # Changing field 'MaternalDeath.death_cause_info'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathCauseInfo']))

        # Changing field 'MaternalDeath.death_medical_responsibility'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['adverse_event.DeathMedicalResponsibility']))
        # Deleting field 'MaternalEnrollClinAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenrollclin_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollClinAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenrollclin_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollClinAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollclin_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalArvPostModAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarvpostmod_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvPostModAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarvpostmod_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEligibilityAnte.revision'
        db.add_column(u'mpepu_maternal_maternaleligibilityante', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalEligibilityAnte.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilityante', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Adding field 'MaternalEnrollDx.revision'
        db.add_column(u'mpepu_maternal_maternalenrolldx', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollDx.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrolldx', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


        # Changing field 'MaternalEnrollDx.diagnosis_year'
        db.alter_column(u'mpepu_maternal_maternalenrolldx', 'diagnosis_year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'MaternalEnrollDx.diagnosis'
        db.alter_column(u'mpepu_maternal_maternalenrolldx', 'diagnosis', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
        # Deleting field 'MaternalEnrollDxAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenrolldx_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollDxAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenrolldx_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollDxAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrolldx_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


        # Changing field 'MaternalEnrollDxAudit.diagnosis_year'
        db.alter_column(u'mpepu_maternal_maternalenrolldx_audit', 'diagnosis_year', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'MaternalEnrollDxAudit.diagnosis'
        db.alter_column(u'mpepu_maternal_maternalenrolldx_audit', 'diagnosis', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))
        # Deleting field 'MaternalPostRegAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalpostreg_audit', '_audit_subject_identifier')

        # Adding field 'MaternalPostRegAudit.revision'
        db.add_column(u'mpepu_maternal_maternalpostreg_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalPostRegAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternalpostreg_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.RegisteredSubject']))
        # Deleting field 'MaternalArvPostAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarvpost_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvPostAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarvpost_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPostAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpost_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalEnroll.revision'
        db.add_column(u'mpepu_maternal_maternalenroll', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnroll.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenroll', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalEnroll.recruitment_clinic'
        db.add_column(u'mpepu_maternal_maternalenroll', 'recruitment_clinic',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'MaternalEnroll.recruitment_clinic_other'
        db.add_column(u'mpepu_maternal_maternalenroll', 'recruitment_clinic_other',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnroll.bp'
        db.add_column(u'mpepu_maternal_maternalenroll', 'bp',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=7),
                      keep_default=False)

        # Adding field 'MaternalEnrollMed.revision'
        db.add_column(u'mpepu_maternal_maternalenrollmed', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollMed.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollmed', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalEnrollArvAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenrollarv_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollArvAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenrollarv_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollArvAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollarv_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalPostFu.revision'
        db.add_column(u'mpepu_maternal_maternalpostfu', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFu.report_datetime'
        db.add_column(u'mpepu_maternal_maternalpostfu', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalPostFuDxTAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalpostfudxt_audit', '_audit_subject_identifier')

        # Adding field 'MaternalPostFuDxTAudit.revision'
        db.add_column(u'mpepu_maternal_maternalpostfudxt_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFuDxTAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalpostfudxt_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


        # Changing field 'MaternalPostFuDxTAudit.hospitalized'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt_audit', 'hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'MaternalPostFuDxTAudit.grade'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt_audit', 'grade', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True))

        # Changing field 'MaternalPostFuDxTAudit.post_fu_dx'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt_audit', 'post_fu_dx', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Deleting field 'MaternalPostFuDxAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalpostfudx_audit', '_audit_subject_identifier')

        # Adding field 'MaternalPostFuDxAudit.revision'
        db.add_column(u'mpepu_maternal_maternalpostfudx_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFuDxAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalpostfudx_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalArvPostAdhAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarvpostadh_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvPostAdhAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarvpostadh_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPostAdhAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpostadh_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalConsentUpdate.revision'
        db.add_column(u'mpepu_maternal_maternalconsentupdate', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalConsentUpdate.consent_catalogue'
        db.alter_column(u'mpepu_maternal_maternalconsentupdate', 'consent_catalogue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['consent.ConsentCatalogue']))
        # Adding field 'MaternalEnrollDem.revision'
        db.add_column(u'mpepu_maternal_maternalenrolldem', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollDem.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrolldem', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalArvPPHistoryAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarvpphistory_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvPPHistoryAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarvpphistory_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPPHistoryAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpphistory_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalLabDelMed.revision'
        db.add_column(u'mpepu_maternal_maternallabdelmed', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelMed.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdelmed', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalPostReg.revision'
        db.add_column(u'mpepu_maternal_maternalpostreg', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)


        # Changing field 'MaternalPostReg.registered_subject'
        db.alter_column(u'mpepu_maternal_maternalpostreg', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True))
        # Deleting field 'MaternalLocatorAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternallocator_audit', '_audit_subject_identifier')

        # Adding field 'MaternalLocatorAudit.revision'
        db.add_column(u'mpepu_maternal_maternallocator_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLocatorAudit.may_sms_follow_up'
        db.add_column(u'mpepu_maternal_maternallocator_audit', 'may_sms_follow_up',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
                      keep_default=False)


        # Changing field 'MaternalLocatorAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternallocator_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['registration.RegisteredSubject']))
        # Adding field 'MaternalArvPPHistory.revision'
        db.add_column(u'mpepu_maternal_maternalarvpphistory', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPPHistory.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpphistory', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalArvPreg.revision'
        db.add_column(u'mpepu_maternal_maternalarvpreg', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPreg.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpreg', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalPostFuDx.revision'
        db.add_column(u'mpepu_maternal_maternalpostfudx', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFuDx.report_datetime'
        db.add_column(u'mpepu_maternal_maternalpostfudx', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalLabDelClinic.revision'
        db.add_column(u'mpepu_maternal_maternallabdelclinic', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelClinic.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdelclinic', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalEnrollClin.revision'
        db.add_column(u'mpepu_maternal_maternalenrollclin', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollClin.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollclin', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalLabDelDxT.revision'
        db.add_column(u'mpepu_maternal_maternallabdeldxt', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelDxT.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdeldxt', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalArvAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalarv_audit', '_audit_subject_identifier')

        # Adding field 'MaternalArvAudit.revision'
        db.add_column(u'mpepu_maternal_maternalarv_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFuDxT.revision'
        db.add_column(u'mpepu_maternal_maternalpostfudxt', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalPostFuDxT.report_datetime'
        db.add_column(u'mpepu_maternal_maternalpostfudxt', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


        # Changing field 'MaternalPostFuDxT.hospitalized'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt', 'hospitalized', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))

        # Changing field 'MaternalPostFuDxT.grade'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt', 'grade', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True))

        # Changing field 'MaternalPostFuDxT.post_fu_dx'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt', 'post_fu_dx', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))
        # Deleting field 'MaternalEnrollObAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenrollob_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollObAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenrollob_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollObAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollob_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'FeedingChoiceSectionThreeAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_feedingchoicesectionthree_audit', '_audit_subject_identifier')

        # Adding field 'FeedingChoiceSectionThreeAudit.revision'
        db.add_column(u'mpepu_maternal_feedingchoicesectionthree_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'FeedingChoiceSectionThreeAudit.report_datetime'
        db.add_column(u'mpepu_maternal_feedingchoicesectionthree_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalLabDelAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternallabdel_audit', '_audit_subject_identifier')

        # Adding field 'MaternalLabDelAudit.revision'
        db.add_column(u'mpepu_maternal_maternallabdel_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDelAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdel_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalConsent.revision'
        db.add_column(u'mpepu_maternal_maternalconsent', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalConsent.language'
        db.add_column(u'mpepu_maternal_maternalconsent', 'language',
                      self.gf('django.db.models.fields.CharField')(default='not specified', max_length=25),
                      keep_default=False)


        # Changing field 'MaternalConsent.study_site'
        db.alter_column(u'mpepu_maternal_maternalconsent', 'study_site_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_variables.StudySite'], null=True))

        # Changing field 'MaternalConsent.initials'
        db.alter_column(u'mpepu_maternal_maternalconsent', 'initials', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))
        # Adding field 'MaternalArvPost.revision'
        db.add_column(u'mpepu_maternal_maternalarvpost', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalArvPost.report_datetime'
        db.add_column(u'mpepu_maternal_maternalarvpost', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Deleting field 'MaternalEnrollMedAudit._audit_subject_identifier'
        db.delete_column('mpepu_maternal_maternalenrollmed_audit', '_audit_subject_identifier')

        # Adding field 'MaternalEnrollMedAudit.revision'
        db.add_column(u'mpepu_maternal_maternalenrollmed_audit', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalEnrollMedAudit.report_datetime'
        db.add_column(u'mpepu_maternal_maternalenrollmed_audit', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)

        # Adding field 'MaternalLocator.revision'
        db.add_column(u'mpepu_maternal_maternallocator', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLocator.may_sms_follow_up'
        db.add_column(u'mpepu_maternal_maternallocator', 'may_sms_follow_up',
                      self.gf('django.db.models.fields.CharField')(max_length=25, null=True),
                      keep_default=False)


        # Changing field 'MaternalLocator.registered_subject'
        db.alter_column(u'mpepu_maternal_maternallocator', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['registration.RegisteredSubject'], unique=True, null=True))
        # Adding field 'MaternalLabDel.revision'
        db.add_column(u'mpepu_maternal_maternallabdel', 'revision',
                      self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True),
                      keep_default=False)

        # Adding field 'MaternalLabDel.report_datetime'
        db.add_column(u'mpepu_maternal_maternallabdel', 'report_datetime',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 2, 12, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MaternalEnrollDemAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenrolldem_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollDemAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenrolldem_audit', 'revision')

        # Deleting field 'MaternalEnrollDemAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrolldem_audit', 'report_datetime')

        # Adding field 'MaternalArvPregHistoryAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarvpreghistory_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvPregHistoryAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpreghistory_audit', 'revision')

        # Deleting field 'MaternalArvPregHistoryAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpreghistory_audit', 'report_datetime')

        # Adding field 'MaternalArvPregAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarvpreg_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvPregAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpreg_audit', 'revision')

        # Deleting field 'MaternalArvPregAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpreg_audit', 'report_datetime')

        # Deleting field 'MaternalVisit.revision'
        db.delete_column('mpepu_maternal_maternalvisit', 'revision')

        # Deleting field 'MaternalVisit.subject_identifier'
        db.delete_column('mpepu_maternal_maternalvisit', 'subject_identifier')


        # Changing field 'MaternalVisit.appointment'
        db.alter_column('mpepu_maternal_maternalvisit', 'appointment_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_appointment.Appointment'], unique=True))
        # Adding field 'MaternalLabDelMedAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternallabdelmed_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalLabDelMedAudit.revision'
        db.delete_column(u'mpepu_maternal_maternallabdelmed_audit', 'revision')

        # Deleting field 'MaternalLabDelMedAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdelmed_audit', 'report_datetime')

        # Adding field 'MaternalConsentAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalconsent_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalConsentAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalconsent_audit', 'revision')

        # Deleting field 'MaternalConsentAudit.language'
        db.delete_column(u'mpepu_maternal_maternalconsent_audit', 'language')


        # Changing field 'MaternalConsentAudit.study_site'
        db.alter_column(u'mpepu_maternal_maternalconsent_audit', 'study_site_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bhp_variables.StudySite']))

        # Changing field 'MaternalConsentAudit.initials'
        db.alter_column(u'mpepu_maternal_maternalconsent_audit', 'initials', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding field 'MaternalVisitAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalvisit_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalVisitAudit.revision'
        db.delete_column('mpepu_maternal_maternalvisit_audit', 'revision')

        # Deleting field 'MaternalVisitAudit.subject_identifier'
        db.delete_column('mpepu_maternal_maternalvisit_audit', 'subject_identifier')


        # Changing field 'MaternalVisitAudit.appointment'
        db.alter_column('mpepu_maternal_maternalvisit_audit', 'appointment_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_appointment.Appointment']))
        # Adding field 'MaternalLabDelDxAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternallabdeldx_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalLabDelDxAudit.revision'
        db.delete_column(u'mpepu_maternal_maternallabdeldx_audit', 'revision')

        # Deleting field 'MaternalLabDelDxAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdeldx_audit', 'report_datetime')

        # Deleting field 'MaternalArv.revision'
        db.delete_column(u'mpepu_maternal_maternalarv', 'revision')

        # Deleting field 'FeedingChoice.revision'
        db.delete_column(u'mpepu_maternal_feedingchoice', 'revision')

        # Deleting field 'FeedingChoice.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoice', 'report_datetime')

        # Adding field 'MaternalDeathAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternaldeath_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalDeathAudit.revision'
        db.delete_column(u'mpepu_maternal_maternaldeath_audit', 'revision')


        # Changing field 'MaternalDeathAudit.dx_code'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(max_length=25, to=orm['bhp_code_lists.DxCode']))

        # Changing field 'MaternalDeathAudit.death_cause_category'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseCategory']))

        # Changing field 'MaternalDeathAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))

        # Changing field 'MaternalDeathAudit.death_reason_hospitalized'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bhp_adverse.DeathReasonHospitalized']))

        # Changing field 'MaternalDeathAudit.death_cause_info'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseInfo']))

        # Changing field 'MaternalDeathAudit.death_medical_responsibility'
        db.alter_column(u'mpepu_maternal_maternaldeath_audit', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathMedicalResponsibility']))
        # Adding field 'MaternalPostFuAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalpostfu_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalPostFuAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalpostfu_audit', 'revision')

        # Deleting field 'MaternalPostFuAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalpostfu_audit', 'report_datetime')

        # Adding field 'FeedingChoiceAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_feedingchoice_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'FeedingChoiceAudit.revision'
        db.delete_column(u'mpepu_maternal_feedingchoice_audit', 'revision')

        # Deleting field 'FeedingChoiceAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoice_audit', 'report_datetime')

        # Deleting field 'MaternalLabDelDx.revision'
        db.delete_column(u'mpepu_maternal_maternallabdeldx', 'revision')

        # Deleting field 'MaternalLabDelDx.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdeldx', 'report_datetime')

        # Deleting field 'MaternalArvPregHistory.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpreghistory', 'revision')

        # Deleting field 'MaternalArvPregHistory.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpreghistory', 'report_datetime')

        # Deleting field 'MaternalArvPostAdh.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpostadh', 'revision')

        # Deleting field 'MaternalArvPostAdh.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpostadh', 'report_datetime')

        # Adding field 'PostNatalInfantFeedingSurveyAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_postnatalinfantfeedingsurvey_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'PostNatalInfantFeedingSurveyAudit.revision'
        db.delete_column(u'mpepu_maternal_postnatalinfantfeedingsurvey_audit', 'revision')

        # Deleting field 'PostNatalInfantFeedingSurveyAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_postnatalinfantfeedingsurvey_audit', 'report_datetime')


        # Changing field 'PostNatalInfantFeedingSurveyAudit.feeding_duration'
        db.alter_column(u'mpepu_maternal_postnatalinfantfeedingsurvey_audit', 'feeding_duration', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding field 'MaternalEligibilityPostAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternaleligibilitypost_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEligibilityPostAudit.revision'
        db.delete_column(u'mpepu_maternal_maternaleligibilitypost_audit', 'revision')


        # Changing field 'MaternalEligibilityPostAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilitypost_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
        # Deleting field 'MaternalEnrollOb.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollob', 'revision')

        # Deleting field 'MaternalEnrollOb.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollob', 'report_datetime')

        # Deleting field 'FeedingChoiceSectionOne.revision'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionone', 'revision')

        # Deleting field 'FeedingChoiceSectionOne.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionone', 'report_datetime')

        # Deleting field 'MaternalEnrollArv.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollarv', 'revision')

        # Deleting field 'MaternalEnrollArv.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollarv', 'report_datetime')

        # Deleting field 'FeedingChoiceSectionTwo.revision'
        db.delete_column(u'mpepu_maternal_feedingchoicesectiontwo', 'revision')

        # Deleting field 'FeedingChoiceSectionTwo.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoicesectiontwo', 'report_datetime')

        # Adding field 'MaternalEligibilityAnteAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternaleligibilityante_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEligibilityAnteAudit.revision'
        db.delete_column(u'mpepu_maternal_maternaleligibilityante_audit', 'revision')


        # Changing field 'MaternalEligibilityAnteAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilityante_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
        # Adding field 'MaternalLabDelDxTAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternallabdeldxt_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalLabDelDxTAudit.revision'
        db.delete_column(u'mpepu_maternal_maternallabdeldxt_audit', 'revision')

        # Deleting field 'MaternalLabDelDxTAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdeldxt_audit', 'report_datetime')

        # Deleting field 'PostNatalInfantFeedingSurvey.revision'
        db.delete_column(u'mpepu_maternal_postnatalinfantfeedingsurvey', 'revision')

        # Deleting field 'PostNatalInfantFeedingSurvey.report_datetime'
        db.delete_column(u'mpepu_maternal_postnatalinfantfeedingsurvey', 'report_datetime')


        # Changing field 'PostNatalInfantFeedingSurvey.feeding_duration'
        db.alter_column(u'mpepu_maternal_postnatalinfantfeedingsurvey', 'feeding_duration', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding field 'FeedingChoiceSectionTwoAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_feedingchoicesectiontwo_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'FeedingChoiceSectionTwoAudit.revision'
        db.delete_column(u'mpepu_maternal_feedingchoicesectiontwo_audit', 'revision')

        # Deleting field 'FeedingChoiceSectionTwoAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoicesectiontwo_audit', 'report_datetime')

        # Adding field 'MaternalEnrollAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenroll_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenroll_audit', 'revision')

        # Deleting field 'MaternalEnrollAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenroll_audit', 'report_datetime')

        # Deleting field 'MaternalEnrollAudit.recruitment_clinic'
        db.delete_column(u'mpepu_maternal_maternalenroll_audit', 'recruitment_clinic')

        # Deleting field 'MaternalEnrollAudit.recruitment_clinic_other'
        db.delete_column(u'mpepu_maternal_maternalenroll_audit', 'recruitment_clinic_other')

        # Deleting field 'MaternalEnrollAudit.bp'
        db.delete_column(u'mpepu_maternal_maternalenroll_audit', 'bp')

        # Deleting field 'FeedingChoiceSectionThree.revision'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionthree', 'revision')

        # Deleting field 'FeedingChoiceSectionThree.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionthree', 'report_datetime')

        # Deleting field 'MaternalOffStudy.revision'
        db.delete_column(u'mpepu_maternal_maternaloffstudy', 'revision')


        # Changing field 'MaternalOffStudy.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaloffstudy', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
        # Deleting field 'MaternalEligibilityPost.revision'
        db.delete_column(u'mpepu_maternal_maternaleligibilitypost', 'revision')


        # Changing field 'MaternalEligibilityPost.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilitypost', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
        # Deleting field 'MaternalArvPostMod.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpostmod', 'revision')

        # Adding field 'MaternalOffStudyAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternaloffstudy_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalOffStudyAudit.revision'
        db.delete_column(u'mpepu_maternal_maternaloffstudy_audit', 'revision')


        # Changing field 'MaternalOffStudyAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaloffstudy_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
        # Adding field 'FeedingChoiceSectionOneAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_feedingchoicesectionone_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'FeedingChoiceSectionOneAudit.revision'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionone_audit', 'revision')

        # Deleting field 'FeedingChoiceSectionOneAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionone_audit', 'report_datetime')

        # Adding field 'MaternalLabDelClinicAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternallabdelclinic_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalLabDelClinicAudit.revision'
        db.delete_column(u'mpepu_maternal_maternallabdelclinic_audit', 'revision')

        # Deleting field 'MaternalLabDelClinicAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdelclinic_audit', 'report_datetime')

        # Deleting field 'MaternalDeath.revision'
        db.delete_column(u'mpepu_maternal_maternaldeath', 'revision')


        # Changing field 'MaternalDeath.dx_code'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'dx_code_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_code_lists.DxCode'], max_length=25))

        # Changing field 'MaternalDeath.death_cause_category'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_cause_category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseCategory']))

        # Changing field 'MaternalDeath.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))

        # Changing field 'MaternalDeath.death_reason_hospitalized'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_reason_hospitalized_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathReasonHospitalized'], null=True))

        # Changing field 'MaternalDeath.death_cause_info'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_cause_info_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathCauseInfo']))

        # Changing field 'MaternalDeath.death_medical_responsibility'
        db.alter_column(u'mpepu_maternal_maternaldeath', 'death_medical_responsibility_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_adverse.DeathMedicalResponsibility']))
        # Adding field 'MaternalEnrollClinAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenrollclin_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollClinAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollclin_audit', 'revision')

        # Deleting field 'MaternalEnrollClinAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollclin_audit', 'report_datetime')

        # Adding field 'MaternalArvPostModAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarvpostmod_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvPostModAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpostmod_audit', 'revision')

        # Deleting field 'MaternalEligibilityAnte.revision'
        db.delete_column(u'mpepu_maternal_maternaleligibilityante', 'revision')


        # Changing field 'MaternalEligibilityAnte.registered_subject'
        db.alter_column(u'mpepu_maternal_maternaleligibilityante', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
        # Deleting field 'MaternalEnrollDx.revision'
        db.delete_column(u'mpepu_maternal_maternalenrolldx', 'revision')

        # Deleting field 'MaternalEnrollDx.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrolldx', 'report_datetime')


        # Changing field 'MaternalEnrollDx.diagnosis_year'
        db.alter_column(u'mpepu_maternal_maternalenrolldx', 'diagnosis_year', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'MaternalEnrollDx.diagnosis'
        db.alter_column(u'mpepu_maternal_maternalenrolldx', 'diagnosis', self.gf('django.db.models.fields.CharField')(default='', max_length=50))
        # Adding field 'MaternalEnrollDxAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenrolldx_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollDxAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenrolldx_audit', 'revision')

        # Deleting field 'MaternalEnrollDxAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrolldx_audit', 'report_datetime')


        # Changing field 'MaternalEnrollDxAudit.diagnosis_year'
        db.alter_column(u'mpepu_maternal_maternalenrolldx_audit', 'diagnosis_year', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'MaternalEnrollDxAudit.diagnosis'
        db.alter_column(u'mpepu_maternal_maternalenrolldx_audit', 'diagnosis', self.gf('django.db.models.fields.CharField')(default='', max_length=50))
        # Adding field 'MaternalPostRegAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalpostreg_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalPostRegAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalpostreg_audit', 'revision')


        # Changing field 'MaternalPostRegAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternalpostreg_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_registration.RegisteredSubject']))
        # Adding field 'MaternalArvPostAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarvpost_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvPostAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpost_audit', 'revision')

        # Deleting field 'MaternalArvPostAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpost_audit', 'report_datetime')

        # Deleting field 'MaternalEnroll.revision'
        db.delete_column(u'mpepu_maternal_maternalenroll', 'revision')

        # Deleting field 'MaternalEnroll.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenroll', 'report_datetime')

        # Deleting field 'MaternalEnroll.recruitment_clinic'
        db.delete_column(u'mpepu_maternal_maternalenroll', 'recruitment_clinic')

        # Deleting field 'MaternalEnroll.recruitment_clinic_other'
        db.delete_column(u'mpepu_maternal_maternalenroll', 'recruitment_clinic_other')

        # Deleting field 'MaternalEnroll.bp'
        db.delete_column(u'mpepu_maternal_maternalenroll', 'bp')

        # Deleting field 'MaternalEnrollMed.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollmed', 'revision')

        # Deleting field 'MaternalEnrollMed.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollmed', 'report_datetime')

        # Adding field 'MaternalEnrollArvAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenrollarv_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollArvAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollarv_audit', 'revision')

        # Deleting field 'MaternalEnrollArvAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollarv_audit', 'report_datetime')

        # Deleting field 'MaternalPostFu.revision'
        db.delete_column(u'mpepu_maternal_maternalpostfu', 'revision')

        # Deleting field 'MaternalPostFu.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalpostfu', 'report_datetime')

        # Adding field 'MaternalPostFuDxTAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalpostfudxt_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalPostFuDxTAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalpostfudxt_audit', 'revision')

        # Deleting field 'MaternalPostFuDxTAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalpostfudxt_audit', 'report_datetime')


        # Changing field 'MaternalPostFuDxTAudit.hospitalized'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt_audit', 'hospitalized', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'MaternalPostFuDxTAudit.grade'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt_audit', 'grade', self.gf('django.db.models.fields.IntegerField')(default='', max_length=3))

        # Changing field 'MaternalPostFuDxTAudit.post_fu_dx'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt_audit', 'post_fu_dx', self.gf('django.db.models.fields.CharField')(default='', max_length=100))
        # Adding field 'MaternalPostFuDxAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalpostfudx_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalPostFuDxAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalpostfudx_audit', 'revision')

        # Deleting field 'MaternalPostFuDxAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalpostfudx_audit', 'report_datetime')

        # Adding field 'MaternalArvPostAdhAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarvpostadh_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvPostAdhAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpostadh_audit', 'revision')

        # Deleting field 'MaternalArvPostAdhAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpostadh_audit', 'report_datetime')

        # Deleting field 'MaternalConsentUpdate.revision'
        db.delete_column(u'mpepu_maternal_maternalconsentupdate', 'revision')


        # Changing field 'MaternalConsentUpdate.consent_catalogue'
        db.alter_column(u'mpepu_maternal_maternalconsentupdate', 'consent_catalogue_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bhp_consent.ConsentCatalogue']))
        # Deleting field 'MaternalEnrollDem.revision'
        db.delete_column(u'mpepu_maternal_maternalenrolldem', 'revision')

        # Deleting field 'MaternalEnrollDem.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrolldem', 'report_datetime')

        # Adding field 'MaternalArvPPHistoryAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarvpphistory_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvPPHistoryAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpphistory_audit', 'revision')

        # Deleting field 'MaternalArvPPHistoryAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpphistory_audit', 'report_datetime')

        # Deleting field 'MaternalLabDelMed.revision'
        db.delete_column(u'mpepu_maternal_maternallabdelmed', 'revision')

        # Deleting field 'MaternalLabDelMed.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdelmed', 'report_datetime')

        # Deleting field 'MaternalPostReg.revision'
        db.delete_column(u'mpepu_maternal_maternalpostreg', 'revision')


        # Changing field 'MaternalPostReg.registered_subject'
        db.alter_column(u'mpepu_maternal_maternalpostreg', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True))
        # Adding field 'MaternalLocatorAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternallocator_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalLocatorAudit.revision'
        db.delete_column(u'mpepu_maternal_maternallocator_audit', 'revision')

        # Deleting field 'MaternalLocatorAudit.may_sms_follow_up'
        db.delete_column(u'mpepu_maternal_maternallocator_audit', 'may_sms_follow_up')


        # Changing field 'MaternalLocatorAudit.registered_subject'
        db.alter_column(u'mpepu_maternal_maternallocator_audit', 'registered_subject_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bhp_registration.RegisteredSubject']))
        # Deleting field 'MaternalArvPPHistory.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpphistory', 'revision')

        # Deleting field 'MaternalArvPPHistory.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpphistory', 'report_datetime')

        # Deleting field 'MaternalArvPreg.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpreg', 'revision')

        # Deleting field 'MaternalArvPreg.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpreg', 'report_datetime')

        # Deleting field 'MaternalPostFuDx.revision'
        db.delete_column(u'mpepu_maternal_maternalpostfudx', 'revision')

        # Deleting field 'MaternalPostFuDx.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalpostfudx', 'report_datetime')

        # Deleting field 'MaternalLabDelClinic.revision'
        db.delete_column(u'mpepu_maternal_maternallabdelclinic', 'revision')

        # Deleting field 'MaternalLabDelClinic.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdelclinic', 'report_datetime')

        # Deleting field 'MaternalEnrollClin.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollclin', 'revision')

        # Deleting field 'MaternalEnrollClin.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollclin', 'report_datetime')

        # Deleting field 'MaternalLabDelDxT.revision'
        db.delete_column(u'mpepu_maternal_maternallabdeldxt', 'revision')

        # Deleting field 'MaternalLabDelDxT.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdeldxt', 'report_datetime')

        # Adding field 'MaternalArvAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalarv_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalArvAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalarv_audit', 'revision')

        # Deleting field 'MaternalPostFuDxT.revision'
        db.delete_column(u'mpepu_maternal_maternalpostfudxt', 'revision')

        # Deleting field 'MaternalPostFuDxT.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalpostfudxt', 'report_datetime')


        # Changing field 'MaternalPostFuDxT.hospitalized'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt', 'hospitalized', self.gf('django.db.models.fields.CharField')(default='', max_length=3))

        # Changing field 'MaternalPostFuDxT.grade'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt', 'grade', self.gf('django.db.models.fields.IntegerField')(default='', max_length=3))

        # Changing field 'MaternalPostFuDxT.post_fu_dx'
        db.alter_column(u'mpepu_maternal_maternalpostfudxt', 'post_fu_dx', self.gf('django.db.models.fields.CharField')(default='', max_length=100))
        # Adding field 'MaternalEnrollObAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenrollob_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollObAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollob_audit', 'revision')

        # Deleting field 'MaternalEnrollObAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollob_audit', 'report_datetime')

        # Adding field 'FeedingChoiceSectionThreeAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_feedingchoicesectionthree_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'FeedingChoiceSectionThreeAudit.revision'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionthree_audit', 'revision')

        # Deleting field 'FeedingChoiceSectionThreeAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_feedingchoicesectionthree_audit', 'report_datetime')

        # Adding field 'MaternalLabDelAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternallabdel_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalLabDelAudit.revision'
        db.delete_column(u'mpepu_maternal_maternallabdel_audit', 'revision')

        # Deleting field 'MaternalLabDelAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdel_audit', 'report_datetime')

        # Deleting field 'MaternalConsent.revision'
        db.delete_column(u'mpepu_maternal_maternalconsent', 'revision')

        # Deleting field 'MaternalConsent.language'
        db.delete_column(u'mpepu_maternal_maternalconsent', 'language')


        # Changing field 'MaternalConsent.study_site'
        db.alter_column(u'mpepu_maternal_maternalconsent', 'study_site_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['bhp_variables.StudySite']))

        # Changing field 'MaternalConsent.initials'
        db.alter_column(u'mpepu_maternal_maternalconsent', 'initials', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Deleting field 'MaternalArvPost.revision'
        db.delete_column(u'mpepu_maternal_maternalarvpost', 'revision')

        # Deleting field 'MaternalArvPost.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalarvpost', 'report_datetime')

        # Adding field 'MaternalEnrollMedAudit._audit_subject_identifier'
        db.add_column('mpepu_maternal_maternalenrollmed_audit', '_audit_subject_identifier',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True),
                      keep_default=False)

        # Deleting field 'MaternalEnrollMedAudit.revision'
        db.delete_column(u'mpepu_maternal_maternalenrollmed_audit', 'revision')

        # Deleting field 'MaternalEnrollMedAudit.report_datetime'
        db.delete_column(u'mpepu_maternal_maternalenrollmed_audit', 'report_datetime')

        # Deleting field 'MaternalLocator.revision'
        db.delete_column(u'mpepu_maternal_maternallocator', 'revision')

        # Deleting field 'MaternalLocator.may_sms_follow_up'
        db.delete_column(u'mpepu_maternal_maternallocator', 'may_sms_follow_up')


        # Changing field 'MaternalLocator.registered_subject'
        db.alter_column(u'mpepu_maternal_maternallocator', 'registered_subject_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bhp_registration.RegisteredSubject'], unique=True, null=True))
        # Deleting field 'MaternalLabDel.revision'
        db.delete_column(u'mpepu_maternal_maternallabdel', 'revision')

        # Deleting field 'MaternalLabDel.report_datetime'
        db.delete_column(u'mpepu_maternal_maternallabdel', 'report_datetime')


    models = {
        'adverse_event.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory', 'db_table': "'bhp_adverse_deathcausecategory'"},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'code_lists.wcsdxadult': {
            'Meta': {'object_name': 'WcsDxAdult', 'db_table': "'bhp_code_lists_wcsdxadult'"},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'consent.consentcatalogue': {
            'Meta': {'ordering': "['name', 'version']", 'unique_together': "(('name', 'version'),)", 'object_name': 'ConsentCatalogue', 'db_table': "'bhp_consent_consentcatalogue'"},
            'add_for_app': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'consent_type': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'content_type_map': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_content_type_map.ContentTypeMap']", 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'end_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'list_for_update': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'start_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mpepu_list.chroniccond': {
            'Meta': {'object_name': 'ChronicCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.maternalbfffrisksbenefits': {
            'Meta': {'object_name': 'MaternalBfFfRisksBenefits'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_maternal.feedingchoice': {
            'Meta': {'object_name': 'FeedingChoice'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_time_feeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.feedingchoiceaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'FeedingChoiceAudit', 'db_table': "u'mpepu_maternal_feedingchoice_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_time_feeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_feedingchoice'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.feedingchoicesectionone': {
            'Meta': {'object_name': 'FeedingChoiceSectionOne'},
            'baby_weaned_age': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hiv_aware_feeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'last_baby_feeding': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.feedingchoicesectiononeaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'FeedingChoiceSectionOneAudit', 'db_table': "u'mpepu_maternal_feedingchoicesectionone_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'baby_weaned_age': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hiv_aware_feeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'last_baby_feeding': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_feedingchoicesectionone'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.feedingchoicesectionthree': {
            'Meta': {'object_name': 'FeedingChoiceSectionThree'},
            'bf_advice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'chosen_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_choice_made': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ff_advice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'risk_benefit_training': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.MaternalBfFfRisksBenefits']", 'symmetrical': 'False'}),
            'und_risk_benefit': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'undecided_feeding': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.MaternalUndecidedFeeding']", 'symmetrical': 'False'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.feedingchoicesectionthreeaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'FeedingChoiceSectionThreeAudit', 'db_table': "u'mpepu_maternal_feedingchoicesectionthree_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bf_advice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'chosen_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_choice_made': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'ff_advice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_feedingchoicesectionthree'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'und_risk_benefit': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.feedingchoicesectiontwo': {
            'Meta': {'object_name': 'FeedingChoiceSectionTwo'},
            'baby_bf_choice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'bf_ff_benefits': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'bf_hiv_arv': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'bf_hiv_worry': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'death_worry': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'disclose_hiv_father': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'doc_feeding_advice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hiv_worry': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_hiv_risk': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'influential_people': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.MaternalFeedingInfluence']", 'symmetrical': 'False'}),
            'influential_people_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'outside_disclosure': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'safe_ff': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'status_disclosure': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'work_influence': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'work_return': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'mpepu_maternal.feedingchoicesectiontwoaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'FeedingChoiceSectionTwoAudit', 'db_table': "u'mpepu_maternal_feedingchoicesectiontwo_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'baby_bf_choice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'bf_ff_benefits': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'bf_hiv_arv': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'bf_hiv_worry': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'death_worry': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'disclose_hiv_father': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'doc_feeding_advice': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hiv_worry': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'infant_hiv_risk': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'influential_people_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_feedingchoicesectiontwo'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'outside_disclosure': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'safe_ff': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'status_disclosure': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'work_influence': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'work_return': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'mpepu_maternal.maternalarv': {
            'Meta': {'object_name': 'MaternalArv'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_stop': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_pp_history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPPHistory']", 'null': 'True', 'blank': 'True'}),
            'maternal_arv_preg_history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPregHistory']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'transaction_flag': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvAudit', 'db_table': "u'mpepu_maternal_maternalarv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_stop': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_arv_pp_history': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternalarv'", 'null': 'True', 'to': "orm['mpepu_maternal.MaternalArvPPHistory']"}),
            'maternal_arv_preg_history': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternalarv'", 'null': 'True', 'to': "orm['mpepu_maternal.MaternalArvPregHistory']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'transaction_flag': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpost': {
            'Meta': {'object_name': 'MaternalArvPost'},
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_last_visit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'haart_reason': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'haart_reason_other': ('django.db.models.fields.TextField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpostadh': {
            'Meta': {'object_name': 'MaternalArvPostAdh'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_post': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalArvPost']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'missed_days': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_days_discnt': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_doses': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpostadhaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPostAdhAudit', 'db_table': "u'mpepu_maternal_maternalarvpostadh_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_arv_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpostadh'", 'to': "orm['mpepu_maternal.MaternalArvPost']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpostadh'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'missed_days': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_days_discnt': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_doses': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpostaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPostAudit', 'db_table': "u'mpepu_maternal_maternalarvpost_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_last_visit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'haart_reason': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'haart_reason_other': ('django.db.models.fields.TextField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpost'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpostmod': {
            'Meta': {'unique_together': "(('maternal_arv_post', 'arv_code', 'modification_date'),)", 'object_name': 'MaternalArvPostMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPost']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpostmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPostModAudit', 'db_table': "u'mpepu_maternal_maternalarvpostmod_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_arv_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpostmod'", 'to': "orm['mpepu_maternal.MaternalArvPost']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpphistory': {
            'Meta': {'object_name': 'MaternalArvPPHistory'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpphistoryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPPHistoryAudit', 'db_table': "u'mpepu_maternal_maternalarvpphistory_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpphistory'", 'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpphistory'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpreg': {
            'Meta': {'object_name': 'MaternalArvPreg'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sd_nvp': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_pp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'took_arv': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpregaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPregAudit', 'db_table': "u'mpepu_maternal_maternalarvpreg_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpreg'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'sd_nvp': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_pp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'took_arv': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpreghistory': {
            'Meta': {'object_name': 'MaternalArvPregHistory'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'interrupt': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'interrupt_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'is_interrupt': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalarvpreghistoryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPregHistoryAudit', 'db_table': "u'mpepu_maternal_maternalarvpreghistory_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'interrupt': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'interrupt_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'is_interrupt': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpreghistory'", 'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpreghistory'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalconsent': {
            'Meta': {'object_name': 'MaternalConsent'},
            'assessment_score': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'confirm_identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'consent_copy': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'consent_reviewed': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'consent_version_on_entry': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'consent_version_recent': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'is_incarcerated': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '3'}),
            'is_literate': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '3'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'not specified'", 'max_length': '25'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_questions': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'subject_identifier_as_pk': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'witness_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_maternal.maternalconsentaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalConsentAudit', 'db_table': "u'mpepu_maternal_maternalconsent_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'assessment_score': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'confirm_identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'consent_copy': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'consent_reviewed': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'consent_version_on_entry': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'consent_version_recent': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'is_incarcerated': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '3'}),
            'is_literate': ('django.db.models.fields.CharField', [], {'default': "'-'", 'max_length': '3'}),
            'is_verified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_verified_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'not specified'", 'max_length': '25'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_questions': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalconsent'", 'null': 'True', 'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'blank': 'True'}),
            'subject_identifier_as_pk': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'witness_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_maternal.maternalconsentupdate': {
            'Meta': {'unique_together': "(('maternal_consent', 'consent_version'), ('maternal_consent', 'consent_datetime'))", 'object_name': 'MaternalConsentUpdate'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'consent_catalogue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['consent.ConsentCatalogue']"}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'consent_version': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_consent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalConsent']"}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaldeath': {
            'Meta': {'object_name': 'MaternalDeath'},
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
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['code_lists.DxCode']", 'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaldeathaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalDeathAudit', 'db_table': "u'mpepu_maternal_maternaldeath_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['adverse_event.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['adverse_event.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['adverse_event.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternaldeath'", 'null': 'True', 'to': "orm['adverse_event.DeathReasonHospitalized']"}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'max_length': '25', 'to': "orm['code_lists.DxCode']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaleligibilityante': {
            'Meta': {'object_name': 'MaternalEligibilityAnte'},
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'gestational_age': ('django.db.models.fields.IntegerField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_cd4_low': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalConsent']", 'unique': 'True'}),
            'maternal_haart': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaleligibilityanteaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEligibilityAnteAudit', 'db_table': "u'mpepu_maternal_maternaleligibilityante_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'gestational_age': ('django.db.models.fields.IntegerField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_cd4_low': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilityante'", 'to': "orm['mpepu_maternal.MaternalConsent']"}),
            'maternal_haart': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilityante'", 'to': "orm['registration.RegisteredSubject']"}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaleligibilitypost': {
            'Meta': {'object_name': 'MaternalEligibilityPost'},
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_pnc': ('django.db.models.fields.IntegerField', [], {}),
            'feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_cd4_low': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalConsent']", 'unique': 'True'}),
            'maternal_haart': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaleligibilitypostaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEligibilityPostAudit', 'db_table': "u'mpepu_maternal_maternaleligibilitypost_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_pnc': ('django.db.models.fields.IntegerField', [], {}),
            'feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_cd4_low': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilitypost'", 'to': "orm['mpepu_maternal.MaternalConsent']"}),
            'maternal_haart': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilitypost'", 'to': "orm['registration.RegisteredSubject']"}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenroll': {
            'Meta': {'object_name': 'MaternalEnroll'},
            'bp': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_pregnancies': ('django.db.models.fields.IntegerField', [], {}),
            'prev_pregnancy_arv': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_health_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'recruit_source': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'recruit_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'recruitment_clinic': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recruitment_clinic_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'mpepu_maternal.maternalenrollarv': {
            'Meta': {'object_name': 'MaternalEnrollArv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_changes': ('django.db.models.fields.IntegerField', [], {}),
            'haart_start_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'preg_on_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_arv': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.PriorArv']", 'symmetrical': 'False'}),
            'prior_arv_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'prior_preg': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrollarvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollArvAudit', 'db_table': "u'mpepu_maternal_maternalenrollarv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_changes': ('django.db.models.fields.IntegerField', [], {}),
            'haart_start_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollarv'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollarv'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'preg_on_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_arv_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'prior_preg': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrollaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollAudit', 'db_table': "u'mpepu_maternal_maternalenroll_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bp': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenroll'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_pregnancies': ('django.db.models.fields.IntegerField', [], {}),
            'prev_pregnancy_arv': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_health_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'recruit_source': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'recruit_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'recruitment_clinic': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'recruitment_clinic_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'mpepu_maternal.maternalenrollclin': {
            'Meta': {'object_name': 'MaternalEnrollClin'},
            'cd4_count': ('django.db.models.fields.IntegerField', [], {}),
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_preg_azt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_preg_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_sdnvp_labour': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrollclinaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollClinAudit', 'db_table': "u'mpepu_maternal_maternalenrollclin_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cd4_count': ('django.db.models.fields.IntegerField', [], {}),
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollclin'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollclin'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_preg_azt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_preg_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_sdnvp_labour': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrolldem': {
            'Meta': {'object_name': 'MaternalEnrollDem'},
            'cooking_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'current_occupation': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'current_occupation_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ethnicity_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'hh_goods': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.HhGoods']", 'symmetrical': 'False'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'house_electrified': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_fridge': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_people_number': ('django.db.models.fields.IntegerField', [], {}),
            'house_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'know_hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'marital_status_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'money_earned': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'money_earned_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'own_phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'provides_money': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'provides_money_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'toilet_facility': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toilet_facility_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'water_source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'mpepu_maternal.maternalenrolldemaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollDemAudit', 'db_table': "u'mpepu_maternal_maternalenrolldem_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cooking_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'current_occupation': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'current_occupation_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ethnicity_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'house_electrified': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_fridge': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_people_number': ('django.db.models.fields.IntegerField', [], {}),
            'house_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'know_hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'marital_status_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrolldem'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrolldem'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'money_earned': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'money_earned_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'own_phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'provides_money': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'provides_money_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'toilet_facility': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toilet_facility_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'water_source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'mpepu_maternal.maternalenrolldx': {
            'Meta': {'object_name': 'MaternalEnrollDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'diagnosis_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_enroll_med': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalEnrollMed']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrolldxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollDxAudit', 'db_table': "u'mpepu_maternal_maternalenrolldx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'diagnosis_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_enroll_med': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrolldx'", 'to': "orm['mpepu_maternal.MaternalEnrollMed']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrollmed': {
            'Meta': {'object_name': 'MaternalEnrollMed'},
            'chronic_cond': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.ChronicCond']", 'symmetrical': 'False'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_maternal.maternalenrollmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollMedAudit', 'db_table': "u'mpepu_maternal_maternalenrollmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollmed'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollmed'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_maternal.maternalenrollob': {
            'Meta': {'object_name': 'MaternalEnrollOb'},
            'children_died_b4_5yrs': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'live_children': ('django.db.models.fields.IntegerField', [], {}),
            'lost_after_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'lost_before_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pregs_24wks_or_more': ('django.db.models.fields.IntegerField', [], {}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalenrollobaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollObAudit', 'db_table': "u'mpepu_maternal_maternalenrollob_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'children_died_b4_5yrs': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'live_children': ('django.db.models.fields.IntegerField', [], {}),
            'lost_after_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'lost_before_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollob'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollob'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pregs_24wks_or_more': ('django.db.models.fields.IntegerField', [], {}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'labour_hrs': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'labr_max_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'live_infants': ('django.db.models.fields.IntegerField', [], {}),
            'live_infants_to_register': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'still_born_congen_abn': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'still_born_has_congen_abn': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'still_borns': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallabdelaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelAudit', 'db_table': "u'mpepu_maternal_maternallabdel_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'del_comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'labour_hrs': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'labr_max_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'live_infants': ('django.db.models.fields.IntegerField', [], {}),
            'live_infants_to_register': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdel'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'still_born_congen_abn': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'still_born_has_congen_abn': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'still_borns': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallabdelclinic': {
            'Meta': {'object_name': 'MaternalLabDelClinic'},
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cd4_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_vl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalLabDel']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'suppliment': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.Suppliment']", 'symmetrical': 'False'}),
            'took_suppliments': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vl_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_maternal.maternallabdelclinicaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelClinicAudit', 'db_table': "u'mpepu_maternal_maternallabdelclinic_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cd4_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_vl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelclinic'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelclinic'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'took_suppliments': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vl_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_maternal.maternallabdeldx': {
            'Meta': {'object_name': 'MaternalLabDelDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_preg_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_who_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalLabDel']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'wcs_dx_adult': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['code_lists.WcsDxAdult']", 'symmetrical': 'False'})
        },
        'mpepu_maternal.maternallabdeldxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelDxAudit', 'db_table': "u'mpepu_maternal_maternallabdeldx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_preg_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_who_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdeldx'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdeldx'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallabdeldxt': {
            'Meta': {'object_name': 'MaternalLabDelDxT'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lab_del_dx': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lab_del_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'maternal_lab_del_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalLabDelDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallabdeldxtaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelDxTAudit', 'db_table': "u'mpepu_maternal_maternallabdeldxt_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'lab_del_dx': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lab_del_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'maternal_lab_del_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdeldxt'", 'to': "orm['mpepu_maternal.MaternalLabDelDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallabdelmed': {
            'Meta': {'object_name': 'MaternalLabDelMed'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_health_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_ob_comp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_cond': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.HealthCond']", 'symmetrical': 'False'}),
            'health_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalLabDel']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ob_comp': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.ObComp']", 'symmetrical': 'False'}),
            'ob_comp_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallabdelmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelMedAudit', 'db_table': "u'mpepu_maternal_maternallabdelmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_health_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_ob_comp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelmed'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelmed'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ob_comp_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallocator': {
            'Meta': {'object_name': 'MaternalLocator'},
            'care_clinic': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'caretaker_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'caretaker_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'caretaker_tel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'has_caretaker_alt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_sms_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True', 'null': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternallocatoraudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLocatorAudit', 'db_table': "u'mpepu_maternal_maternallocator_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'care_clinic': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'caretaker_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'caretaker_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'caretaker_tel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'contact_physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'contact_rel': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'has_caretaker_alt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallocator'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_sms_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallocator'", 'null': 'True', 'to': "orm['registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaloffstudy': {
            'Meta': {'object_name': 'MaternalOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_scheduled_data': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternaloffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalOffStudyAudit', 'db_table': "u'mpepu_maternal_maternaloffstudy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_scheduled_data': ('django.db.models.fields.CharField', [], {'default': "'Yes'", 'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaloffstudy'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalpostfu': {
            'Meta': {'object_name': 'MaternalPostFu'},
            'breastfeeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'chronic_cond': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.ChronicCond']", 'symmetrical': 'False'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'enter_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'had_mastitis': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_weight': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'started_ctx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalpostfuaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostFuAudit', 'db_table': "u'mpepu_maternal_maternalpostfu_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'breastfeeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'enter_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'had_mastitis': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfu'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_weight': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'started_ctx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalpostfudx': {
            'Meta': {'object_name': 'MaternalPostFuDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_post_fu': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalPostFu']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'new_diagnoses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'wcs_dx_adult': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['code_lists.WcsDxAdult']", 'symmetrical': 'False'}),
            'who_clinical_stage': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_maternal.maternalpostfudxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostFuDxAudit', 'db_table': "u'mpepu_maternal_maternalpostfudx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_post_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfudx'", 'to': "orm['mpepu_maternal.MaternalPostFu']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfudx'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'new_diagnoses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_clinical_stage': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_maternal.maternalpostfudxt': {
            'Meta': {'object_name': 'MaternalPostFuDxT'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_post_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalPostFuDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_fu_specify': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalpostfudxtaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostFuDxTAudit', 'db_table': "u'mpepu_maternal_maternalpostfudxt_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_post_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfudxt'", 'to': "orm['mpepu_maternal.MaternalPostFuDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_fu_specify': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalpostreg': {
            'Meta': {'object_name': 'MaternalPostReg'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reg_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['registration.RegisteredSubject']", 'unique': 'True'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalpostregaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostRegAudit', 'db_table': "u'mpepu_maternal_maternalpostreg_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reg_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostreg'", 'to': "orm['registration.RegisteredSubject']"}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalvisit': {
            'Meta': {'object_name': 'MaternalVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.maternalvisitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalVisitAudit', 'db_table': "'mpepu_maternal_maternalvisit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalvisit'", 'to': "orm['appointment.Appointment']"}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.postnatalinfantfeedingsurvey': {
            'Meta': {'object_name': 'PostNatalInfantFeedingSurvey'},
            'correct_bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'feeding_period': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'feeding_satisfaction': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalVisit']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'next_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_maternal.postnatalinfantfeedingsurveyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'PostNatalInfantFeedingSurveyAudit', 'db_table': "u'mpepu_maternal_postnatalinfantfeedingsurvey_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'correct_bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_duration': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'feeding_period': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'feeding_satisfaction': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_postnatalinfantfeedingsurvey'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'next_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 2, 12, 0, 0)'}),
            'revision': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '25', 'unique': 'True', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'silverapple'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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

    complete_apps = ['mpepu_maternal']