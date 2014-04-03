from datetime import datetime

from edc.apps.app_configuration.classes import BaseAppConfiguration

from edc.lab.lab_profile.classes import ProfileItemTuple, ProfileTuple

from lis.specimen.lab_aliquot_list.classes import AliquotTypeTuple
from lis.specimen.lab_panel.classes import PanelTuple
from lis.labeling.classes import LabelPrinterTuple

study_start_datetime = datetime(2011, 05, 10, 8, 00, 00)
study_end_datetime = datetime(2016, 01, 20, 23, 49, 40)


class MpepuAppConfiguration(BaseAppConfiguration):

    def __init__(self):
        super(MpepuAppConfiguration, self).__init__()

    global_configuration = {'dashboard': {'show_not_required_metadata': True, 'allow_additional_requisitions': False, 'show_drop_down_requisitions': True, 'drop_down_list_entries': True},
                            'appointment': {'allowed_iso_weekdays': '1234567', 'use_same_weekday': True, 'default_appt_type': 'default'},
                                 }

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
                'content_type_map': 'maternalconsent',
                'consent_type': 'study',
                'version': 1,
                'start_datetime': study_start_datetime,
                'end_datetime': study_end_datetime,
                'add_for_app': 'mpepu_maternal'}

    v2_consent_catalogue_setup = {
                'name': 'mpepu',
                'content_type_map': 'maternalconsent',
                'consent_type': 'study',
                'version': 2,
                'start_datetime': datetime(2013, 01, 21, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    v3_consent_catalogue_setup = {
                'name': 'mpepu',
                'content_type_map': 'maternalconsent',
                'consent_type': 'study',
                'version': 3,
                'start_datetime': datetime(2013, 8, 24, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    v4_consent_catalogue_setup = {
                'name': 'mpepu_v4',
                'content_type_map': 'maternalconsent',
                'consent_type': 'study',
                'version': 4,
                'start_datetime': datetime(2014, 03, 10, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    v4_1_consent_catalogue_setup = {
                'name': 'mpepu_arv',
                'content_type_map': 'resistanceconsent',
                'consent_type': 'sub-study',
                'version': 1,
                'start_datetime': datetime(2014, 03, 03, 07, 00, 00),
                'end_datetime': datetime(2016, 01, 20, 23, 51, 06),
                'add_for_app': 'mpepu_maternal'}

    study_site_setup = {'site_name': 'Gaborone',
                        'site_code': '4'}
#                         {'site_name': 'Lobatse',
#                          'site_code': '3'},
#                         {'site_name': 'Mochudi',
#                          'site_code': '2'},
#                         {'site_name': 'Molepolole',
#                          'site_code': '1'}

    lab_clinic_api_setup = {
        'panel': [PanelTuple('BHP023  HEMATOLOGY', 'TEST', 'WB'),
                  PanelTuple('Chromosonal Analysis', 'TEST', 'WB'),
                  PanelTuple('PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB'),
                  PanelTuple('PHM Viral load (amplicore >400)', 'TEST', 'WB'),
                  PanelTuple('CD4 (ARV)', 'TEST', 'WB'),
                  PanelTuple('Breast Milk (Storage)', 'STORAGE', 'BM'),
                  PanelTuple('Basic Chemistry + Glucose', 'TEST', 'WB'),
                  PanelTuple('PHS Ultrasensetive Viral Load', 'TEST', 'WB'),
                  PanelTuple('DNA PCR', 'TEST', 'WB'),
                  PanelTuple('Confirmatory Viral Load', 'TEST', 'WB'),
                  PanelTuple('Bana 01 Chemistry', 'TEST', 'WB'),
                  PanelTuple('Viral load (storage only)', 'STORAGE', 'WB'),
                  PanelTuple('Hepatitis B only', 'TEST', 'WB'),
                  PanelTuple('ELISA', 'TEST', 'WB'),
                  PanelTuple('Hematology (ARV)', 'TEST', 'WB'),
                  PanelTuple('Chemistry NVP/LFT + ALPL6 (ARV)', 'TEST', 'WB'),
                  PanelTuple('RT-PCR', 'TEST', 'WB'),
                  PanelTuple('PHS Ultrasensitive Viral Load (>50)', 'TEST', 'WB'),
                  PanelTuple('PHS: Ultrasensetive Viral Load', 'TEST', 'WB'),
                  PanelTuple('Plasma and Buffy Coat Storage', 'STORAGE', 'WB'),
                  PanelTuple('HIV Western Blot', 'TEST', 'WB'),
                  PanelTuple('Stool storage', 'STORAGE', 'ST'),
                  PanelTuple('ARV Resistance Testing', 'TEST', 'WB')],
        'aliquot_type': [AliquotTypeTuple('Whole Blood', 'WB', '02'),
                         AliquotTypeTuple('Plasma', 'PL', '32'),
                         AliquotTypeTuple('Serum', 'SERUM', '06'),
                         AliquotTypeTuple('Breast Milk: Whole', 'BM', '20'),
                         AliquotTypeTuple('Stool', 'ST', '01')]}

    lab_setup = {'mpepu': {
                    'panel': [PanelTuple('BHP023  HEMATOLOGY', 'TEST', 'WB'),
                              PanelTuple('Chromosonal Analysis', 'TEST', 'WB'),
                              PanelTuple('PBMC Plasma (STORE ONLY)', 'STORAGE', 'WB'),
                              PanelTuple('PHM Viral load (amplicore >400)', 'TEST', 'WB'),
                              PanelTuple('CD4 (ARV)', 'TEST', 'WB'),
                              PanelTuple('Breast Milk (Storage)', 'STORAGE', 'BM'),
                              PanelTuple('Basic Chemistry + Glucose', 'TEST', 'WB'),
                              PanelTuple('PHS Ultrasensetive Viral Load', 'TEST', 'WB'),
                              PanelTuple('DNA PCR', 'TEST', 'WB'),
                              PanelTuple('Confirmatory Viral Load', 'TEST', 'WB'),
                              PanelTuple('Bana 01 Chemistry', 'TEST', 'WB'),
                              PanelTuple('Viral load (storage only)', 'STORAGE', 'WB'),
                              PanelTuple('Hepatitis B only', 'TEST', 'WB'),
                              PanelTuple('ELISA', 'TEST', 'WB'),
                              PanelTuple('Hematology (ARV)', 'TEST', 'WB'),
                              PanelTuple('Chemistry NVP/LFT + ALPL6 (ARV)', 'TEST', 'WB'),
                              PanelTuple('RT-PCR', 'TEST', 'WB'),
                              PanelTuple('PHS Ultrasensitive Viral Load (>50)', 'TEST', 'WB'),
                              PanelTuple('PHS: Ultrasensetive Viral Load', 'TEST', 'WB'),
                              PanelTuple('Plasma and Buffy Coat Storage', 'STORAGE', 'WB'),
                              PanelTuple('HIV Western Blot', 'TEST', 'WB'),
                              PanelTuple('Stool storage', 'STORAGE', 'ST'),
                              PanelTuple('ARV Resistance Testing', 'TEST', 'WB')],
                    'aliquot_type': [AliquotTypeTuple('Whole Blood', 'WB', '02'),
                                     AliquotTypeTuple('Plasma', 'PL', '32'),
                                     AliquotTypeTuple('Serum', 'SERUM', '06'),
                                     AliquotTypeTuple('Breast Milk: Whole', 'BM', '20'),
                                     AliquotTypeTuple('Stool', 'ST', '01')],
                     'profile': [ProfileTuple('PBMC Plasma (STORE ONLY)', 'WB'), ProfileTuple('Plasma and Buffy Coat Storage', 'WB')],
                     'profile_item': [ProfileItemTuple('PBMC Plasma (STORE ONLY)', 'PL', 0.1, 3),
                                      ProfileItemTuple('Plasma and Buffy Coat Storage', 'PL', 0.1, 3)]}}

    labeling = {'label_printer': [LabelPrinterTuple('Zebra_Technologies_ZTC_GK420t', '127.0.0.1', True), ], }

    consent_catalogue_list = [v1_consent_catalogue_setup, v2_consent_catalogue_setup, v3_consent_catalogue_setup, v4_consent_catalogue_setup, v4_1_consent_catalogue_setup]
