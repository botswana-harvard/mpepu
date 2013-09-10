# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'InfantMouthUpGastrointestinalItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantmouthupgastrointestinalitems', ['user_modified'])

        # Adding index on 'InfantMouthUpGastrointestinalItems', fields ['user_created']
        db.create_index('mpepu_infant_infantmouthupgastrointestinalitems', ['user_created'])

        # Adding index on 'InfantFuMed', fields ['user_modified']
        db.create_index('mpepu_infant_infantfumed', ['user_modified'])

        # Adding index on 'InfantFuMed', fields ['user_created']
        db.create_index('mpepu_infant_infantfumed', ['user_created'])

        # Adding index on 'InfantHaartAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infanthaart_audit', ['user_modified'])

        # Adding index on 'InfantHaartAudit', fields ['user_created']
        db.create_index('mpepu_infant_infanthaart_audit', ['user_created'])

        # Adding index on 'InfantFuMedAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfumed_audit', ['user_modified'])

        # Adding index on 'InfantFuMedAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfumed_audit', ['user_created'])

        # Adding index on 'InfantOffStudyAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantoffstudy_audit', ['user_modified'])


        # Changing field 'InfantOffStudyAudit.reason'
        db.alter_column('mpepu_infant_infantoffstudy_audit', 'reason', self.gf('django.db.models.fields.CharField')(max_length=30))
        # Adding index on 'InfantOffStudyAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantoffstudy_audit', ['user_created'])

        # Adding index on 'InfantBirth', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirth', ['user_modified'])

        # Adding index on 'InfantBirth', fields ['user_created']
        db.create_index('mpepu_infant_infantbirth', ['user_created'])

        # Adding index on 'InfantSkinAbnormalItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantskinabnormalitems', ['user_modified'])

        # Adding index on 'InfantSkinAbnormalItems', fields ['user_created']
        db.create_index('mpepu_infant_infantskinabnormalitems', ['user_created'])

        # Adding index on 'InfantOffStudy', fields ['user_modified']
        db.create_index('mpepu_infant_infantoffstudy', ['user_modified'])


        # Changing field 'InfantOffStudy.reason'
        db.alter_column('mpepu_infant_infantoffstudy', 'reason', self.gf('django.db.models.fields.CharField')(max_length=30))
        # Adding index on 'InfantOffStudy', fields ['user_created']
        db.create_index('mpepu_infant_infantoffstudy', ['user_created'])

        # Adding index on 'InfantRandoDeferralAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantrandodeferral_audit', ['user_modified'])

        # Adding index on 'InfantRandoDeferralAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantrandodeferral_audit', ['user_created'])

        # Adding index on 'InfantFuPhysical', fields ['user_modified']
        db.create_index('mpepu_infant_infantfuphysical', ['user_modified'])

        # Adding index on 'InfantFuPhysical', fields ['user_created']
        db.create_index('mpepu_infant_infantfuphysical', ['user_created'])

        # Adding index on 'InfantFemaleGenitalAnomalyItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantfemalegenitalanomalyitems', ['user_modified'])

        # Adding index on 'InfantFemaleGenitalAnomalyItems', fields ['user_created']
        db.create_index('mpepu_infant_infantfemalegenitalanomalyitems', ['user_created'])

        # Adding index on 'InfantFuDAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfud_audit', ['user_modified'])

        # Adding index on 'InfantFuDAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfud_audit', ['user_created'])

        # Adding index on 'InfantFuD', fields ['user_modified']
        db.create_index('mpepu_infant_infantfud', ['user_modified'])

        # Adding index on 'InfantFuD', fields ['user_created']
        db.create_index('mpepu_infant_infantfud', ['user_created'])

        # Adding index on 'InfantFu', fields ['user_modified']
        db.create_index('mpepu_infant_infantfu', ['user_modified'])

        # Adding index on 'InfantFu', fields ['user_created']
        db.create_index('mpepu_infant_infantfu', ['user_created'])

        # Adding index on 'InfantFuDxItemsAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudxitems_audit', ['user_modified'])

        # Adding index on 'InfantFuDxItemsAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfudxitems_audit', ['user_created'])

        # Adding index on 'InfantStudyDrugItemsAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantstudydrugitems_audit', ['user_modified'])

        # Adding index on 'InfantStudyDrugItemsAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantstudydrugitems_audit', ['user_created'])

        # Adding index on 'InfantCongenitalAnomalies', fields ['user_modified']
        db.create_index('mpepu_infant_infantcongenitalanomalies', ['user_modified'])

        # Adding index on 'InfantCongenitalAnomalies', fields ['user_created']
        db.create_index('mpepu_infant_infantcongenitalanomalies', ['user_created'])

        # Adding index on 'InfantCardiovascularDisorderItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantcardiovasculardisorderitems', ['user_modified'])

        # Adding index on 'InfantCardiovascularDisorderItems', fields ['user_created']
        db.create_index('mpepu_infant_infantcardiovasculardisorderitems', ['user_created'])

        # Adding index on 'InfantArvProph', fields ['user_modified']
        db.create_index('mpepu_infant_infantarvproph', ['user_modified'])

        # Adding index on 'InfantArvProph', fields ['user_created']
        db.create_index('mpepu_infant_infantarvproph', ['user_created'])

        # Adding index on 'InfantStudyDrugAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantstudydrug_audit', ['user_modified'])

        # Adding index on 'InfantStudyDrugAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantstudydrug_audit', ['user_created'])

        # Adding index on 'InfantHivStatusAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infanthivstatus_audit', ['user_modified'])

        # Adding index on 'InfantHivStatusAudit', fields ['user_created']
        db.create_index('mpepu_infant_infanthivstatus_audit', ['user_created'])

        # Adding index on 'InfantArvProphAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantarvproph_audit', ['user_modified'])

        # Adding index on 'InfantArvProphAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantarvproph_audit', ['user_created'])

        # Adding index on 'InfantFuNewMedItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantfunewmeditems', ['user_modified'])

        # Adding index on 'InfantFuNewMedItems', fields ['user_created']
        db.create_index('mpepu_infant_infantfunewmeditems', ['user_created'])

        # Adding index on 'InfantHaart', fields ['user_modified']
        db.create_index('mpepu_infant_infanthaart', ['user_modified'])

        # Adding index on 'InfantHaart', fields ['user_created']
        db.create_index('mpepu_infant_infanthaart', ['user_created'])

        # Adding index on 'InfantLowerGastrointestinalItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantlowergastrointestinalitems', ['user_modified'])

        # Adding index on 'InfantLowerGastrointestinalItems', fields ['user_created']
        db.create_index('mpepu_infant_infantlowergastrointestinalitems', ['user_created'])

        # Adding index on 'InfantMaleGenitalAnomalyItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantmalegenitalanomalyitems', ['user_modified'])

        # Adding index on 'InfantMaleGenitalAnomalyItems', fields ['user_created']
        db.create_index('mpepu_infant_infantmalegenitalanomalyitems', ['user_created'])

        # Adding index on 'InfantStudyDrugInit', fields ['user_modified']
        db.create_index('mpepu_infant_infantstudydruginit', ['user_modified'])

        # Adding index on 'InfantStudyDrugInit', fields ['user_created']
        db.create_index('mpepu_infant_infantstudydruginit', ['user_created'])

        # Adding index on 'InfantHaartModAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infanthaartmod_audit', ['user_modified'])

        # Adding index on 'InfantHaartModAudit', fields ['user_created']
        db.create_index('mpepu_infant_infanthaartmod_audit', ['user_created'])

        # Adding index on 'InfantFuDx2ProphItemsAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudx2prophitems_audit', ['user_modified'])

        # Adding index on 'InfantFuDx2ProphItemsAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfudx2prophitems_audit', ['user_created'])

        # Adding index on 'InfantNvpAdherenceAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantnvpadherence_audit', ['user_modified'])

        # Adding index on 'InfantNvpAdherenceAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantnvpadherence_audit', ['user_created'])

        # Adding index on 'InfantFuNewMedItemsAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfunewmeditems_audit', ['user_modified'])

        # Adding index on 'InfantFuNewMedItemsAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfunewmeditems_audit', ['user_created'])

        # Adding index on 'InfantMusculoskeletalAbnormalItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantmusculoskeletalabnormalitems', ['user_modified'])

        # Adding index on 'InfantMusculoskeletalAbnormalItems', fields ['user_created']
        db.create_index('mpepu_infant_infantmusculoskeletalabnormalitems', ['user_created'])

        # Adding index on 'InfantHivStatus', fields ['user_modified']
        db.create_index('mpepu_infant_infanthivstatus', ['user_modified'])

        # Adding index on 'InfantHivStatus', fields ['user_created']
        db.create_index('mpepu_infant_infanthivstatus', ['user_created'])

        # Adding index on 'InfantDeath', fields ['user_created']
        db.create_index('mpepu_infant_infantdeath', ['user_created'])

        # Adding index on 'InfantDeath', fields ['user_modified']
        db.create_index('mpepu_infant_infantdeath', ['user_modified'])


        # Changing field 'InfantDeath.death_cause'
        db.alter_column('mpepu_infant_infantdeath', 'death_cause', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))
        # Adding index on 'InfantSurvival', fields ['user_modified']
        db.create_index('mpepu_infant_infantsurvival', ['user_modified'])

        # Adding index on 'InfantSurvival', fields ['user_created']
        db.create_index('mpepu_infant_infantsurvival', ['user_created'])

        # Adding index on 'InfantFuAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfu_audit', ['user_modified'])

        # Adding index on 'InfantFuAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfu_audit', ['user_created'])

        # Adding index on 'InfantBirthFeed', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirthfeed', ['user_modified'])

        # Adding index on 'InfantBirthFeed', fields ['user_created']
        db.create_index('mpepu_infant_infantbirthfeed', ['user_created'])

        # Adding index on 'InfantVitalStatusAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantvitalstatus_audit', ['user_modified'])

        # Adding index on 'InfantVitalStatusAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantvitalstatus_audit', ['user_created'])

        # Adding index on 'InfantEligibilityAudit', fields ['user_created']
        db.create_index('mpepu_infant_infanteligibility_audit', ['user_created'])

        # Adding index on 'InfantEligibilityAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infanteligibility_audit', ['user_modified'])

        # Adding index on 'InfantStudyDrug', fields ['user_modified']
        db.create_index('mpepu_infant_infantstudydrug', ['user_modified'])

        # Adding index on 'InfantStudyDrug', fields ['user_created']
        db.create_index('mpepu_infant_infantstudydrug', ['user_created'])

        # Adding index on 'InfantRandoDeferral', fields ['user_modified']
        db.create_index('mpepu_infant_infantrandodeferral', ['user_modified'])

        # Adding index on 'InfantRandoDeferral', fields ['user_created']
        db.create_index('mpepu_infant_infantrandodeferral', ['user_created'])

        # Adding index on 'InfantBirthExamAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantbirthexam_audit', ['user_created'])

        # Adding index on 'InfantBirthExamAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirthexam_audit', ['user_modified'])

        # Adding index on 'InfantOffDrug', fields ['user_modified']
        db.create_index('mpepu_infant_infantoffdrug', ['user_modified'])

        # Adding index on 'InfantOffDrug', fields ['user_created']
        db.create_index('mpepu_infant_infantoffdrug', ['user_created'])

        # Adding index on 'InfantFeeding', fields ['user_modified']
        db.create_index('mpepu_infant_infantfeeding', ['user_modified'])

        # Adding index on 'InfantFeeding', fields ['user_created']
        db.create_index('mpepu_infant_infantfeeding', ['user_created'])

        # Adding index on 'InfantFeedingAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfeeding_audit', ['user_modified'])

        # Adding index on 'InfantFeedingAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfeeding_audit', ['user_created'])

        # Adding index on 'InfantDeathAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantdeath_audit', ['user_created'])

        # Adding index on 'InfantDeathAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantdeath_audit', ['user_modified'])


        # Changing field 'InfantDeathAudit.death_cause'
        db.alter_column('mpepu_infant_infantdeath_audit', 'death_cause', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))
        # Adding index on 'InfantFacialDefectItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantfacialdefectitems', ['user_modified'])

        # Adding index on 'InfantFacialDefectItems', fields ['user_created']
        db.create_index('mpepu_infant_infantfacialdefectitems', ['user_created'])

        # Adding index on 'InfantBirthArv', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirtharv', ['user_modified'])

        # Adding index on 'InfantBirthArv', fields ['user_created']
        db.create_index('mpepu_infant_infantbirtharv', ['user_created'])

        # Adding index on 'InfantRespiratoryDefectItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantrespiratorydefectitems', ['user_modified'])

        # Adding index on 'InfantRespiratoryDefectItems', fields ['user_created']
        db.create_index('mpepu_infant_infantrespiratorydefectitems', ['user_created'])

        # Adding index on 'InfantOtherAbnormalityItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantotherabnormalityitems', ['user_modified'])

        # Adding index on 'InfantOtherAbnormalityItems', fields ['user_created']
        db.create_index('mpepu_infant_infantotherabnormalityitems', ['user_created'])

        # Adding index on 'InfantPreEligibility', fields ['user_modified']
        db.create_index('mpepu_infant_infantpreeligibility', ['user_modified'])

        # Adding index on 'InfantPreEligibility', fields ['user_created']
        db.create_index('mpepu_infant_infantpreeligibility', ['user_created'])

        # Adding index on 'InfantSurvivalAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantsurvival_audit', ['user_modified'])

        # Adding index on 'InfantSurvivalAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantsurvival_audit', ['user_created'])

        # Adding index on 'InfantCnsAbnormalityItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantcnsabnormalityitems', ['user_modified'])

        # Adding index on 'InfantCnsAbnormalityItems', fields ['user_created']
        db.create_index('mpepu_infant_infantcnsabnormalityitems', ['user_created'])

        # Adding index on 'InfantHaartMod', fields ['user_modified']
        db.create_index('mpepu_infant_infanthaartmod', ['user_modified'])

        # Adding index on 'InfantHaartMod', fields ['user_created']
        db.create_index('mpepu_infant_infanthaartmod', ['user_created'])

        # Adding index on 'InfantCtxPlaceboAdhAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantctxplaceboadh_audit', ['user_modified'])

        # Adding index on 'InfantCtxPlaceboAdhAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantctxplaceboadh_audit', ['user_created'])

        # Adding index on 'InfantArvProphModAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantarvprophmod_audit', ['user_modified'])

        # Adding index on 'InfantArvProphModAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantarvprophmod_audit', ['user_created'])

        # Adding index on 'InfantCleftDisorderItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantcleftdisorderitems', ['user_modified'])

        # Adding index on 'InfantCleftDisorderItems', fields ['user_created']
        db.create_index('mpepu_infant_infantcleftdisorderitems', ['user_created'])

        # Adding index on 'InfantFuDx2Proph', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudx2proph', ['user_modified'])

        # Adding index on 'InfantFuDx2Proph', fields ['user_created']
        db.create_index('mpepu_infant_infantfudx2proph', ['user_created'])

        # Adding index on 'InfantBirthData', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirthdata', ['user_modified'])

        # Adding index on 'InfantBirthData', fields ['user_created']
        db.create_index('mpepu_infant_infantbirthdata', ['user_created'])

        # Adding index on 'InfantStudyDrugInitAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantstudydruginit_audit', ['user_modified'])

        # Adding index on 'InfantStudyDrugInitAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantstudydruginit_audit', ['user_created'])

        # Adding index on 'InfantVisit', fields ['user_modified']
        db.create_index('mpepu_infant_infantvisit', ['user_modified'])

        # Adding index on 'InfantVisit', fields ['user_created']
        db.create_index('mpepu_infant_infantvisit', ['user_created'])

        # Adding index on 'InfantFuDx2ProphItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudx2prophitems', ['user_modified'])

        # Adding index on 'InfantFuDx2ProphItems', fields ['user_created']
        db.create_index('mpepu_infant_infantfudx2prophitems', ['user_created'])

        # Adding index on 'InfantFuNewMed', fields ['user_modified']
        db.create_index('mpepu_infant_infantfunewmed', ['user_modified'])

        # Adding index on 'InfantFuNewMed', fields ['user_created']
        db.create_index('mpepu_infant_infantfunewmed', ['user_created'])

        # Adding index on 'InfantRenalAnomalyItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantrenalanomalyitems', ['user_modified'])

        # Adding index on 'InfantRenalAnomalyItems', fields ['user_created']
        db.create_index('mpepu_infant_infantrenalanomalyitems', ['user_created'])

        # Adding index on 'InfantBirthArvAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantbirtharv_audit', ['user_created'])

        # Adding index on 'InfantBirthArvAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirtharv_audit', ['user_modified'])

        # Adding index on 'InfantFuNewMedAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfunewmed_audit', ['user_modified'])

        # Adding index on 'InfantFuNewMedAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfunewmed_audit', ['user_created'])

        # Adding index on 'InfantBirthExam', fields ['user_created']
        db.create_index('mpepu_infant_infantbirthexam', ['user_created'])

        # Adding index on 'InfantBirthExam', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirthexam', ['user_modified'])

        # Adding index on 'InfantTrisomiesChromosomeItems', fields ['user_modified']
        db.create_index('mpepu_infant_infanttrisomieschromosomeitems', ['user_modified'])

        # Adding index on 'InfantTrisomiesChromosomeItems', fields ['user_created']
        db.create_index('mpepu_infant_infanttrisomieschromosomeitems', ['user_created'])

        # Adding index on 'InfantBirthFeedAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirthfeed_audit', ['user_modified'])

        # Adding index on 'InfantBirthFeedAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantbirthfeed_audit', ['user_created'])

        # Adding index on 'InfantFuDx2ProphAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudx2proph_audit', ['user_modified'])

        # Adding index on 'InfantFuDx2ProphAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfudx2proph_audit', ['user_created'])

        # Adding index on 'InfantPreEligibilityAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantpreeligibility_audit', ['user_modified'])

        # Adding index on 'InfantPreEligibilityAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantpreeligibility_audit', ['user_created'])

        # Adding index on 'InfantCtxPlaceboAdh', fields ['user_modified']
        db.create_index('mpepu_infant_infantctxplaceboadh', ['user_modified'])

        # Adding index on 'InfantCtxPlaceboAdh', fields ['user_created']
        db.create_index('mpepu_infant_infantctxplaceboadh', ['user_created'])

        # Adding index on 'InfantFuPhysicalAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfuphysical_audit', ['user_modified'])

        # Adding index on 'InfantFuPhysicalAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfuphysical_audit', ['user_created'])

        # Adding index on 'InfantFuDxAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudx_audit', ['user_modified'])

        # Adding index on 'InfantFuDxAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantfudx_audit', ['user_created'])

        # Adding index on 'InfantFuDxItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudxitems', ['user_modified'])

        # Adding index on 'InfantFuDxItems', fields ['user_created']
        db.create_index('mpepu_infant_infantfudxitems', ['user_created'])

        # Adding index on 'InfantStudyDrugItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantstudydrugitems', ['user_modified'])

        # Adding index on 'InfantStudyDrugItems', fields ['user_created']
        db.create_index('mpepu_infant_infantstudydrugitems', ['user_created'])

        # Adding index on 'InfantBirthDataAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirthdata_audit', ['user_modified'])

        # Adding index on 'InfantBirthDataAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantbirthdata_audit', ['user_created'])

        # Adding index on 'InfantVerbalAutopsy', fields ['user_modified']
        db.create_index('mpepu_infant_infantverbalautopsy', ['user_modified'])

        # Adding index on 'InfantVerbalAutopsy', fields ['user_created']
        db.create_index('mpepu_infant_infantverbalautopsy', ['user_created'])

        # Adding index on 'InfantVerbalAutopsyItems', fields ['user_modified']
        db.create_index('mpepu_infant_infantverbalautopsyitems', ['user_modified'])

        # Adding index on 'InfantVerbalAutopsyItems', fields ['user_created']
        db.create_index('mpepu_infant_infantverbalautopsyitems', ['user_created'])

        # Adding index on 'InfantEligibility', fields ['user_modified']
        db.create_index('mpepu_infant_infanteligibility', ['user_modified'])

        # Adding index on 'InfantEligibility', fields ['user_created']
        db.create_index('mpepu_infant_infanteligibility', ['user_created'])

        # Adding index on 'InfantPrerandoLoss', fields ['user_modified']
        db.create_index('mpepu_infant_infantprerandoloss', ['user_modified'])

        # Adding index on 'InfantPrerandoLoss', fields ['user_created']
        db.create_index('mpepu_infant_infantprerandoloss', ['user_created'])

        # Adding index on 'InfantOffDrugAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantoffdrug_audit', ['user_modified'])

        # Adding index on 'InfantOffDrugAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantoffdrug_audit', ['user_created'])

        # Adding index on 'InfantNvpAdherence', fields ['user_modified']
        db.create_index('mpepu_infant_infantnvpadherence', ['user_modified'])

        # Adding index on 'InfantNvpAdherence', fields ['user_created']
        db.create_index('mpepu_infant_infantnvpadherence', ['user_created'])

        # Adding index on 'InfantVitalStatus', fields ['user_modified']
        db.create_index('mpepu_infant_infantvitalstatus', ['user_modified'])

        # Adding index on 'InfantVitalStatus', fields ['user_created']
        db.create_index('mpepu_infant_infantvitalstatus', ['user_created'])

        # Adding index on 'InfantVisitAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantvisit_audit', ['user_created'])

        # Adding index on 'InfantVisitAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantvisit_audit', ['user_modified'])

        # Adding index on 'InfantPrerandoLossAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantprerandoloss_audit', ['user_modified'])

        # Adding index on 'InfantPrerandoLossAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantprerandoloss_audit', ['user_created'])

        # Adding index on 'InfantVerbalAutopsyAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantverbalautopsy_audit', ['user_modified'])

        # Adding index on 'InfantVerbalAutopsyAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantverbalautopsy_audit', ['user_created'])

        # Adding index on 'InfantArvProphMod', fields ['user_modified']
        db.create_index('mpepu_infant_infantarvprophmod', ['user_modified'])

        # Adding index on 'InfantArvProphMod', fields ['user_created']
        db.create_index('mpepu_infant_infantarvprophmod', ['user_created'])

        # Adding index on 'InfantFuDx', fields ['user_modified']
        db.create_index('mpepu_infant_infantfudx', ['user_modified'])

        # Adding index on 'InfantFuDx', fields ['user_created']
        db.create_index('mpepu_infant_infantfudx', ['user_created'])

        # Adding index on 'InfantBirthAudit', fields ['user_modified']
        db.create_index('mpepu_infant_infantbirth_audit', ['user_modified'])

        # Adding index on 'InfantBirthAudit', fields ['user_created']
        db.create_index('mpepu_infant_infantbirth_audit', ['user_created'])


    def backwards(self, orm):
        # Removing index on 'InfantBirthAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirth_audit', ['user_created'])

        # Removing index on 'InfantBirthAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirth_audit', ['user_modified'])

        # Removing index on 'InfantFuDx', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudx', ['user_created'])

        # Removing index on 'InfantFuDx', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudx', ['user_modified'])

        # Removing index on 'InfantArvProphMod', fields ['user_created']
        db.delete_index('mpepu_infant_infantarvprophmod', ['user_created'])

        # Removing index on 'InfantArvProphMod', fields ['user_modified']
        db.delete_index('mpepu_infant_infantarvprophmod', ['user_modified'])

        # Removing index on 'InfantVerbalAutopsyAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantverbalautopsy_audit', ['user_created'])

        # Removing index on 'InfantVerbalAutopsyAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantverbalautopsy_audit', ['user_modified'])

        # Removing index on 'InfantPrerandoLossAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantprerandoloss_audit', ['user_created'])

        # Removing index on 'InfantPrerandoLossAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantprerandoloss_audit', ['user_modified'])

        # Removing index on 'InfantVisitAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantvisit_audit', ['user_modified'])

        # Removing index on 'InfantVisitAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantvisit_audit', ['user_created'])

        # Removing index on 'InfantVitalStatus', fields ['user_created']
        db.delete_index('mpepu_infant_infantvitalstatus', ['user_created'])

        # Removing index on 'InfantVitalStatus', fields ['user_modified']
        db.delete_index('mpepu_infant_infantvitalstatus', ['user_modified'])

        # Removing index on 'InfantNvpAdherence', fields ['user_created']
        db.delete_index('mpepu_infant_infantnvpadherence', ['user_created'])

        # Removing index on 'InfantNvpAdherence', fields ['user_modified']
        db.delete_index('mpepu_infant_infantnvpadherence', ['user_modified'])

        # Removing index on 'InfantOffDrugAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantoffdrug_audit', ['user_created'])

        # Removing index on 'InfantOffDrugAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantoffdrug_audit', ['user_modified'])

        # Removing index on 'InfantPrerandoLoss', fields ['user_created']
        db.delete_index('mpepu_infant_infantprerandoloss', ['user_created'])

        # Removing index on 'InfantPrerandoLoss', fields ['user_modified']
        db.delete_index('mpepu_infant_infantprerandoloss', ['user_modified'])

        # Removing index on 'InfantEligibility', fields ['user_created']
        db.delete_index('mpepu_infant_infanteligibility', ['user_created'])

        # Removing index on 'InfantEligibility', fields ['user_modified']
        db.delete_index('mpepu_infant_infanteligibility', ['user_modified'])

        # Removing index on 'InfantVerbalAutopsyItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantverbalautopsyitems', ['user_created'])

        # Removing index on 'InfantVerbalAutopsyItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantverbalautopsyitems', ['user_modified'])

        # Removing index on 'InfantVerbalAutopsy', fields ['user_created']
        db.delete_index('mpepu_infant_infantverbalautopsy', ['user_created'])

        # Removing index on 'InfantVerbalAutopsy', fields ['user_modified']
        db.delete_index('mpepu_infant_infantverbalautopsy', ['user_modified'])

        # Removing index on 'InfantBirthDataAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirthdata_audit', ['user_created'])

        # Removing index on 'InfantBirthDataAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirthdata_audit', ['user_modified'])

        # Removing index on 'InfantStudyDrugItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantstudydrugitems', ['user_created'])

        # Removing index on 'InfantStudyDrugItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantstudydrugitems', ['user_modified'])

        # Removing index on 'InfantFuDxItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudxitems', ['user_created'])

        # Removing index on 'InfantFuDxItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudxitems', ['user_modified'])

        # Removing index on 'InfantFuDxAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudx_audit', ['user_created'])

        # Removing index on 'InfantFuDxAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudx_audit', ['user_modified'])

        # Removing index on 'InfantFuPhysicalAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfuphysical_audit', ['user_created'])

        # Removing index on 'InfantFuPhysicalAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfuphysical_audit', ['user_modified'])

        # Removing index on 'InfantCtxPlaceboAdh', fields ['user_created']
        db.delete_index('mpepu_infant_infantctxplaceboadh', ['user_created'])

        # Removing index on 'InfantCtxPlaceboAdh', fields ['user_modified']
        db.delete_index('mpepu_infant_infantctxplaceboadh', ['user_modified'])

        # Removing index on 'InfantPreEligibilityAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantpreeligibility_audit', ['user_created'])

        # Removing index on 'InfantPreEligibilityAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantpreeligibility_audit', ['user_modified'])

        # Removing index on 'InfantFuDx2ProphAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudx2proph_audit', ['user_created'])

        # Removing index on 'InfantFuDx2ProphAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudx2proph_audit', ['user_modified'])

        # Removing index on 'InfantBirthFeedAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirthfeed_audit', ['user_created'])

        # Removing index on 'InfantBirthFeedAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirthfeed_audit', ['user_modified'])

        # Removing index on 'InfantTrisomiesChromosomeItems', fields ['user_created']
        db.delete_index('mpepu_infant_infanttrisomieschromosomeitems', ['user_created'])

        # Removing index on 'InfantTrisomiesChromosomeItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infanttrisomieschromosomeitems', ['user_modified'])

        # Removing index on 'InfantBirthExam', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirthexam', ['user_modified'])

        # Removing index on 'InfantBirthExam', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirthexam', ['user_created'])

        # Removing index on 'InfantFuNewMedAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfunewmed_audit', ['user_created'])

        # Removing index on 'InfantFuNewMedAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfunewmed_audit', ['user_modified'])

        # Removing index on 'InfantBirthArvAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirtharv_audit', ['user_modified'])

        # Removing index on 'InfantBirthArvAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirtharv_audit', ['user_created'])

        # Removing index on 'InfantRenalAnomalyItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantrenalanomalyitems', ['user_created'])

        # Removing index on 'InfantRenalAnomalyItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantrenalanomalyitems', ['user_modified'])

        # Removing index on 'InfantFuNewMed', fields ['user_created']
        db.delete_index('mpepu_infant_infantfunewmed', ['user_created'])

        # Removing index on 'InfantFuNewMed', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfunewmed', ['user_modified'])

        # Removing index on 'InfantFuDx2ProphItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudx2prophitems', ['user_created'])

        # Removing index on 'InfantFuDx2ProphItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudx2prophitems', ['user_modified'])

        # Removing index on 'InfantVisit', fields ['user_created']
        db.delete_index('mpepu_infant_infantvisit', ['user_created'])

        # Removing index on 'InfantVisit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantvisit', ['user_modified'])

        # Removing index on 'InfantStudyDrugInitAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantstudydruginit_audit', ['user_created'])

        # Removing index on 'InfantStudyDrugInitAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantstudydruginit_audit', ['user_modified'])

        # Removing index on 'InfantBirthData', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirthdata', ['user_created'])

        # Removing index on 'InfantBirthData', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirthdata', ['user_modified'])

        # Removing index on 'InfantFuDx2Proph', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudx2proph', ['user_created'])

        # Removing index on 'InfantFuDx2Proph', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudx2proph', ['user_modified'])

        # Removing index on 'InfantCleftDisorderItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantcleftdisorderitems', ['user_created'])

        # Removing index on 'InfantCleftDisorderItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantcleftdisorderitems', ['user_modified'])

        # Removing index on 'InfantArvProphModAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantarvprophmod_audit', ['user_created'])

        # Removing index on 'InfantArvProphModAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantarvprophmod_audit', ['user_modified'])

        # Removing index on 'InfantCtxPlaceboAdhAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantctxplaceboadh_audit', ['user_created'])

        # Removing index on 'InfantCtxPlaceboAdhAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantctxplaceboadh_audit', ['user_modified'])

        # Removing index on 'InfantHaartMod', fields ['user_created']
        db.delete_index('mpepu_infant_infanthaartmod', ['user_created'])

        # Removing index on 'InfantHaartMod', fields ['user_modified']
        db.delete_index('mpepu_infant_infanthaartmod', ['user_modified'])

        # Removing index on 'InfantCnsAbnormalityItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantcnsabnormalityitems', ['user_created'])

        # Removing index on 'InfantCnsAbnormalityItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantcnsabnormalityitems', ['user_modified'])

        # Removing index on 'InfantSurvivalAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantsurvival_audit', ['user_created'])

        # Removing index on 'InfantSurvivalAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantsurvival_audit', ['user_modified'])

        # Removing index on 'InfantPreEligibility', fields ['user_created']
        db.delete_index('mpepu_infant_infantpreeligibility', ['user_created'])

        # Removing index on 'InfantPreEligibility', fields ['user_modified']
        db.delete_index('mpepu_infant_infantpreeligibility', ['user_modified'])

        # Removing index on 'InfantOtherAbnormalityItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantotherabnormalityitems', ['user_created'])

        # Removing index on 'InfantOtherAbnormalityItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantotherabnormalityitems', ['user_modified'])

        # Removing index on 'InfantRespiratoryDefectItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantrespiratorydefectitems', ['user_created'])

        # Removing index on 'InfantRespiratoryDefectItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantrespiratorydefectitems', ['user_modified'])

        # Removing index on 'InfantBirthArv', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirtharv', ['user_created'])

        # Removing index on 'InfantBirthArv', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirtharv', ['user_modified'])

        # Removing index on 'InfantFacialDefectItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantfacialdefectitems', ['user_created'])

        # Removing index on 'InfantFacialDefectItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfacialdefectitems', ['user_modified'])

        # Removing index on 'InfantDeathAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantdeath_audit', ['user_modified'])

        # Removing index on 'InfantDeathAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantdeath_audit', ['user_created'])

        # Removing index on 'InfantFeedingAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfeeding_audit', ['user_created'])

        # Removing index on 'InfantFeedingAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfeeding_audit', ['user_modified'])

        # Removing index on 'InfantFeeding', fields ['user_created']
        db.delete_index('mpepu_infant_infantfeeding', ['user_created'])

        # Removing index on 'InfantFeeding', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfeeding', ['user_modified'])

        # Removing index on 'InfantOffDrug', fields ['user_created']
        db.delete_index('mpepu_infant_infantoffdrug', ['user_created'])

        # Removing index on 'InfantOffDrug', fields ['user_modified']
        db.delete_index('mpepu_infant_infantoffdrug', ['user_modified'])

        # Removing index on 'InfantBirthExamAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirthexam_audit', ['user_modified'])

        # Removing index on 'InfantBirthExamAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirthexam_audit', ['user_created'])

        # Removing index on 'InfantRandoDeferral', fields ['user_created']
        db.delete_index('mpepu_infant_infantrandodeferral', ['user_created'])

        # Removing index on 'InfantRandoDeferral', fields ['user_modified']
        db.delete_index('mpepu_infant_infantrandodeferral', ['user_modified'])

        # Removing index on 'InfantStudyDrug', fields ['user_created']
        db.delete_index('mpepu_infant_infantstudydrug', ['user_created'])

        # Removing index on 'InfantStudyDrug', fields ['user_modified']
        db.delete_index('mpepu_infant_infantstudydrug', ['user_modified'])

        # Removing index on 'InfantEligibilityAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infanteligibility_audit', ['user_modified'])

        # Removing index on 'InfantEligibilityAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infanteligibility_audit', ['user_created'])

        # Removing index on 'InfantVitalStatusAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantvitalstatus_audit', ['user_created'])

        # Removing index on 'InfantVitalStatusAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantvitalstatus_audit', ['user_modified'])

        # Removing index on 'InfantBirthFeed', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirthfeed', ['user_created'])

        # Removing index on 'InfantBirthFeed', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirthfeed', ['user_modified'])

        # Removing index on 'InfantFuAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfu_audit', ['user_created'])

        # Removing index on 'InfantFuAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfu_audit', ['user_modified'])

        # Removing index on 'InfantSurvival', fields ['user_created']
        db.delete_index('mpepu_infant_infantsurvival', ['user_created'])

        # Removing index on 'InfantSurvival', fields ['user_modified']
        db.delete_index('mpepu_infant_infantsurvival', ['user_modified'])

        # Removing index on 'InfantDeath', fields ['user_modified']
        db.delete_index('mpepu_infant_infantdeath', ['user_modified'])

        # Removing index on 'InfantDeath', fields ['user_created']
        db.delete_index('mpepu_infant_infantdeath', ['user_created'])

        # Removing index on 'InfantHivStatus', fields ['user_created']
        db.delete_index('mpepu_infant_infanthivstatus', ['user_created'])

        # Removing index on 'InfantHivStatus', fields ['user_modified']
        db.delete_index('mpepu_infant_infanthivstatus', ['user_modified'])

        # Removing index on 'InfantMusculoskeletalAbnormalItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantmusculoskeletalabnormalitems', ['user_created'])

        # Removing index on 'InfantMusculoskeletalAbnormalItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantmusculoskeletalabnormalitems', ['user_modified'])

        # Removing index on 'InfantFuNewMedItemsAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfunewmeditems_audit', ['user_created'])

        # Removing index on 'InfantFuNewMedItemsAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfunewmeditems_audit', ['user_modified'])

        # Removing index on 'InfantNvpAdherenceAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantnvpadherence_audit', ['user_created'])

        # Removing index on 'InfantNvpAdherenceAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantnvpadherence_audit', ['user_modified'])

        # Removing index on 'InfantFuDx2ProphItemsAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudx2prophitems_audit', ['user_created'])

        # Removing index on 'InfantFuDx2ProphItemsAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudx2prophitems_audit', ['user_modified'])

        # Removing index on 'InfantHaartModAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infanthaartmod_audit', ['user_created'])

        # Removing index on 'InfantHaartModAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infanthaartmod_audit', ['user_modified'])

        # Removing index on 'InfantStudyDrugInit', fields ['user_created']
        db.delete_index('mpepu_infant_infantstudydruginit', ['user_created'])

        # Removing index on 'InfantStudyDrugInit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantstudydruginit', ['user_modified'])

        # Removing index on 'InfantMaleGenitalAnomalyItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantmalegenitalanomalyitems', ['user_created'])

        # Removing index on 'InfantMaleGenitalAnomalyItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantmalegenitalanomalyitems', ['user_modified'])

        # Removing index on 'InfantLowerGastrointestinalItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantlowergastrointestinalitems', ['user_created'])

        # Removing index on 'InfantLowerGastrointestinalItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantlowergastrointestinalitems', ['user_modified'])

        # Removing index on 'InfantHaart', fields ['user_created']
        db.delete_index('mpepu_infant_infanthaart', ['user_created'])

        # Removing index on 'InfantHaart', fields ['user_modified']
        db.delete_index('mpepu_infant_infanthaart', ['user_modified'])

        # Removing index on 'InfantFuNewMedItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantfunewmeditems', ['user_created'])

        # Removing index on 'InfantFuNewMedItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfunewmeditems', ['user_modified'])

        # Removing index on 'InfantArvProphAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantarvproph_audit', ['user_created'])

        # Removing index on 'InfantArvProphAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantarvproph_audit', ['user_modified'])

        # Removing index on 'InfantHivStatusAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infanthivstatus_audit', ['user_created'])

        # Removing index on 'InfantHivStatusAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infanthivstatus_audit', ['user_modified'])

        # Removing index on 'InfantStudyDrugAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantstudydrug_audit', ['user_created'])

        # Removing index on 'InfantStudyDrugAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantstudydrug_audit', ['user_modified'])

        # Removing index on 'InfantArvProph', fields ['user_created']
        db.delete_index('mpepu_infant_infantarvproph', ['user_created'])

        # Removing index on 'InfantArvProph', fields ['user_modified']
        db.delete_index('mpepu_infant_infantarvproph', ['user_modified'])

        # Removing index on 'InfantCardiovascularDisorderItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantcardiovasculardisorderitems', ['user_created'])

        # Removing index on 'InfantCardiovascularDisorderItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantcardiovasculardisorderitems', ['user_modified'])

        # Removing index on 'InfantCongenitalAnomalies', fields ['user_created']
        db.delete_index('mpepu_infant_infantcongenitalanomalies', ['user_created'])

        # Removing index on 'InfantCongenitalAnomalies', fields ['user_modified']
        db.delete_index('mpepu_infant_infantcongenitalanomalies', ['user_modified'])

        # Removing index on 'InfantStudyDrugItemsAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantstudydrugitems_audit', ['user_created'])

        # Removing index on 'InfantStudyDrugItemsAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantstudydrugitems_audit', ['user_modified'])

        # Removing index on 'InfantFuDxItemsAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfudxitems_audit', ['user_created'])

        # Removing index on 'InfantFuDxItemsAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfudxitems_audit', ['user_modified'])

        # Removing index on 'InfantFu', fields ['user_created']
        db.delete_index('mpepu_infant_infantfu', ['user_created'])

        # Removing index on 'InfantFu', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfu', ['user_modified'])

        # Removing index on 'InfantFuD', fields ['user_created']
        db.delete_index('mpepu_infant_infantfud', ['user_created'])

        # Removing index on 'InfantFuD', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfud', ['user_modified'])

        # Removing index on 'InfantFuDAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfud_audit', ['user_created'])

        # Removing index on 'InfantFuDAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfud_audit', ['user_modified'])

        # Removing index on 'InfantFemaleGenitalAnomalyItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantfemalegenitalanomalyitems', ['user_created'])

        # Removing index on 'InfantFemaleGenitalAnomalyItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfemalegenitalanomalyitems', ['user_modified'])

        # Removing index on 'InfantFuPhysical', fields ['user_created']
        db.delete_index('mpepu_infant_infantfuphysical', ['user_created'])

        # Removing index on 'InfantFuPhysical', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfuphysical', ['user_modified'])

        # Removing index on 'InfantRandoDeferralAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantrandodeferral_audit', ['user_created'])

        # Removing index on 'InfantRandoDeferralAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantrandodeferral_audit', ['user_modified'])

        # Removing index on 'InfantOffStudy', fields ['user_created']
        db.delete_index('mpepu_infant_infantoffstudy', ['user_created'])

        # Removing index on 'InfantOffStudy', fields ['user_modified']
        db.delete_index('mpepu_infant_infantoffstudy', ['user_modified'])

        # Removing index on 'InfantSkinAbnormalItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantskinabnormalitems', ['user_created'])

        # Removing index on 'InfantSkinAbnormalItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantskinabnormalitems', ['user_modified'])

        # Removing index on 'InfantBirth', fields ['user_created']
        db.delete_index('mpepu_infant_infantbirth', ['user_created'])

        # Removing index on 'InfantBirth', fields ['user_modified']
        db.delete_index('mpepu_infant_infantbirth', ['user_modified'])

        # Removing index on 'InfantOffStudyAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantoffstudy_audit', ['user_created'])

        # Removing index on 'InfantOffStudyAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantoffstudy_audit', ['user_modified'])

        # Removing index on 'InfantFuMedAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infantfumed_audit', ['user_created'])

        # Removing index on 'InfantFuMedAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfumed_audit', ['user_modified'])

        # Removing index on 'InfantHaartAudit', fields ['user_created']
        db.delete_index('mpepu_infant_infanthaart_audit', ['user_created'])

        # Removing index on 'InfantHaartAudit', fields ['user_modified']
        db.delete_index('mpepu_infant_infanthaart_audit', ['user_modified'])

        # Removing index on 'InfantFuMed', fields ['user_created']
        db.delete_index('mpepu_infant_infantfumed', ['user_created'])

        # Removing index on 'InfantFuMed', fields ['user_modified']
        db.delete_index('mpepu_infant_infantfumed', ['user_modified'])

        # Removing index on 'InfantMouthUpGastrointestinalItems', fields ['user_created']
        db.delete_index('mpepu_infant_infantmouthupgastrointestinalitems', ['user_created'])

        # Removing index on 'InfantMouthUpGastrointestinalItems', fields ['user_modified']
        db.delete_index('mpepu_infant_infantmouthupgastrointestinalitems', ['user_modified'])


        # Changing field 'InfantOffStudyAudit.reason'
        db.alter_column('mpepu_infant_infantoffstudy_audit', 'reason', self.gf('django.db.models.fields.CharField')(max_length=25))

        # Changing field 'InfantOffStudy.reason'
        db.alter_column('mpepu_infant_infantoffstudy', 'reason', self.gf('django.db.models.fields.CharField')(max_length=25))

        # User chose to not deal with backwards NULL issues for 'InfantDeath.death_cause'
        raise RuntimeError("Cannot reverse this migration. 'InfantDeath.death_cause' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'InfantDeathAudit.death_cause'
        raise RuntimeError("Cannot reverse this migration. 'InfantDeathAudit.death_cause' and its values cannot be restored.")

    models = {
        'bhp_adverse.deathcausecategory': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseCategory'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathcauseinfo': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathCauseInfo'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathmedicalresponsibility': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathMedicalResponsibility'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_adverse.deathreasonhospitalized': {
            'Meta': {'ordering': "['display_index']", 'object_name': 'DeathReasonHospitalized'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'default': "'1.0'", 'max_length': '35'})
        },
        'bhp_appointment.appointment': {
            'Meta': {'ordering': "['registered_subject', 'appt_datetime']", 'unique_together': "(('registered_subject', 'visit_definition', 'visit_instance'),)", 'object_name': 'Appointment'},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'is_confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'study_site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_variables.StudySite']", 'null': 'True'}),
            'timepoint_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visit_definition': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['bhp_visit.VisitDefinition']"}),
            'visit_instance': ('django.db.models.fields.CharField', [], {'default': "'0'", 'max_length': '1', 'null': 'True', 'db_index': 'True', 'blank': 'True'})
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_code_lists.wcsdxped': {
            'Meta': {'object_name': 'WcsDxPed'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '15'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list_ref': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'long_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_content_type_map.contenttypemap': {
            'Meta': {'ordering': "['name']", 'unique_together': "(['app_label', 'model'],)", 'object_name': 'ContentTypeMap', 'db_table': "'bhp_common_contenttypemap'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_registration.registeredsubject': {
            'Meta': {'ordering': "['subject_identifier']", 'unique_together': "(('identity', 'first_name', 'dob', 'initials', 'registration_identifier'),)", 'object_name': 'RegisteredSubject'},
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
            'subject_identifier': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'unique': 'True', 'max_length': '50', 'blank': 'True'}),
            'subject_identifier_as_pk': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'db_index': 'True'}),
            'subject_type': ('django.db.models.fields.CharField', [], {'default': "'undetermined'", 'max_length': '25', 'null': 'True'}),
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_variables.studysite': {
            'Meta': {'ordering': "['site_code']", 'unique_together': "[('site_code', 'site_name')]", 'object_name': 'StudySite'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'site_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '4'}),
            'site_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_visit.membershipform': {
            'Meta': {'object_name': 'MembershipForm'},
            'category': ('django.db.models.fields.CharField', [], {'default': "'subject'", 'max_length': '25', 'null': 'True'}),
            'content_type_map': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'+'", 'unique': 'True', 'to': "orm['bhp_content_type_map.ContentTypeMap']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'bhp_visit.schedulegroup': {
            'Meta': {'ordering': "['group_name']", 'object_name': 'ScheduleGroup'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'group_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'grouping_key': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'membership_form': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_visit.MembershipForm']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'bhp_visit.visitdefinition': {
            'Meta': {'ordering': "['code', 'time_point']", 'object_name': 'VisitDefinition'},
            'base_interval': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'base_interval_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '6', 'db_index': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'grouping': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {'max_length': '255', 'blank': 'True'}),
            'lower_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'lower_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'schedule_group': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bhp_visit.ScheduleGroup']", 'null': 'True', 'blank': 'True'}),
            'time_point': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '35', 'db_index': 'True'}),
            'upper_window': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'upper_window_unit': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '10'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prophylatic_nvp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantarvprophaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantArvProphAudit', 'db_table': "'mpepu_infant_infantarvproph_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'arv_status': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantarvproph'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prophylatic_nvp': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantarvprophmod': {
            'Meta': {'object_name': 'InfantArvProphMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantArvProph']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantarvprophmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantArvProphModAudit', 'db_table': "'mpepu_infant_infantarvprophmod_audit'"},
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
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantarvprophmod'", 'to': "orm['mpepu_infant.InfantArvProph']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nvp_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sdnvp_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirtharvaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthArvAudit', 'db_table': "'mpepu_infant_infantbirtharv_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_arv_comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirtharv'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirtharv'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp_discharge_supply': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'nvp_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'sdnvp_after_birth': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthAudit', 'db_table': "'mpepu_infant_infantbirth_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'birth_order': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '78L'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'maternal_lab_del': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirth'", 'to': "orm['mpepu_maternal.MaternalLabDel']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirth'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_birth_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'infant_length': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_birth_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthdataaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthDataAudit', 'db_table': "'mpepu_infant_infantbirthdata_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthdata'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_birth_weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'infant_length': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '1'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthdata'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_birth_info': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthexamaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthExamAudit', 'db_table': "'mpepu_infant_infantbirthexam_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantbirthfeed': {
            'Meta': {'object_name': 'InfantBirthFeed'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_after_delivery': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vaccination': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.InfantVaccines']", 'symmetrical': 'False'})
        },
        'mpepu_infant.infantbirthfeedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantBirthFeedAudit', 'db_table': "'mpepu_infant_infantbirthfeed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'feeding_after_delivery': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthfeed'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantbirthfeed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantcongenitalanomalies': {
            'Meta': {'object_name': 'InfantCongenitalAnomalies'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantctxplaceboadh': {
            'Meta': {'object_name': 'InfantCtxPlaceboAdh'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'day_missed_drug': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'reason_missed_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantctxplaceboadhaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantCtxPlaceboAdhAudit', 'db_table': "'mpepu_infant_infantctxplaceboadh_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'day_missed_drug': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantctxplaceboadh'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'reason_missed_other': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantdeath': {
            'Meta': {'object_name': 'InfantDeath'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_adverse.DeathReasonHospitalized']", 'null': 'True', 'blank': 'True'}),
            'death_reason_hospitalized_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bhp_code_lists.DxCode']", 'max_length': '25'}),
            'haart_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'infant_nvp_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'study_drug_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'trad_med_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantdeathaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantDeathAudit', 'db_table': "'mpepu_infant_infantdeath_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'death_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'death_cause_category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathCauseCategory']"}),
            'death_cause_info': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathCauseInfo']"}),
            'death_cause_info_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_cause_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'death_date': ('django.db.models.fields.DateField', [], {}),
            'death_medical_responsibility': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_adverse.DeathMedicalResponsibility']"}),
            'death_reason_hospitalized': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'_audit_infantdeath'", 'null': 'True', 'to': "orm['bhp_adverse.DeathReasonHospitalized']"}),
            'death_reason_hospitalized_other': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'dx_code': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'max_length': '25', 'to': "orm['bhp_code_lists.DxCode']"}),
            'haart_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'illness_duration': ('django.db.models.fields.IntegerField', [], {}),
            'infant_nvp_relate': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'participant_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'perform_autopsy': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantdeath'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'maternal_art_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'maternal_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'rando_bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'randomization_site': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infanteligibilityaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantEligibilityAudit', 'db_table': "'mpepu_infant_infanteligibility_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanteligibility'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'maternal_art_status': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'maternal_feeding_choice': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'rando_bf_duration': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'randomization_site': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanteligibility'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'water': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '10'}),
            'water_used': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '50'}),
            'water_used_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'weaned_completely': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '3'})
        },
        'mpepu_infant.infantfeedingaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFeedingAudit', 'db_table': "'mpepu_infant_infantfeeding_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfu': {
            'Meta': {'object_name': 'InfantFu'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_illness': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_assessment': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfuaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuAudit', 'db_table': "'mpepu_infant_infantfu_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_illness': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfu'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'physical_assessment': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDAudit', 'db_table': "'mpepu_infant_infantfud_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'bloody_diarrhea': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'diarrhea_episodes': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'diarrhea_grade': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'fever_present': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'health_facility': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfud'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfud'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudx': {
            'Meta': {'object_name': 'InfantFuDx'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudx2proph': {
            'Meta': {'object_name': 'InfantFuDx2Proph'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'wcs_dx_ped': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bhp_code_lists.WcsDxPed']", 'symmetrical': 'False'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfudx2prophaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDx2ProphAudit', 'db_table': "'mpepu_infant_infantfudx2proph_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'has_dx': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2proph'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2proph'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'who_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfudx2prophitems': {
            'Meta': {'object_name': 'InfantFuDx2ProphItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuDx2Proph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudx2prophitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDx2ProphItemsAudit', 'db_table': "'mpepu_infant_infantfudx2prophitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'ctx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'dx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx2prophitems'", 'to': "orm['mpepu_infant.InfantFuDx2Proph']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'nvp': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfudxaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDxAudit', 'db_table': "'mpepu_infant_infantfudx_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudx'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuDx']"}),
            'is_eae_required': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_infant.infantfudxitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuDxItemsAudit', 'db_table': "'mpepu_infant_infantfudxitems_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu_dx': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfudxitems'", 'to': "orm['mpepu_infant.InfantFuDx']"}),
            'is_eae_required': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'mpepu_infant.infantfumed': {
            'Meta': {'object_name': 'InfantFuMed'},
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vaccination': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.InfantVaccines']", 'symmetrical': 'False'}),
            'vaccines_received': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfumedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuMedAudit', 'db_table': "'mpepu_infant_infantfumed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfumed'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfumed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'vaccines_received': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'mpepu_infant.infantfunewmed': {
            'Meta': {'object_name': 'InfantFuNewMed'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'new_medications': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_medications': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfunewmedaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuNewMedAudit', 'db_table': "'mpepu_infant_infantfunewmed_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmed'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmed'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'new_medications': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'other_medications': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfunewmeditems': {
            'Meta': {'object_name': 'InfantFuNewMedItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_route': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu_med': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFuNewMed']"}),
            'medication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfunewmeditemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuNewMedItemsAudit', 'db_table': "'mpepu_infant_infantfunewmeditems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_route': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu_med': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfunewmeditems'", 'to': "orm['mpepu_infant.InfantFuNewMed']"}),
            'medication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantfuphysical': {
            'Meta': {'object_name': 'InfantFuPhysical'},
            'abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'was_hospitalized': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'})
        },
        'mpepu_infant.infantfuphysicalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantFuPhysicalAudit', 'db_table': "'mpepu_infant_infantfuphysical_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_hospitalized': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'height': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_fu': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfuphysical'", 'to': "orm['mpepu_infant.InfantFu']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantfuphysical'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthaartaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHaartAudit', 'db_table': "'mpepu_infant_infanthaart_audit'"},
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthaart'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthaartmod': {
            'Meta': {'object_name': 'InfantHaartMod'},
            'arv_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_haart': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantHaart']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthaartmodaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHaartModAudit', 'db_table': "'mpepu_infant_infanthaartmod_audit'"},
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
            'infant_haart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthaartmod'", 'to': "orm['mpepu_infant.InfantHaart']"}),
            'modification_code': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modification_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthivstatus': {
            'Meta': {'object_name': 'InfantHivStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_first_pos': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_haart': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'infant_haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'recent_hiv_date': ('django.db.models.fields.DateField', [], {}),
            'recent_hiv_date_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'recent_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'result_record': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'test_place': ('django.db.models.fields.TextField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanthivstatusaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantHivStatusAudit', 'db_table': "'mpepu_infant_infanthivstatus_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_first_pos': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_haart': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'infant_haart_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infanthivstatus'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'recent_hiv_date': ('django.db.models.fields.DateField', [], {}),
            'recent_hiv_date_est': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'recent_hiv_result': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'result_record': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'test_place': ('django.db.models.fields.TextField', [], {'max_length': '35'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantlowergastrointestinalitems': {
            'Meta': {'object_name': 'InfantLowerGastrointestinalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'lower_gastrointestinal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'lower_gastrointestinal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantmalegenitalanomalyitems': {
            'Meta': {'object_name': 'InfantMaleGenitalAnomalyItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'male_genital_anomal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'male_genital_anomal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantmouthupgastrointestinalitems': {
            'Meta': {'object_name': 'InfantMouthUpGastrointestinalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'mouth_up_gastrointest': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'mouth_up_gastrointest_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantmusculoskeletalabnormalitems': {
            'Meta': {'object_name': 'InfantMusculoskeletalAbnormalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'musculo_skeletal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'musculo_skeletal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantnvpadherence': {
            'Meta': {'object_name': 'InfantNvpAdherence'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_missed': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantArvProph']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'reason_missed_other': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantnvpadherenceaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantNvpAdherenceAudit', 'db_table': "'mpepu_infant_infantnvpadherence_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'days_missed': ('django.db.models.fields.IntegerField', [], {'max_length': '2'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_arv_proph': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantnvpadherence'", 'to': "orm['mpepu_infant.InfantArvProph']"}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantnvpadherence'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_missed': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'reason_missed_other': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffdrug': {
            'Meta': {'object_name': 'InfantOffDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'last_dose_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_off': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_off_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffdrugaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantOffDrugAudit', 'db_table': "'mpepu_infant_infantoffdrug_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'last_dose_date': ('django.db.models.fields.DateField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_off': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'reason_off_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffdrug'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffstudy': {
            'Meta': {'object_name': 'InfantOffStudy'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'offstudy_date': ('django.db.models.fields.DateField', [], {}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantoffstudyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantOffStudyAudit', 'db_table': "'mpepu_infant_infantoffstudy_audit'"},
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
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'reason_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantoffstudy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantotherabnormalityitems': {
            'Meta': {'object_name': 'InfantOtherAbnormalityItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'other_abnormalities': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'other_abnormalities_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantpreeligibility': {
            'Meta': {'object_name': 'InfantPreEligibility'},
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infantpreeligibilityaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantPreEligibilityAudit', 'db_table': "'mpepu_infant_infantpreeligibility_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantpreeligibility'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantpreeligibility'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '3', 'decimal_places': '2', 'blank': 'True'})
        },
        'mpepu_infant.infantprerandoloss': {
            'Meta': {'object_name': 'InfantPrerandoLoss'},
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'loss_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_loss': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'reason_loss_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantprerandolossaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantPrerandoLossAudit', 'db_table': "'mpepu_infant_infantprerandoloss_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'loss_code': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_loss': ('django.db.models.fields.TextField', [], {'max_length': '250'}),
            'reason_loss_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantprerandoloss'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantrandodeferral': {
            'Meta': {'object_name': 'InfantRandoDeferral'},
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_birth': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['mpepu_infant.InfantBirth']", 'unique': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        'mpepu_infant.infantrandodeferralaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantRandoDeferralAudit', 'db_table': "'mpepu_infant_infantrandodeferral_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'anemia_neutropenia': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'clinical_jaundice': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_birth': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrandodeferral'", 'to': "orm['mpepu_infant.InfantBirth']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantrandodeferral'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        'mpepu_infant.infantrenalanomalyitems': {
            'Meta': {'object_name': 'InfantRenalAnomalyItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'renal_amomalies': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'renal_amomalies_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantrespiratorydefectitems': {
            'Meta': {'object_name': 'InfantRespiratoryDefectItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'respiratory_defect': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'respiratory_defects_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantskinabnormalitems': {
            'Meta': {'object_name': 'InfantSkinAbnormalItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'skin_abnormality': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'skin_abnormality_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrug': {
            'Meta': {'object_name': 'InfantStudyDrug'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_status': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_placebo_status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrugaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugAudit', 'db_table': "'mpepu_infant_infantstudydrug_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'drug_status': ('django.db.models.fields.CharField', [], {'max_length': '90'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydrug'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'on_placebo_status': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydruginit': {
            'Meta': {'object_name': 'InfantStudyDrugInit'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']"}),
            'initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_not_init': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'reason_not_init_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_not_survive': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydruginitaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugInitAudit', 'db_table': "'mpepu_infant_infantstudydruginit_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_dose_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydruginit'", 'to': "orm['mpepu_infant.InfantVisit']"}),
            'initiated': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'reason_not_init': ('django.db.models.fields.CharField', [], {'default': "'N/A'", 'max_length': '25'}),
            'reason_not_init_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'reason_not_survive': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrugitems': {
            'Meta': {'ordering': "['ingestion_date']", 'object_name': 'InfantStudyDrugItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'inf_study_drug': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantStudyDrug']"}),
            'ingestion_date': ('django.db.models.fields.DateField', [], {}),
            'modification_reason': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantstudydrugitemsaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantStudyDrugItemsAudit', 'db_table': "'mpepu_infant_infantstudydrugitems_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'dose_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'inf_study_drug': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantstudydrugitems'", 'to': "orm['mpepu_infant.InfantStudyDrug']"}),
            'ingestion_date': ('django.db.models.fields.DateField', [], {}),
            'modification_reason': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantsurvival': {
            'Meta': {'object_name': 'InfantSurvival'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_survival_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantsurvivalaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantSurvivalAudit', 'db_table': "'mpepu_infant_infantsurvival_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_survival_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'info_provider_other': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantsurvival'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infanttrisomieschromosomeitems': {
            'Meta': {'object_name': 'InfantTrisomiesChromosomeItems'},
            'abnormality_status': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'congenital_anomalies': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantCongenitalAnomalies']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'triso_chromo_abnormal': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'triso_chromo_abnormal_other': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantverbalautopsy': {
            'Meta': {'object_name': 'InfantVerbalAutopsy'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_sign': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prop_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'sign_symptoms': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'source': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mpepu_list.AutopsyInfoSource']", 'max_length': '50', 'symmetrical': 'False'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantverbalautopsyaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantVerbalAutopsyAudit', 'db_table': "'mpepu_infant_infantverbalautopsy_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'first_sign': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'prop_cause': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantverbalautopsy'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'sign_symptoms': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantverbalautopsyitems': {
            'Meta': {'object_name': 'InfantVerbalAutopsyItems'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'onset_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'sign_symptom': ('django.db.models.fields.CharField', [], {'max_length': '70', 'null': 'True', 'blank': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'verbal_autopsy': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVerbalAutopsy']"})
        },
        'mpepu_infant.infantvisit': {
            'Meta': {'object_name': 'InfantVisit'},
            'appointment': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_appointment.Appointment']", 'unique': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'appointment': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantvisit'", 'to': "orm['bhp_appointment.Appointment']"}),
            'comments': ('django.db.models.fields.TextField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'date_last_alive': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
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
            'survival_status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantvitalstatus': {
            'Meta': {'object_name': 'InfantVitalStatus'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mpepu_infant.InfantVisit']", 'null': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['bhp_registration.RegisteredSubject']", 'unique': 'True'}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_infant.infantvitalstatusaudit': {
            'Meta': {'ordering': "['-_audit_timestamp']", 'object_name': 'InfantVitalStatusAudit', 'db_table': "'mpepu_infant_infantvitalstatus_audit'"},
            '_audit_change_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            '_audit_id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'primary_key': 'True'}),
            '_audit_subject_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            '_audit_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '36', 'blank': 'True'}),
            'infant_visit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantvitalstatus'", 'null': 'True', 'to': "orm['mpepu_infant.InfantVisit']"}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'registered_subject': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'_audit_infantvitalstatus'", 'to': "orm['bhp_registration.RegisteredSubject']"}),
            'report_datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        },
        'mpepu_list.autopsyinfosource': {
            'Meta': {'object_name': 'AutopsyInfoSource'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'display_index': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'field_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'hostname_created': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'hostname_modified': ('django.db.models.fields.CharField', [], {'default': "'mac.local'", 'max_length': '50', 'db_index': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
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
            'user_created': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'}),
            'user_modified': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'db_index': 'True'})
        }
    }

    complete_apps = ['mpepu_infant']