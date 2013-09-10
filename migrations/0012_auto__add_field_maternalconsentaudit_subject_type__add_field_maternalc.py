# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'MaternalConsent', fields ['subject_identifier']
        #db.delete_unique('mpepu_maternal_maternalconsent', ['subject_identifier'])

#        # Adding index on 'MaternalEnrollDemAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrolldem_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollDemAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrolldem_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPregHistoryAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpreghistory_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPregHistoryAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpreghistory_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPregAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpreg_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPregAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpreg_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalVisit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalvisit', ['hostname_created'])
#
#        # Adding index on 'MaternalVisit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalvisit', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelMed', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdelmed', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelMed', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdelmed', ['hostname_modified'])
#
        # Adding field 'MaternalConsentAudit.subject_type'
        #db.add_column('mpepu_maternal_maternalconsent_audit', 'subject_type',
        #              self.gf('django.db.models.fields.CharField')(default='undetermined', max_length=25),
        #              keep_default=False)

        # Adding field 'MaternalConsentAudit.screening_datetime'
        #db.add_column('mpepu_maternal_maternalconsent_audit', 'screening_datetime',
        #              self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
        #              keep_default=False)

        # Adding field 'MaternalConsentAudit.registration_datetime'
        #db.add_column('mpepu_maternal_maternalconsent_audit', 'registration_datetime',
        #              self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
        #              keep_default=False)

        # Adding field 'MaternalConsentAudit.randomization_datetime'
        #db.add_column('mpepu_maternal_maternalconsent_audit', 'randomization_datetime',
        #              self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
        #              keep_default=False)

        # Adding field 'MaternalConsentAudit.registration_status'
        #db.add_column('mpepu_maternal_maternalconsent_audit', 'registration_status',
        #              self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True),
        #              keep_default=False)

        # Adding index on 'MaternalConsentAudit', fields ['hostname_created']
        #db.create_index('mpepu_maternal_maternalconsent_audit', ['hostname_created'])


        # Changing field 'MaternalConsentAudit.last_name'
