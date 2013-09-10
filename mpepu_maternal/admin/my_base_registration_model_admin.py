from bhp_base_admin.admin import BaseModelAdmin
from bhp_registration.models import RegisteredSubject


class MyBaseRegistrationModelAdmin (BaseModelAdmin):

    """Model Admin for models with a foreignkey to the maternal consent model that are maternal eligibility forms"""

    # override, limit dropdown in add_view to id passed in the URL
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        # raise TypeError(request.GET.get('registered_subject'))
        if db_field.name == "registered_subject":
            if request.GET.get('registered_subject'):
                kwargs["queryset"] = RegisteredSubject.objects.filter(pk=request.GET.get('registered_subject'))

        super(MyBaseRegistrationModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):

        self.readonly_fields = super(MyBaseRegistrationModelAdmin, self).get_readonly_fields(request, obj)

        if obj:  # In edit mode
            return ('registration_datetime',) + self.readonly_fields
        else:
            return self.readonly_fields
