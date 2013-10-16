# from django.conf.urls import patterns, url
from .classes import MaternalDashboard, InfantDashboard

# regex['dashboard_type'] = 'infant'
# regex['subject_identifier'] = '056\-[1234]{1}[0-9]{5,7}\-[0-9]{1}\-[0-9]{2}'
# regex['visit_code'] = '\w+'
# regex['visit_instance'] = '[0-9]{1}'
# regex['dashboard_type'] = 'maternal'
# regex['subject_identifier'] = '056\-[1234]{1}[0-9]{5,7}\-[0-9]{1}'
# regex['visit_code'] = '\w+'
# regex['visit_instance'] = '[0-9]{1}'

regex = {}
regex['dashboard_type'] = 'maternal'
regex['dashboard_model'] = 'maternal_consent'
urlpatterns = MaternalDashboard.get_urlpatterns('apps.mpepu_dashboard.views', regex, view='maternal_dashboard', visit_field_names=['maternal_visit', ])

regex = {}
regex['dashboard_type'] = 'infant'
regex['dashboard_model'] = 'infant_birth'
urlpatterns = InfantDashboard.get_urlpatterns('apps.mpepu_dashboard.views', regex, view='infant_dashboard', visit_field_names=['infant_visit', ])