#        db.alter_column('mpepu_maternal_maternalconsent_audit', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))
        # Adding index on 'MaternalConsentAudit', fields ['hostname_modified']
        #db.create_index('mpepu_maternal_maternalconsent_audit', ['hostname_modified'])


        # Changing field 'MaternalConsentAudit.first_name'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalConsentAudit.is_dob_estimated'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'is_dob_estimated', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))

        # Changing field 'MaternalConsentAudit.subject_identifier'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=36, null=True))
        # Adding index on 'MaternalConsentAudit', fields ['subject_identifier']
        #db.create_index('mpepu_maternal_maternalconsent_audit', ['subject_identifier'])


        # Changing field 'MaternalConsentAudit.identity'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'identity', self.gf('django.db.models.fields.CharField')(max_length=78L))

        # Changing field 'MaternalConsentAudit.gender'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'MaternalConsentAudit.dob'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'dob', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'MaternalConsentAudit.guardian_name'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'guardian_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalConsentAudit.initials'
        db.alter_column('mpepu_maternal_maternalconsent_audit', 'initials', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
#        # Adding index on 'MaternalVisitAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalvisit_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalVisitAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalvisit_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalArv', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarv', ['hostname_created'])
#
#        # Adding index on 'MaternalArv', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarv', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollArv', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollarv', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollArv', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollarv', ['hostname_modified'])
#
#        # Adding index on 'MaternalDeathAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaldeath_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalDeathAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaldeath_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostFuAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostfu_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalPostFuAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostfu_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalOffStudy', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaloffstudy', ['hostname_created'])
#
#        # Adding index on 'MaternalOffStudy', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaloffstudy', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelDx', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdeldx', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelDx', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdeldx', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPregHistory', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpreghistory', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPregHistory', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpreghistory', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPostAdh', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpostadh', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPostAdh', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpostadh', ['hostname_modified'])
#
#        # Adding index on 'MaternalEligibilityPostAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaleligibilitypost_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEligibilityPostAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaleligibilitypost_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollOb', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollob', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollOb', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollob', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPostAdhAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpostadh_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPostAdhAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpostadh_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalEligibilityAnteAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaleligibilityante_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEligibilityAnteAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaleligibilityante_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelDxTAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdeldxt_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelDxTAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdeldxt_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenroll_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenroll_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPostMod', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpostmod', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPostMod', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpostmod', ['hostname_created'])
#
#        # Adding index on 'MaternalOffStudyAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaloffstudy_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalOffStudyAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaloffstudy_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelMedAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdelmed_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelMedAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdelmed_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelDxAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdeldx_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelDxAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdeldx_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalDeath', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaldeath', ['hostname_created'])
#
#        # Adding index on 'MaternalDeath', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaldeath', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollClinAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollclin_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollClinAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollclin_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPostModAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpostmod_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPostModAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpostmod_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelClinicAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdelclinic_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelClinicAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdelclinic_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollDx', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrolldx', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollDx', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrolldx', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollDxAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrolldx_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollDxAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrolldx_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostRegAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostreg_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalPostRegAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostreg_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPostAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpost_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPostAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpost_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnroll', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenroll', ['hostname_created'])
#
#        # Adding index on 'MaternalEnroll', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenroll', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollMed', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollmed', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollMed', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollmed', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollArvAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollarv_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollArvAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollarv_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostFu', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostfu', ['hostname_created'])
#
#        # Adding index on 'MaternalPostFu', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostfu', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostFuDxTAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostfudxt_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalPostFuDxTAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostfudxt_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostFuDxAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostfudx_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalPostFuDxAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostfudx_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalEligibilityPost', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaleligibilitypost', ['hostname_modified'])
#
#        # Adding index on 'MaternalEligibilityPost', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaleligibilitypost', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollDem', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrolldem', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollDem', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrolldem', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPPHistoryAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpphistory_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPPHistoryAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpphistory_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostReg', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostreg', ['hostname_created'])
#
#        # Adding index on 'MaternalPostReg', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostreg', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvPPHistory', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpphistory', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPPHistory', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpphistory', ['hostname_modified'])
#
        # Adding field 'MaternalLocatorAudit.report_datetime'
#        db.add_column('mpepu_maternal_maternallocator_audit', 'report_datetime',
#                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 29, 0, 0)),
#                      keep_default=False)

#        # Adding index on 'MaternalLocatorAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallocator_audit', ['hostname_created'])

        # Changing field 'MaternalLocatorAudit.contact_physical_address'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'contact_physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))
#        # Adding index on 'MaternalLocatorAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallocator_audit', ['hostname_modified'])

        # Changing field 'MaternalLocatorAudit.subject_work_phone'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'subject_work_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.contact_name'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.contact_rel'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'contact_rel', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.caretaker_cell'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'caretaker_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.contact_phone'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.physical_address'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'MaternalLocatorAudit.subject_cell_alt'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'subject_cell_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.subject_phone_alt'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'subject_phone_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.contact_cell'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'contact_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.subject_cell'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'subject_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.subject_work_place'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'subject_work_place', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'MaternalLocatorAudit.caretaker_name'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'caretaker_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.mail_address'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'mail_address', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'MaternalLocatorAudit.subject_phone'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'subject_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocatorAudit.caretaker_tel'
        db.alter_column('mpepu_maternal_maternallocator_audit', 'caretaker_tel', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))
