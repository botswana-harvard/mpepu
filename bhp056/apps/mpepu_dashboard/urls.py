from .classes import MaternalDashboard, InfantDashboard

regex = {}
regex['dashboard_type'] = 'infant'
regex['dashboard_model'] = 'infant_birth'
urlpatterns = InfantDashboard.get_urlpatterns('apps.mpepu_dashboard.views', regex, visit_field_names=['infant_visit', ])

regex = {}
regex['dashboard_type'] = 'maternal'
regex['dashboard_model'] = 'maternal_consent'
urlpatterns += MaternalDashboard.get_urlpatterns('apps.mpepu_dashboard.views', regex, visit_field_names=['maternal_visit', ])
