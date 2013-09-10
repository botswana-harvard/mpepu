from bhp_dashboard_registered_subject.classes import RegisteredSubjectDashboard

dashboard = RegisteredSubjectDashboard()
regex = {}

regex['dashboard_type'] = 'infant'
regex['subject_identifier'] = '056\-[1234]{1}[0-9]{5,7}\-[0-9]{1}\-[0-9]{2}'
regex['visit_code'] = '\w+'
regex['visit_instance'] = '[0-9]{1}'

urlpatterns = dashboard.get_urlpatterns('mpepu_dashboard.views', regex, visit_field_names=['infant_visit'])

regex['dashboard_type'] = 'maternal'
regex['subject_identifier'] = '056\-[1234]{1}[0-9]{5,7}\-[0-9]{1}'
regex['visit_code'] = '\w+'
regex['visit_instance'] = '[0-9]{1}'

urlpatterns += dashboard.get_urlpatterns('mpepu_dashboard.views', regex, visit_field_names=['maternal_visit'])
