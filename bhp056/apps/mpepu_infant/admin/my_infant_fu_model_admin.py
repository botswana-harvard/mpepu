from ..models import InfantFu
from .infant_visit_model_admin import InfantVisitModelAdmin


class MyInfantFuModelAdmin (InfantVisitModelAdmin):

    """ For other sections of InfantFu; that is, related to InfantFu model. """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_fu":
            kwargs["queryset"] = InfantFu.objects.filter(infant_visit__exact=request.GET.get('infant_visit', 0))
        return super(MyInfantFuModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):

        self.readonly_fields = super(MyInfantFuModelAdmin, self).get_readonly_fields(request, obj)

        if obj:  # In edit mode
            return ('infant_fu',) + self.readonly_fields
        else:
            return self.readonly_fields
