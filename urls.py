from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
import databrowse
from django.db.models import get_models
#from django.contrib.auth.views import logout, login, password_change
from django.views.generic.simple import redirect_to
from django.contrib.auth.decorators import login_required
#from autocomplete.views import autocomplete
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from dajaxice.core import dajaxice_autodiscover

admin.autodiscover()
dajaxice_autodiscover()
for model in get_models():
    databrowse.site.register(model)

urlpatterns = staticfiles_urlpatterns()

urlpatterns += patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/logout/$', redirect_to, {'url':'/mpepu/logout/'}),
    (r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
)

urlpatterns += patterns('',
    (r'^databrowse/(.*)', login_required(databrowse.site.root)),
)

urlpatterns += patterns('',
    (r'^audit_trail/', include('audit_trail.urls')),
    (r'^mpepu/audit_trail/', include('audit_trail.urls')),    
)

urlpatterns += patterns('',
    url(r'^mpepu/(?P<section_name>statistics)/',include('mpepu_stats.urls'), name="section_url_name"),
)

urlpatterns += patterns('',
    url(r'^mpepu/(?P<section_name>specimens)/',include('lab_clinic_api.urls'), name="section_url_name"),
)


urlpatterns += patterns('',
    url(r'^mpepu/dashboard/', include('mpepu_dashboard.urls')),
)

urlpatterns += patterns('',
    url(r'^mpepu/login/', 'django.contrib.auth.views.login', name='mpepu_login'),
    url(r'^mpepu/logout/', 'django.contrib.auth.views.logout_then_login', name='mpepu_logout'),
    url(r'^mpepu/passwordchange/', 'django.contrib.auth.views.password_change', name='mpepu_password_change'),
    url(r'^mpepu/passwordchangedone/', 'django.contrib.auth.views.password_change_done', name='mpepu_password_change_done'),                            
    url(r'^mpepu/', include('mpepu.urls'), name='home'),
    url(r'', include('mpepu.urls'), name='index'),    
)

    

"""
urlpatterns += patterns('',
    (r'^accounts/login/$', include(admin.site.urls)),
    (r'^accounts/profile/$', redirect_to, {'url': '/mpepu/'}),
    (r'^accounts/profile/logout', 'django.contrib.auth.views.login'),
)
"""

