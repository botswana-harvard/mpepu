from datetime import *
from dateutil.relativedelta import *
from django import template
from django.core.urlresolvers import reverse
from django.db.models import get_model 


register = template.Library()

@register.filter(name='admin_url_for_infant_dashboard')
def admin_url_for_infant_dashboard(contenttype, visit_pk):
    """Return a url to add or change an admin entry form via the infant dashboard based on visit_pk

    in order for this to work for a model, the ModelAdmin must catch the GET next parameter, so you need to add this:
    
        def change_view(self, request, object_id, extra_context=None):

            result = super(MaternalEnrollAdmin, self).change_view(request, object_id, extra_context)

            if request.GET.get('next'):
                kwargs={}
                for k in request.GET.iterkeys():
                    kwargs[str(k)]=''.join(unicode(i) for i in request.GET.get(k))
                del kwargs['next']
                result['Location'] = reverse(request.GET.get('next'),kwargs=kwargs )
            
            return result     


    this method refers to visit model, so it assumes these parameters in order to get to the named url:
    * next = infant_dashboard_visit_url
    * dashboard = 'infant'

    takes these from given visit model
    * subject_identifier = (comes from visit model)
    * visit_code = (comes from visit model)
   
    """
    
    dashboard_type = 'infant'
    app_label = 'mpepu_infant'
    
    if contenttype.model_class().objects.filter(visit = visit_pk):
        """the link is for a change"""
        """ these next two lines would change if for another dashboard_type and another visit model """
        next = '%s_dashboard_visit_url' % dashboard_type       
        model = contenttype.model_class().objects.get(visit = visit_pk)
        visit_model = model.visit        
        """ do reverse url """
        view = 'admin:%s_%s_change' % (contenttype.app_label, contenttype.model)
        view = str(view)
        rev_url = reverse(view, args=(model.pk,))
        """ add GET string to rev_url so that you will return to the dashboard ...whence you came... assuming you catch "next" in change_view"""
        rev_url = '%s?next=%s&dashboard_type=%s&subject_identifier=%s&visit_code=%s&visit_instance=%s' % (rev_url, next, dashboard_type, visit_model.appointment.registered_subject.subject_identifier, visit_model.appointment.visit_definition.code, visit_model.appointment.visit_instance )            
    else:
        """ the link is for an add"""
        next = '%s_dashboard_visit_add_url' % dashboard_type               
        visit_model = get_model(app_label, 'Visit').objects.get(pk = visit_pk)
        view = 'admin:%s_%s_add' % (contenttype.app_label, contenttype.model)
        view = str(view)
        try:
            rev_url = reverse(view)
            rev_url = '%s?visit=%s&next=%s&dashboard_type=%s&subject_identifier=%s&visit_code=%s&visit_instance=%s' % (rev_url, visit_pk, next, dashboard_type, visit_model.appointment.registered_subject.subject_identifier, visit_model.appointment.visit_definition.code, visit_model.appointment.visit_instance)            
        except:
            raise TypeError('NoReverseMatch while rendering reverse for %s_%s in admin_url_from_contenttype. Is model registered in admin?' % (contenttype.app_label, contenttype.model))    
    return rev_url

