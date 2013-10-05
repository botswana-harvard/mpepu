# from datetime import *
# from dateutil.relativedelta import *
# from django import template
# from django.core.urlresolvers import reverse
# from ..models import MaternalVisit
# 
# register = template.Library()
# 
# @register.filter(name='admin_url_for_maternal_dashboard')
# def admin_url_for_maternal_dashboard(contenttype, maternal_visit_pk):
#     """Return a url to add or change an admin entry form via the maternal dashboard based on maternal_visit_pk
# 
#     in order for this to work for a model, the ModelAdmin must catch the GET next parameter, so you need to add this:
#     
#         def change_view(self, request, object_id, extra_context=None):
# 
#             result = super(MaternalEnrollAdmin, self).change_view(request, object_id, extra_context)
# 
#             if request.GET.get('next'):
#                 kwargs={}
#                 for k in request.GET.iterkeys():
#                     kwargs[str(k)]=''.join(unicode(i) for i in request.GET.get(k))
#                 del kwargs['next']
#                 result['Location'] = reverse(request.GET.get('next'),kwargs=kwargs )
#             
#             return result     
# 
# 
#     this method refers to maternal_visit model, so it assumes these parameters in order to get to the named url:
#     * next = maternal_dashboard_visit_url
#     * dashboard = 'maternal'
# 
#     takes these from given maternal_visit model
#     * subject_identifier = (comes from maternal_visit model)
#     * visit_code = (comes from maternal_visit model)
#    
#     """
#     
#     dashboard = 'maternal'
#     
#     if contenttype.model_class().objects.filter(maternal_visit = maternal_visit_pk):
#         """the link is for a change"""
#         """ these next two lines would change if for another dashboard and another visit model """
#         next = 'maternal_dashboard_visit_url'        
#         model = contenttype.model_class().objects.get(maternal_visit = maternal_visit_pk)
#         visit_model = model.maternal_visit        
#         """ do reverse url """
#         view = 'admin:%s_%s_change' % (contenttype.app_label, contenttype.model)
#         view = str(view)
#         rev_url = reverse(view, args=(model.pk,))
#         """ add GET string to rev_url so that you will return to the dashboard ...whence you came... assuming you catch "next" in change_view"""
#         rev_url = '%s?next=%s&dashboard=%s&subject_identifier=%s&visit_code=%s&visit_instance=%s' % (rev_url, next, dashboard, visit_model.appointment.registered_subject.subject_identifier, visit_model.appointment.visit_definition.code, visit_model.appointment.visit_instance )            
#     else:
#         """ the link is for an add"""
#         next = 'maternal_dashboard_visit_add_url'                
#         visit_model = MaternalVisit.objects.get(pk = maternal_visit_pk)
#         view = 'admin:%s_%s_add' % (contenttype.app_label, contenttype.model)
#         view = str(view)
#         try:
#             rev_url = reverse(view)
#             rev_url = '%s?maternal_visit=%s&next=%s&dashboard=%s&subject_identifier=%s&visit_code=%s&visit_instance=%s' % (rev_url, maternal_visit_pk, next, dashboard, visit_model.appointment.registered_subject.subject_identifier, visit_model.appointment.visit_definition.code,visit_model.appointment.visit_instance)            
#         except:
#             raise TypeError('NoReverseMatch while rendering reverse for %s_%s in admin_url_from_contenttype. Is model registered in admin?' % (contenttype.app_label, contenttype.model))    
#     return rev_url
#     
# """
#     
# @register.filter(name='admin_url_for_maternal_dashboard')
# def admin_url_for_maternal_dashboard(contenttype, maternal_visit_pk):
#     ""Return a url to add or change an admin entry form via the maternal dashboard based on maternal_visit_pk""
#     if contenttype.model_class().objects.filter(maternal_visit = maternal_visit_pk):
#         model = contenttype.model_class().objects.get(maternal_visit = maternal_visit_pk)
#         view = 'admin:%s_%s_change' % (contenttype.app_label, contenttype.model)
#         view = str(view)
#         rev_url = reverse(view, args=(model.pk,))
#         rev_url = '%s?%s' % (rev_url, 'next=maternal_dashboard_visit_url&dashboard=maternal')            
#         #else:
#         #    raise TypeError("Maternal_visit_pk is not None but does not exist for model '%s'. Got '%s'" % (contenttype.model, maternal_visit_pk))
#     else:
#         view = 'admin:%s_%s_add' % (contenttype.app_label, contenttype.model)
#         view = str(view)
#         try:
#             rev_url = reverse(view)
#             rev_url = '%s?maternal_visit=%s&%s' % (rev_url, maternal_visit_pk, 'next=maternal_dashboard_visit_url&dashboard=maternal')            
#         except:
#             raise TypeError('NoReverseMatch while rendering reverse for %s_%s in admin_url_from_contenttype. Is model registered in admin?' % (contenttype.app_label, contenttype.model))    
#     return rev_url
#     
# """
