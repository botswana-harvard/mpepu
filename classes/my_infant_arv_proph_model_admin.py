from mpepu_infant.models import InfantArvProph
from infant_visit_model_admin import InfantVisitModelAdmin      
            
            
class MyInfantArvProphModelAdmin (InfantVisitModelAdmin):

    """ For other sections of InfantArvProph; that is, related to InfantArvProph model. """
 
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_arv_proph":
            kwargs["queryset"] = InfantArvProph.objects.filter(infant_visit__exact=request.GET.get('infant_visit', 0))
        return super(MyInfantArvProphModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)   
        
    #override to disallow subject to be changed
    def get_readonly_fields(self, request, obj = None):
    
        self.readonly_fields = super(MyInfantArvProphModelAdmin, self).get_readonly_fields(request, obj)    
    
        if obj: #In edit mode
            return ('infant_arv_proph',) + self.readonly_fields
        else:
            return self.readonly_fields                                  

