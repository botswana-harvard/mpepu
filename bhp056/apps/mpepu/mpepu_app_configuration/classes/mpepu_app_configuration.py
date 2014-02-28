from datetime import datetime

from edc.apps.app_configuration.classes import BaseAppConfiguration
from edc.core.bhp_content_type_map.models import ContentTypeMap
study_start_datetime = datetime(2011, 05, 10, 8, 00, 00)
study_end_datetime = datetime(2016, 01, 20, 23, 49, 40)


class MpepuAppConfiguration(BaseAppConfiguration):

    def __init__(self):
        super(MpepuAppConfiguration, self).__init__()

    appointment_configuration = {
                'allowed_iso_weekdays': '12345',
                'use_same_weekday': True,
                'default_appt_type': 'default'}

    study_variables_setup = {
                'protocol_number': 'BHP056',
                'protocol_code': '056',
                'protocol_title': 'BHP056',
                'research_title': 'BHP056',
                'study_start_datetime': study_start_datetime,
                'minimum_age_of_consent': 16,
                'maximum_age_of_consent': 64,
                'gender_of_consent': 'F',
                'subject_identifier_seed': '10000',
                'subject_identifier_prefix': '056',
                'subject_identifier_modulus': '7',
                'subject_type': 'subject',
                'machine_type': 'SERVER',
                'hostname_prefix': 's007',
                'device_id': '0'}

    v1_consent_catalogue_setup = {
                'name': 'mpepu',
                # TO DO: how do we call a ContentTypeMap here???
#                 'content_type_map': 'Maternal Consent',
                'consent_type': 'study',
                'version': 1,
                'start_datetime': study_start_datetime,
                'end_datetime': study_end_datetime,
                'add_for_app': 'mpepu_maternal'}

    v2_consent_catalogue_setup = {
                'name': 'mpepu',
#                 'content_type_map': ContentTypeMap.objects.get(name='Maternal Consent'),
                'consent_type': 'study',
                'version': 2,
                'start_datetime': datetime(2013, 01, 21, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    v3_consent_catalogue_setup = {
                'name': 'mpepu',
                # TO DO: how do we call a ContentTypeMap here???
#                 'content_type_map': '',
                'consent_type': 'study',
                'version': 3,
                'start_datetime': datetime(2013, 8, 24, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    v4_consent_catalogue_setup = {
                'name': 'mpepu',
                # TO DO: how do we call a ContentTypeMap here???
#                 'content_type_map': '',
                'consent_type': 'study',
                'version': 4,
                'start_datetime': datetime(2014, 03, 10, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    consent_catalogue_list = [v1_consent_catalogue_setup, v2_consent_catalogue_setup, v3_consent_catalogue_setup, v4_consent_catalogue_setup]
