from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .classes import MaternalDashboard, InfantDashboard


urlpatterns = []

# regex = {}
# regex['dashboard_type'] = 'infant'
# regex['dashboard_model'] = 'infant_birth'
# urlpatterns = InfantDashboard.get_urlpatterns('apps.mpepu_dashboard.views', regex, visit_field_names=['infant_visit', ])
# 
# regex = {}
# regex['dashboard_type'] = 'maternal'
# regex['dashboard_model'] = 'maternal_consent'
# urlpatterns += MaternalDashboard.get_urlpatterns('apps.mpepu_dashboard.views', regex, visit_field_names=['maternal_visit', ])


for pattern in MaternalDashboard.get_urlpatterns():
    urlpatterns.append(
        url(
            pattern,
            login_required(MaternalDashboard.as_view()),
            name=MaternalDashboard.dashboard_url_name
            )
    )

for pattern in InfantDashboard.get_urlpatterns():
    urlpatterns.append(
        url(
            pattern,
            login_required(InfantDashboard.as_view()),
            name=InfantDashboard.dashboard_url_name
            )
    )