#        # Adding index on 'MaternalArvPreg', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarvpreg', ['hostname_created'])
#
#        # Adding index on 'MaternalArvPreg', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpreg', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostFuDx', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostfudx', ['hostname_created'])
#
#        # Adding index on 'MaternalPostFuDx', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostfudx', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelClinic', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdelclinic', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelClinic', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdelclinic', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollClin', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollclin', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollClin', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollclin', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelDxT', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdeldxt', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelDxT', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdeldxt', ['hostname_modified'])
#
#        # Adding index on 'MaternalArvAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalarv_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalArvAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarv_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalPostFuDxT', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalpostfudxt', ['hostname_created'])
#
#        # Adding index on 'MaternalPostFuDxT', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalpostfudxt', ['hostname_modified'])
#
#        # Adding index on 'MaternalEligibilityAnte', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternaleligibilityante', ['hostname_created'])
#
#        # Adding index on 'MaternalEligibilityAnte', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternaleligibilityante', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollObAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollob_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollObAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollob_audit', ['hostname_modified'])
#
#        # Adding index on 'MaternalLabDelAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdel_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDelAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdel_audit', ['hostname_modified'])

        # Adding field 'MaternalConsent.subject_type'
        #db.add_column('mpepu_maternal_maternalconsent', 'subject_type',
        #              self.gf('django.db.models.fields.CharField')(default='undetermined', max_length=25),
        #              keep_default=False)

        # Adding field 'MaternalConsent.screening_datetime'
        #db.add_column('mpepu_maternal_maternalconsent', 'screening_datetime',
        #              self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
        #              keep_default=False)

        # Adding field 'MaternalConsent.registration_datetime'
        #db.add_column('mpepu_maternal_maternalconsent', 'registration_datetime',
        #              self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
        #              keep_default=False)

        # Adding field 'MaternalConsent.randomization_datetime'
        #db.add_column('mpepu_maternal_maternalconsent', 'randomization_datetime',
        #              self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
        #              keep_default=False)

        # Adding field 'MaternalConsent.registration_status'
        #db.add_column('mpepu_maternal_maternalconsent', 'registration_status',
        #              self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True),
        #              keep_default=False)

        # Changing field 'MaternalConsent.guardian_name'
        db.alter_column('mpepu_maternal_maternalconsent', 'guardian_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))
        # Adding index on 'MaternalConsent', fields ['hostname_created']
        #db.create_index('mpepu_maternal_maternalconsent', ['hostname_created'])

        # Changing field 'MaternalConsent.last_name'
        db.alter_column('mpepu_maternal_maternalconsent', 'last_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalConsent.is_dob_estimated'
        db.alter_column('mpepu_maternal_maternalconsent', 'is_dob_estimated', self.gf('django.db.models.fields.CharField')(max_length=25, null=True))
        # Adding index on 'MaternalConsent', fields ['hostname_modified']
        #db.create_index('mpepu_maternal_maternalconsent', ['hostname_modified'])


        # Changing field 'MaternalConsent.dob'
        db.alter_column('mpepu_maternal_maternalconsent', 'dob', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'MaternalConsent.first_name'
        db.alter_column('mpepu_maternal_maternalconsent', 'first_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalConsent.identity'
        db.alter_column('mpepu_maternal_maternalconsent', 'identity', self.gf('django.db.models.fields.CharField')(unique=True, max_length=78L))

        # Changing field 'MaternalConsent.gender'
        db.alter_column('mpepu_maternal_maternalconsent', 'gender', self.gf('django.db.models.fields.CharField')(max_length=1, null=True))

        # Changing field 'MaternalConsent.subject_identifier'
        db.alter_column('mpepu_maternal_maternalconsent', 'subject_identifier', self.gf('django.db.models.fields.CharField')(max_length=36, null=True))
        # Adding index on 'MaternalConsent', fields ['subject_identifier']
#        db.create_index('mpepu_maternal_maternalconsent', ['subject_identifier'])


        # Changing field 'MaternalConsent.initials'
        db.alter_column('mpepu_maternal_maternalconsent', 'initials', self.gf('django.db.models.fields.CharField')(max_length=3, null=True))
        # Adding index on 'MaternalArvPost', fields ['hostname_created']
        #db.create_index('mpepu_maternal_maternalarvpost', ['hostname_created'])

#        # Adding index on 'MaternalArvPost', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalarvpost', ['hostname_modified'])
#
#        # Adding index on 'MaternalEnrollMedAudit', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternalenrollmed_audit', ['hostname_created'])
#
#        # Adding index on 'MaternalEnrollMedAudit', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternalenrollmed_audit', ['hostname_modified'])

        # Adding field 'MaternalLocator.report_datetime'
 #       db.add_column('mpepu_maternal_maternallocator', 'report_datetime',
 #                     self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 29, 0, 0)),
 #                     keep_default=False)

        # Adding index on 'MaternalLocator', fields ['hostname_created']
        #db.create_index('mpepu_maternal_maternallocator', ['hostname_created'])


        # Changing field 'MaternalLocator.contact_physical_address'
        db.alter_column('mpepu_maternal_maternallocator', 'contact_physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))
        # Adding index on 'MaternalLocator', fields ['hostname_modified']
        #db.create_index('mpepu_maternal_maternallocator', ['hostname_modified'])


        # Changing field 'MaternalLocator.subject_work_phone'
        db.alter_column('mpepu_maternal_maternallocator', 'subject_work_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.contact_name'
        db.alter_column('mpepu_maternal_maternallocator', 'contact_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.contact_rel'
        db.alter_column('mpepu_maternal_maternallocator', 'contact_rel', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.caretaker_cell'
        db.alter_column('mpepu_maternal_maternallocator', 'caretaker_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.contact_phone'
        db.alter_column('mpepu_maternal_maternallocator', 'contact_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.physical_address'
        db.alter_column('mpepu_maternal_maternallocator', 'physical_address', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'MaternalLocator.subject_cell_alt'
        db.alter_column('mpepu_maternal_maternallocator', 'subject_cell_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.subject_phone_alt'
        db.alter_column('mpepu_maternal_maternallocator', 'subject_phone_alt', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.contact_cell'
        db.alter_column('mpepu_maternal_maternallocator', 'contact_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.mail_address'
        db.alter_column('mpepu_maternal_maternallocator', 'mail_address', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'MaternalLocator.subject_cell'
        db.alter_column('mpepu_maternal_maternallocator', 'subject_cell', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.subject_work_place'
        db.alter_column('mpepu_maternal_maternallocator', 'subject_work_place', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'MaternalLocator.caretaker_name'
        db.alter_column('mpepu_maternal_maternallocator', 'caretaker_name', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.subject_phone'
        db.alter_column('mpepu_maternal_maternallocator', 'subject_phone', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))

        # Changing field 'MaternalLocator.caretaker_tel'
        db.alter_column('mpepu_maternal_maternallocator', 'caretaker_tel', self.gf('django.db.models.fields.CharField')(max_length=78L, null=True))
#        # Adding index on 'MaternalLabDel', fields ['hostname_created']
#        db.create_index('mpepu_maternal_maternallabdel', ['hostname_created'])
#
#        # Adding index on 'MaternalLabDel', fields ['hostname_modified']
#        db.create_index('mpepu_maternal_maternallabdel', ['hostname_modified'])

    def backwards(self, orm):
        pass

    models = {
        'bhp_adverse.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'object_name': 'Appointment', 'db_table': "'bhp_form_appointment'"},
            'appt_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'appt_reason': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'appt_status': ('django.db.models.fields.CharField', [], {'default': "'new'", 'max_length': '25'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_tel': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dashboard_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'timepoint_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_visit.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        'bhp_code_lists.dxcode': {
            'Meta': {'object_name': 'DxCode'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_code_lists.wcsdxadult': {
            'Meta': {'object_name': 'WcsDxAdult'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_content_type_map.contenttypemap': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap', 'db_table': "'bhp_common_contenttypemap'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'object_name': 'RegisteredSubject'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'default': "'?'", 'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_identifier': ('django.db.models.fields.CharField', [], {'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'relative_identifier': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'salt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'sid': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True', 'blank': 'True'}),
            'subject_consent_id': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'bhp_visit.membershipform': {
            'Meta': {'object_name': 'MembershipForm', 'db_table': "'bhp_form_membershipform'"},
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '25', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'bhp_visit.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup', 'db_table': "'bhp_form_schedulegroup'"},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
        'mpepu_list.chroniccond': {
            'Meta': {'object_name': 'ChronicCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.delcomp': {
            'Meta': {'object_name': 'DelComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.healthcond': {
            'Meta': {'object_name': 'HealthCond'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.hhgoods': {
            'Meta': {'object_name': 'HhGoods'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.obcomp': {
            'Meta': {'object_name': 'ObComp'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.priorarv': {
            'Meta': {'object_name': 'PriorArv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_list.suppliment': {
            'Meta': {'object_name': 'Suppliment'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'mpepu_maternal.maternalarv': {
            'Meta': {'object_name': 'MaternalArv'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_stop': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_pp_history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPPHistory']", 'null': 'True', 'blank': 'True'}),
            'maternal_arv_preg_history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPregHistory']", 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'transaction_flag': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvAudit', 'db_table': "'mpepu_maternal_maternalarv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_stop': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_arv_pp_history': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternalarv'", 'null': 'True', 'to': "orm['mpepu_maternal.MaternalArvPPHistory']"}),
            'maternal_arv_preg_history': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternalarv'", 'null': 'True', 'to': "orm['mpepu_maternal.MaternalArvPregHistory']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'transaction_flag': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpost': {
            'Meta': {'object_name': 'MaternalArvPost'},
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_last_visit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'haart_reason': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'haart_reason_other': ('django.db.models.fields.TextField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpostadh': {
            'Meta': {'object_name': 'MaternalArvPostAdh'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_post': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalArvPost']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'missed_days': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_days_discnt': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_doses': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpostadhaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPostAdhAudit', 'db_table': "'mpepu_maternal_maternalarvpostadh_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_arv_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpostadh'", 'to': "orm['mpepu_maternal.MaternalArvPost']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpostadh'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'missed_days': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_days_discnt': ('django.db.models.fields.IntegerField', [], {'default': "'0'"}),
            'missed_doses': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpostaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPostAudit', 'db_table': "'mpepu_maternal_maternalarvpost_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_last_visit': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'haart_reason': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'haart_reason_other': ('django.db.models.fields.TextField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpost'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpostmod': {
            'Meta': {'object_name': 'MaternalArvPostMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_post': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPost']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpostmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPostModAudit', 'db_table': "'mpepu_maternal_maternalarvpostmod_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_arv_post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpostmod'", 'to': "orm['mpepu_maternal.MaternalArvPost']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpphistory': {
            'Meta': {'object_name': 'MaternalArvPPHistory'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpphistoryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPPHistoryAudit', 'db_table': "'mpepu_maternal_maternalarvpphistory_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpphistory'", 'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpphistory'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpreg': {
            'Meta': {'object_name': 'MaternalArvPreg'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'sd_nvp': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_pp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'took_arv': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpregaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPregAudit', 'db_table': "'mpepu_maternal_maternalarvpreg_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpreg'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'sd_nvp': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'start_pp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'took_arv': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpreghistory': {
            'Meta': {'object_name': 'MaternalArvPregHistory'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'interrupt': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'interrupt_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'is_interrupt': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalarvpreghistoryaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalArvPregHistoryAudit', 'db_table': "'mpepu_maternal_maternalarvpreghistory_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'interrupt': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'interrupt_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'is_interrupt': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_arv_preg': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpreghistory'", 'to': "orm['mpepu_maternal.MaternalArvPreg']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalarvpreghistory'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalconsent': {
            'Meta': {'object_name': 'MaternalConsent'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalconsentaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalConsentAudit', 'db_table': "'mpepu_maternal_maternalconsent_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'consent_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True'}),
            'guardian_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'identity_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True'}),
            'is_dob_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True'}),
            'may_store_samples': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'randomization_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'registration_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'screening_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalconsent'", 'to': "orm['bhp_variables.StudySite']"}),
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '36', 'null': 'True', 'blank': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaldeath': {
            'Meta': {'object_name': 'MaternalDeath'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathReasonHospitalized']", 'null': 'True', 'blank': 'True'}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_code_lists.DxCode']", 'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaldeathaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalDeathAudit', 'db_table': "'mpepu_maternal_maternaldeath_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_maternaldeath'", 'null': 'True', 'to': "orm['bhp_adverse.DeathReasonHospitalized']"}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'max_length': '25', 'to': "orm['bhp_code_lists.DxCode']"}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaldeath'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaleligibilityante': {
            'Meta': {'object_name': 'MaternalEligibilityAnte'},
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'gestational_age': ('django.db.models.fields.IntegerField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalConsent']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaleligibilityanteaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEligibilityAnteAudit', 'db_table': "'mpepu_maternal_maternaleligibilityante_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'gestational_age': ('django.db.models.fields.IntegerField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilityante'", 'to': "orm['mpepu_maternal.MaternalConsent']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilityante'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaleligibilitypost': {
            'Meta': {'object_name': 'MaternalEligibilityPost'},
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_pnc': ('django.db.models.fields.IntegerField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalConsent']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaleligibilitypostaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEligibilityPostAudit', 'db_table': "'mpepu_maternal_maternaleligibilitypost_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'agree_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_pnc': ('django.db.models.fields.IntegerField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'is_hiv_positive': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_consent': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilitypost'", 'to': "orm['mpepu_maternal.MaternalConsent']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaleligibilitypost'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'registration_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenroll': {
            'Meta': {'object_name': 'MaternalEnroll'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_pregnancies': ('django.db.models.fields.IntegerField', [], {}),
            'prev_pregnancy_arv': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_health_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'recruit_source': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'recruit_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'mpepu_maternal.maternalenrollarv': {
            'Meta': {'object_name': 'MaternalEnrollArv'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_changes': ('django.db.models.fields.IntegerField', [], {}),
            'haart_start_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'preg_on_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_arv': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.PriorArv']", 'symmetrical': 'False'}),
            'prior_arv_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'prior_preg': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenrollarvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollArvAudit', 'db_table': "'mpepu_maternal_maternalenrollarv_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'haart_changes': ('django.db.models.fields.IntegerField', [], {}),
            'haart_start_date': ('django.db.models.fields.DateField', [], {}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollarv'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollarv'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'preg_on_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_arv_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'prior_preg': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenrollaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollAudit', 'db_table': "'mpepu_maternal_maternalenroll_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenroll'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_pregnancies': ('django.db.models.fields.IntegerField', [], {}),
            'prev_pregnancy_arv': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prior_health_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'recruit_source': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'recruit_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        'mpepu_maternal.maternalenrollclin': {
            'Meta': {'object_name': 'MaternalEnrollClin'},
            'cd4_count': ('django.db.models.fields.IntegerField', [], {}),
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_preg_azt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_preg_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_sdnvp_labour': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenrollclinaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollClinAudit', 'db_table': "'mpepu_maternal_maternalenrollclin_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cd4_count': ('django.db.models.fields.IntegerField', [], {}),
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'is_date_estimated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollclin'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollclin'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prev_preg_azt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_preg_haart': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'prev_sdnvp_labour': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'house_electrified': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_fridge': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_people_number': ('django.db.models.fields.IntegerField', [], {}),
            'house_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'know_hiv_status': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'marital_status_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'money_earned': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'money_earned_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'own_phone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'provides_money': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'provides_money_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'toilet_facility': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toilet_facility_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'water_source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'mpepu_maternal.maternalenrolldemaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollDemAudit', 'db_table': "'mpepu_maternal_maternalenrolldem_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cooking_method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'current_occupation': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'current_occupation_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'ethnicity_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'highest_education': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'house_electrified': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_fridge': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'house_people_number': ('django.db.models.fields.IntegerField', [], {}),
            'house_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
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
            'toilet_facility': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'toilet_facility_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'water_source': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'mpepu_maternal.maternalenrolldx': {
            'Meta': {'object_name': 'MaternalEnrollDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'diagnosis_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_enroll_med': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalEnrollMed']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenrolldxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollDxAudit', 'db_table': "'mpepu_maternal_maternalenrolldx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'diagnosis_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_enroll_med': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrolldx'", 'to': "orm['mpepu_maternal.MaternalEnrollMed']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenrollmed': {
            'Meta': {'object_name': 'MaternalEnrollMed'},
            'chronic_cond': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.ChronicCond']", 'symmetrical': 'False'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_maternal.maternalenrollmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollMedAudit', 'db_table': "'mpepu_maternal_maternalenrollmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollmed'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollmed'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_maternal.maternalenrollob': {
            'Meta': {'object_name': 'MaternalEnrollOb'},
            'children_died_b4_5yrs': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'live_children': ('django.db.models.fields.IntegerField', [], {}),
            'lost_after_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'lost_before_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_enroll': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalEnroll']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pregs_24wks_or_more': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalenrollobaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalEnrollObAudit', 'db_table': "'mpepu_maternal_maternalenrollob_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'children_died_b4_5yrs': ('django.db.models.fields.IntegerField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'live_children': ('django.db.models.fields.IntegerField', [], {}),
            'lost_after_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'lost_before_24wks': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_enroll': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollob'", 'to': "orm['mpepu_maternal.MaternalEnroll']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalenrollob'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'pregs_24wks_or_more': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
        'mpepu_maternal.maternallabdelaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelAudit', 'db_table': "'mpepu_maternal_maternallabdel_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'labour_hrs': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'labr_max_temp': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'live_infants': ('django.db.models.fields.IntegerField', [], {}),
            'live_infants_to_register': ('django.db.models.fields.IntegerField', [], {}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdel'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'still_born_congen_abn': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'still_born_has_congen_abn': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'still_borns': ('django.db.models.fields.IntegerField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternallabdelclinic': {
            'Meta': {'object_name': 'MaternalLabDelClinic'},
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cd4_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_vl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalLabDel']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'suppliment': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.Suppliment']", 'symmetrical': 'False'}),
            'took_suppliments': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vl_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_maternal.maternallabdelclinicaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelClinicAudit', 'db_table': "'mpepu_maternal_maternallabdelclinic_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'cd4_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'cd4_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_cd4': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_vl': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelclinic'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelclinic'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'took_suppliments': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'vl_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'vl_result': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'})
        },
        'mpepu_maternal.maternallabdeldx': {
            'Meta': {'object_name': 'MaternalLabDelDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_preg_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_who_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalLabDel']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'wcs_dx_adult': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_code_lists.WcsDxAdult']", 'symmetrical': 'False'})
        },
        'mpepu_maternal.maternallabdeldxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelDxAudit', 'db_table': "'mpepu_maternal_maternallabdeldx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_preg_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_who_dx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdeldx'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdeldx'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternallabdeldxt': {
            'Meta': {'object_name': 'MaternalLabDelDxT'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lab_del_dx': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lab_del_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'maternal_lab_del_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalLabDelDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternallabdeldxtaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelDxTAudit', 'db_table': "'mpepu_maternal_maternallabdeldxt_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'lab_del_dx': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lab_del_dx_specify': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'maternal_lab_del_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdeldxt'", 'to': "orm['mpepu_maternal.MaternalLabDelDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternallabdelmed': {
            'Meta': {'object_name': 'MaternalLabDelMed'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_health_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_ob_comp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_cond': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.HealthCond']", 'symmetrical': 'False'}),
            'health_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalLabDel']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ob_comp': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.ObComp']", 'symmetrical': 'False'}),
            'ob_comp_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternallabdelmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLabDelMedAudit', 'db_table': "'mpepu_maternal_maternallabdelmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_health_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_ob_comp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelmed'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallabdelmed'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ob_comp_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
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
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 29, 0, 0)'}),
            'has_caretaker_alt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 29, 0, 0)'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternallocatoraudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalLocatorAudit', 'db_table': "'mpepu_maternal_maternallocator_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
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
            'date_signed': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2012, 7, 29, 0, 0)'}),
            'has_caretaker_alt': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'home_visit_permission': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'mail_address': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternallocator'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'may_call_work': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_contact_someone': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'may_follow_up': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_address': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 29, 0, 0)'}),
            'subject_cell': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_cell_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_phone_alt': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '78L', 'null': 'True', 'blank': 'True'}),
            'subject_work_place': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaloffstudy': {
            'Meta': {'object_name': 'MaternalOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternaloffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalOffStudyAudit', 'db_table': "'mpepu_maternal_maternaloffstudy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternaloffstudy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_weight': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'started_ctx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalpostfuaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostFuAudit', 'db_table': "'mpepu_maternal_maternalpostfu_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'breastfeeding': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'chronic_cond_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'enter_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'had_mastitis': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'has_chronic_cond': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfu'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_weight': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'started_ctx': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalpostfudx': {
            'Meta': {'object_name': 'MaternalPostFuDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_post_fu': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_maternal.MaternalPostFu']", 'unique': 'True'}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'new_diagnoses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'wcs_dx_adult': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_code_lists.WcsDxAdult']", 'symmetrical': 'False'}),
            'who_clinical_stage': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_maternal.maternalpostfudxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostFuDxAudit', 'db_table': "'mpepu_maternal_maternalpostfudx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_post_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfudx'", 'to': "orm['mpepu_maternal.MaternalPostFu']"}),
            'maternal_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfudx'", 'to': "orm['mpepu_maternal.MaternalVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mother_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'new_diagnoses': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'who_clinical_stage': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_maternal.maternalpostfudxt': {
            'Meta': {'object_name': 'MaternalPostFuDxT'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'maternal_post_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalPostFuDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_fu_specify': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalpostfudxtaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostFuDxTAudit', 'db_table': "'mpepu_maternal_maternalpostfudxt_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grade': ('django.db.models.fields.IntegerField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'maternal_post_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostfudxt'", 'to': "orm['mpepu_maternal.MaternalPostFuDx']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'post_fu_dx': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'post_fu_specify': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalpostreg': {
            'Meta': {'object_name': 'MaternalPostReg'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reg_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalpostregaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalPostRegAudit', 'db_table': "'mpepu_maternal_maternalpostreg_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reg_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalpostreg'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalvisit': {
            'Meta': {'object_name': 'MaternalVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'info_source': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_source_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'mpepu_maternal.maternalvisitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'MaternalVisitAudit', 'db_table': "'mpepu_maternal_maternalvisit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_maternalvisit'", 'to': "orm['bhp_appointment.Appointment']"}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
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

    complete_apps = ['mpepu_maternal']
