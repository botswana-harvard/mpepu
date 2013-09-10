# from django.conf.urls.defaults import patterns, url, include
# from django.conf import settings
# 
# from mpepu.classes import SearchByWord, SearchByDate, SearchByWeek
# 
# app_name = settings.APP_NAME
# 
# section_names = ('mother', 'appointment', 'maternal', 'randomize',
#                  'infant', 'statistics', 'administration')
# 
# urlpatterns = SearchByWord().urlpatterns(section_names)
# urlpatterns += SearchByDate().urlpatterns(section_names)
# urlpatterns += SearchByWeek().urlpatterns(section_names)
# 
# urlpatterns += patterns('{app_name}.views'.format(app_name=app_name),
# 
#     url(r'^(?P<section_name>{section_names})/$'.format(section_names='|'.join(section_names)),
#         'section_index',
#         name="section_url_name"
#         ),
#     url(r'^(?P<section_name>{section_names})/search/(?P<search_name>maternalconsent|infantbirth|appointment)/$'.format(section_names='|'.join(section_names)),
#         'section_index',
#         name="section_search_url_name"
#         ),
#     url(r'^urls/{app_name}_dashboard/$'.format(app_name=app_name), include('{app_name}_dashboard.urls'.format(app_name=app_name))),
#     url(r'^',
#         'index',
#         name="home_url_name"
#         ),
# )
