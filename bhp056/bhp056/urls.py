from dajaxice.core import dajaxice_autodiscover

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.conf import settings
from django.views.generic import RedirectView
from django.db.models import get_models
import django_databrowse

# from edc.subject.rule_groups.classes import site_rule_groups
from edc.subject.lab_tracker.classes import site_lab_tracker
from edc.core.bhp_data_manager.classes import data_manager
from edc.dashboard.section.classes import site_sections
from edc.subject.visit_schedule.classes import site_visit_schedules
from apps.mpepu.mpepu_app_configuration.classes import MpepuAppConfiguration

dajaxice_autodiscover()
site_lab_tracker.autodiscover()
data_manager.prepare()
admin.autodiscover()
# site_rule_groups.autodiscover()
site_sections.autodiscover()
site_visit_schedules.autodiscover()
site_visit_schedules.build_all()
MpepuAppConfiguration()

APP_NAME = settings.APP_NAME

for model in get_models():
    try:
        django_databrowse.site.register(model)
    except:
        pass

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/logout/$', RedirectView.as_view(url='/{app_name}/logout/'.format(app_name=APP_NAME))),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

urlpatterns += patterns('',
    url(r'^databrowse/(.*)', login_required(django_databrowse.site.root)),
    #url(r'^databrowse/(?P<app_label>.*)/(?P<model_name>.*)/objects/(?P<pk>.*)/$', login_required(django_databrowse.site.root), name='databrowse'),
)

# urlpatterns += patterns('',
#     (r'^bhp_sync/', include('edc.device.sync.urls')),
# )

urlpatterns += patterns('',
    url(r'^{app_name}/(?P<section_name>audit_trail)/'.format(app_name=APP_NAME),
        include('edc.audit.urls'), name="section_url_name"),
)

urlpatterns += patterns('',
    url(r'^{app_name}/section/statistics/'.format(app_name=APP_NAME),
         include('apps.mpepu_stats.urls'), name="stats_url_name"),
 )

urlpatterns += patterns('',
    url(r'^{app_name}/(?P<section_name>specimens)/'.format(app_name=APP_NAME),
        include('edc.lab.lab_clinic_api.urls'), name="section_url_name"),
)

urlpatterns += patterns('',
    url(r'^{app_name}/dashboard/'.format(app_name=APP_NAME), include('apps.{app_name}_dashboard.urls'.format(app_name=APP_NAME))),
)

urlpatterns += patterns('',
    url(r'^{app_name}/login/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.login',
        name='{app_name}_login'.format(app_name=APP_NAME)),
    url(r'^{app_name}/logout/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.logout_then_login',
        name='{app_name}_logout'.format(app_name=APP_NAME)),
    url(r'^{app_name}/password_change/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.password_change',
        name='password_change_url'.format(app_name=APP_NAME)),
    url(r'^{app_name}/password_change_done/'.format(app_name=APP_NAME),
        'django.contrib.auth.views.password_change_done',
        name='password_change_done'.format(app_name=APP_NAME)),
)
urlpatterns += patterns('',
    url(r'^{app_name}/section/'.format(app_name=APP_NAME), include('edc.dashboard.section.urls'), name='section'),
)

urlpatterns += patterns('',
    url(r'^{app_name}/$'.format(app_name=APP_NAME), RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
    url(r'', RedirectView.as_view(url='/{app_name}/section/'.format(app_name=APP_NAME))),
    )
# from django.conf import settings
# from django.conf.urls import include, patterns, url
#
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += patterns('',
#         url(r'^__debug__/', include(debug_toolbar.urls)),
#     )
#     urlpatterns += patterns('django.contrib.staticfiles.views',
#         url(r'^static/(?P<path>.*)$', 'serve'),
#     )
