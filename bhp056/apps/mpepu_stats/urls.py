from django.conf.urls import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('edc.core.model_data_inspector.views.model_group_describer',
    url(r'^model_describer/', 'model_group_describer', name="model_describer_url_name" ),
    )

urlpatterns += patterns('apps.mpepu_stats.views',
    url(r'^$', 'index', name="stats_home_url" ),
    url(r'^potential_randos_report/', 'potential_randos_report', name="report_url_name"),
    url(r'^infant_death_report/', 'infant_death_report', name="report_url_name"),
    url(r'^infant_hospitalization/', 'infant_hospitalization', name="report_url_name"),
    url(r'^infant_diagnoses/', 'infant_diagnoses', name="report_url_name"),
    url(r'^model_group_describer/(?P<common_foreign_key_field_name>registered_subject|maternal_visit|infant_visit)/$', 'model_group_describer', name="model_group_describer_url_name" ),
    url(r'^eligible_infants/$', 'eligible_infants', name="eligible_infants_path"),
    )
