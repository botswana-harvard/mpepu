from datetime import datetime

try:
    from config.labels import aliquot_label
except ImportError:
    aliquot_label = None

from edc.apps.app_configuration.classes import BaseAppConfiguration
from edc.core.bhp_variables.models import StudySpecific, StudySite
from edc.lab.lab_profile.classes import ProfileItemTuple, ProfileTuple

from lis.specimen.lab_aliquot_list.classes import AliquotTypeTuple
from lis.specimen.lab_panel.classes import PanelTuple
from lis.labeling.classes import LabelPrinterTuple, ZplTemplateTuple, ClientTuple

study_start_datetime = datetime(2011, 05, 10, 8, 00, 00)
study_end_datetime = datetime(2016, 01, 20, 23, 49, 40)


class MpepuAppConfiguration(BaseAppConfiguration):

    def prepare(self):
        super(MpepuAppConfiguration, self).prepare()

    global_configuration = {'dashboard': {'show_not_required_metadata': False, 'allow_additional_requisitions': False, 'show_drop_down_requisitions': True},
                            'appointment': {'allowed_iso_weekdays': '12345', 'use_same_weekday': True, 'default_appt_type': 'default'},
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

    study_site_setup = [{'site_name': 'Gaborone', 'site_code': '4'},
                        {'site_name': 'Lobatse', 'site_code': '3'},
                        {'site_name': 'Mochudi', 'site_code': '2'},
                        {'site_name': 'Molepolole', 'site_code': '1'},
                        ]

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
                                     AliquotTypeTuple('Stool', 'ST', '01'),
                                     AliquotTypeTuple('Buffy Coat', 'BC', '16')
                                     ],
                    'profile': [ProfileTuple('Viral load (storage only)','WB'),
                                ProfileTuple('ARV Resistance Testing','WB'),
                                ProfileTuple('Plasma and Buffy Coat Storage (Infant)','WB'),
                                ProfileTuple('Plasma and Buffy Coat Storage (Maternal)','WB'),
                                ],
                    'profile_item': [ProfileItemTuple('Viral load (storage only)', 'PL', 1.8, 3),
                                     ProfileItemTuple('Viral load (storage only)', 'BC', 0.5, 1),
                                     ProfileItemTuple('ARV Resistance Testing','PL', 1.8, 3),
                                     ProfileItemTuple('ARV Resistance Testing','BC', 0.5, 1),
                                     ProfileItemTuple('Plasma and Buffy Coat Storage (Infant)','PL', 1.0, 1),
                                     ProfileItemTuple('Plasma and Buffy Coat Storage (Infant)','BC', 0.2, 1),
                                     ProfileItemTuple('Plasma and Buffy Coat Storage (Maternal)','PL', 1.8, 2),
                                     ProfileItemTuple('Plasma and Buffy Coat Storage (Maternal)','BC', 0.5, 2),
                                     ]
                    }}

    labeling_setup = {'label_printer': [LabelPrinterTuple('Zebra_Technologies_ZTC_GK420t', 'mpepu01', '192.168.1.63', False),
                                        LabelPrinterTuple('Mpepu_Pharmacy_Label_Printer', 'mpepu02',  '192.168.1.160', False),
                                        LabelPrinterTuple('Moleps_room2_Label_Printer', 'moleps16', '10.70.117.77', False),
                                        LabelPrinterTuple('Moleps_Pharmacy_Label_Printer', 'moleps17', '10.70.117.38', False),
                                        LabelPrinterTuple('zebra', 'fchilisa', 'localhost', False),
                                        ],
                      'client': [ClientTuple(hostname='mpepu08', aliases=None, ip=None, printer_name='Zebra_Technologies_ZTC_GK420t', cups_hostname='mpepu01',),
                                  ],
                      'zpl_template': [aliquot_label or ZplTemplateTuple(
                                'aliquot_label', (
                                    """^XA
                                    ^FO325,5^A0N,15,20^FD%(protocol)s Site %(site)s %(item_count)s/%(item_count_total)s^FS
                                    ^FO320,20^BY1,3.0^BCN,50,N,N,N
                                    ^BY^FD%(specimen_identifier)s^FS
                                    ^FO320,80^A0N,15,20^FD%(specimen_identifier)s [%(requisition_identifier)s]^FS
                                    ^FO325,100^A0N,15,20^FD%(panel)s %(aliquot_type)s^FS
                                    ^FO325,118^A0N,16,20^FD%(subject_identifier)s (%(initials)s)^FS
                                    ^FO325,136^A0N,16,20^FDDOB: %(dob)s %(gender)s^FS
                                    ^FO325,152^A0N,20^FD%(drawn_datetime)s^FS
                                    ^XZ"""
                                    ),
                                True),
                        ZplTemplateTuple(
                                'requisition_label', (
                                    """^XA
                                    ^FO325,5^A0N,15,20^FD${protocol} Site ${site} ${label_count}/${label_count_total}^FS
                                    ^FO320,20^BY1,3.0^BCN,50,N,N,N
                                    ^BY^FD${specimen_identifier}^FS
                                    ^FO320,80^A0N,15,20^FD${specimen_identifier} [${requisition_identifier}]^FS
                                    ^FO325,100^A0N,15,20^FD${panel} ${aliquot_type}^FS
                                    ^FO325,118^A0N,16,20^FD${subject_identifier} (${initials})^FS
                                    ^FO325,136^A0N,16,20^FDDOB: ${dob} ${gender}^FS
                                    ^FO325,152^A0N,20^FD${drawn_datetime}^FS
                                    ^XZ"""
                                    ),
                                True),
                        ZplTemplateTuple(
                                'dispensing', (
                                    """^XA
                                    ^FO100,25^A0N,25^FDBotswana-Harvard Partnership - SID ${sid}^FS
                                    ^FO100,50^BY2.0^BCN,50,N,N,N
                                    ^BY^FD${barcode_value}^FS
                                    ^FO100,120^A0N,20^FD${barcode_value}^FS
                                    ^FO100,150^A0N,30^FD${subject_identifier} [${initials}]^FS
                                    ^FO100,180^A0N,40^FD${treatment}^FS
                                    ^FO100,220^A0N,35^FDDosage: ${dose}^FS
                                    ^FO100,270^A0N,40^FD${packing_amount} ${packing_unit}^FS
                                    ^FO100,330^A0N,30^FDdispensed on ${dispense_date} by ${user_created}^FS
                                    ^XZ"""
                                    ),
                                True),
                                     ],
                      }

    consent_catalogue_list = [v1_consent_catalogue_setup, v2_consent_catalogue_setup, v3_consent_catalogue_setup, v4_consent_catalogue_setup, v4_1_consent_catalogue_setup]

    def update_or_create_study_variables(self):
        if StudySpecific.objects.all().count() == 0:
            StudySpecific.objects.create(**self.study_variables_setup)
        else:
            StudySpecific.objects.all().update(**self.study_variables_setup)
        self._setup_study_sites()

    def _setup_study_sites(self):
        for site in self.study_site_setup:
            try:
                StudySite.objects.get(**site)
            except StudySite.DoesNotExist:
                StudySite.objects.create(**site)
