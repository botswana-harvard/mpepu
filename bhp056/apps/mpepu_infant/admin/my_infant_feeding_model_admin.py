from ..models import InfantFeeding
from .infant_visit_model_admin import InfantVisitModelAdmin


class MyInfantFeedingModelAdmin (InfantVisitModelAdmin):

    """ For other sections of InfantFeeding; that is, related to InfantFeeding model. """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "infant_feeding":
            kwargs["queryset"] = InfantFeeding.objects.filter(infant_visit__exact=request.GET.get('infant_visit', 0))
        return super(MyInfantFeedingModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):

        self.readonly_fields = super(MyInfantFeedingModelAdmin, self).get_readonly_fields(request, obj)

        if obj:  # In edit mode
            return ('infant_feeding',) + self.readonly_fields
        else:
            return self.readonly_fields
