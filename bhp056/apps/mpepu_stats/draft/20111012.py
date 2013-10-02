"""

>>> infant_birth = InfantBirth.objects.values('registered_subject__study_site__site_name').filter(maternal_lab_del__maternal_visit__report_datetime__lt=cut_off).annotate(freq=Count('registered_subject__study_site__site_name'))
>>> infant_birth
[{'freq': 114, 'registered_subject__study_site__site_name': u'Molepolole'}, {'freq': 166, 'registered_subject__study_site__site_name': u'Gaborone'}, {'freq': 64, 'registered_subject__study_site__site_name': u'Lobatse'}]


>>>infant_birth = InfantBirth.objects.values('registered_subject__study_site__site_name','infantbirthfeed__feeding_after_delivery').filter(maternal_lab_del__maternal_visit__report_datetime__lt=cut_off).annotate(freq=Count('infantbirthfeed__feeding_after_delivery'))
>>>infant_birth

[{'infantbirthfeed__feeding_after_delivery': u'Formula feeding only',
 'freq': 83,
 'registered_subject__study_site__site_name': u'Molepolole'},

 {'infantbirthfeed__feeding_after_delivery': u'Formula feeding only',
 'freq': 150,
 'registered_subject__study_site__site_name': u'Gaborone'},

 {'infantbirthfeed__feeding_after_delivery': u'Breastfeeding only',
 'freq': 29,
 'registered_subject__study_site__site_name': u'Molepolole'},

 {'infantbirthfeed__feeding_after_delivery': u'Formula feeding only',
 'freq': 56,
 'registered_subject__study_site__site_name': u'Lobatse'},

 {'infantbirthfeed__feeding_after_delivery': u'Breastfeeding only',
 'freq': 7,
 'registered_subject__study_site__site_name': u'Lobatse'},

 {'infantbirthfeed__feeding_after_delivery': u'Breastfeeding only',
 'freq': 16,
 'registered_subject__study_site__site_name': u'Gaborone'},

 {'infantbirthfeed__feeding_after_delivery': None,
 'freq': 0,
 'registered_subject__study_site__site_name': u'Lobatse'},

 {'infantbirthfeed__feeding_after_delivery': u'Both breastfeeding and formula feeding',
 'freq': 1,
 'registered_subject__study_site__site_name': u'Molepolole'},

 {'infantbirthfeed__feeding_after_delivery': None,
 'freq': 0,
 'registered_subject__study_site__site_name': u'Molepolole'}]
 
>>>maternal_enroll = MaternalEnroll.objects.values('maternal_visit__appointment__registered_subject__study_site__site_name').filter(maternal_visit__report_datetime__lt=cut_off).annotate(freq=Count('maternal_visit__appointment__registered_subject__study_site__site_name'))
>>>maternal_enroll

[{'freq': 82, 'maternal_visit__appointment__registered_subject__study_site__site_name': u'Lobatse'}, 
{'freq': 122, 'maternal_visit__appointment__registered_subject__study_site__site_name': u'Molepolole'}, 
{'freq': 166, 'maternal_visit__appointment__registered_subject__study_site__site_name': u'Gaborone'}]

>>>maternal_lab_del = MaternalLabDel.objects.values('maternal_visit__appointment__registered_subject__study_site__site_name').filter(maternal_visit__report_datetime__lt=cut_off).annotate(freq=Count('maternal_visit__appointment__registered_subject__study_site__site_name'))
>>>maternal_lab_del

[{'freq': 114, 'maternal_visit__appointment__registered_subject__study_site__site_name': u'Molepolole'}, 
{'freq': 164, 'maternal_visit__appointment__registered_subject__study_site__site_name': u'Gaborone'}, 
{'freq': 65, 'maternal_visit__appointment__registered_subject__study_site__site_name': u'Lobatse'}]

>>> infant_rando = InfantRando.objects.values('rx').filter(randomization_datetime__lt=cut_off).annotate(freq=Count('rx'))
[{'freq': 119, 'rx': u'Placebo'}, {'freq': 118, 'rx': u'CTX'}]

>>>infant_birth = InfantBirth.objects.values('registered_subject__study_site__site_name').filter(maternal_lab_del__maternal_visit__report_datetime__lt=cut_off, infantbirthfeed__feeding_after_delivery__isnull=True).annotate(freq=Count('registered_subject__study_site__site_name'))
"""
