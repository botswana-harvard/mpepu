from django.contrib import admin

from edc.base.modeladmin.admin import BaseTabularInline, BaseModelAdmin

from .maternal_visit_model_admin import MaternalVisitModelAdmin
from ..models import MaternalArvPreg, MaternalArv, MaternalArvPregHistory
from ..forms import (MaternalArvPPHistoryForm, MaternalArvPregHistoryForm, MaternalArvPostModForm,
                                  MaternalArvPostForm, MaternalArvPostAdhForm, MaternalArvPregForm)
from ..models import (MaternalArvPPHistory, MaternalArvPostMod, MaternalArvPost, MaternalArvPostAdh,
                    MaternalVisit)


class MyMaternalArvPPHistoryAdmin (MaternalVisitModelAdmin):

    """ For other sections of MaternalArvPregHistory; that is, related to MaternalArvPreg model. """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_arv_preg":
            kwargs["queryset"] = MaternalArvPreg.objects.filter(maternal_visit__exact=request.GET.get('maternal_visit', 0))
        return super(MyMaternalArvPPHistoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # override to disallow subject to be changed
#     def get_readonly_fields(self, request, obj=None):
# 
#         self.readonly_fields = super(MyMaternalArvPPHistoryAdmin, self).get_readonly_fields(request, obj)
# 
#         if obj:  # In edit mode
#             return ('maternal_arv_preg',) + self.readonly_fields
#         else:
#             return self.readonly_fields


class MyMaternalArvPregHistoryAdmin (MaternalVisitModelAdmin):

    """ For other sections of MaternalArvPregHistory; that is, related to MaternalArvPreg model. """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_arv_preg":
            kwargs["queryset"] = MaternalArvPreg.objects.filter(maternal_visit__exact=request.GET.get('maternal_visit', 0))
        return super(MyMaternalArvPregHistoryAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # override to disallow subject to be changed
#     def get_readonly_fields(self, request, obj=None):
# 
#         self.readonly_fields = super(MyMaternalArvPregHistoryAdmin, self).get_readonly_fields(request, obj)
# 
#         if obj:  # In edit mode
#             return ('maternal_arv_preg',) + self.readonly_fields
#         else:
#             return self.readonly_fields


class MyMaternalArvPostModelAdmin (MaternalVisitModelAdmin):

    """ For other sections of MaternalEnroll; that is, related to MaternalArvPost model. """

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_arv_post":
            kwargs["queryset"] = MaternalArvPost.objects.filter(maternal_visit__exact=request.GET.get('maternal_visit', 0))
        return super(MyMaternalArvPostModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    # override to disallow subject to be changed
#     def get_readonly_fields(self, request, obj=None):
#         if obj:  # In edit mode
#             return ('maternal_arv_post',) + self.readonly_fields
#         else:
#             return self.readonly_fields


class MaternalArvInlineAdmin(BaseTabularInline):

    model = MaternalArv
    fields = ('arv_code', 'date_start', 'date_stop',)
    extra = 1


class MaternalArvAdmin(BaseModelAdmin):

    fields = (
        "arv_code",
        "date_start",
        "date_stop",
        "maternal_arv_preg_history",
        "maternal_arv_pp_history",
        "transaction_flag")
    radio_fields = {"arv_code": admin.VERTICAL}
    list_filter = ('arv_code', 'date_start', 'date_stop', 'transaction_flag')
    search_fields = ("maternal_arv_preg_history__maternal_visit__appointment__registered_subject__subject_identifier",)
    list_display = ("maternal_arv_preg_history", "arv_code", "date_start", "date_stop", "transaction_flag")
admin.site.register(MaternalArv, MaternalArvAdmin)


class MaternalArvPregAdmin(MaternalVisitModelAdmin):

    form = MaternalArvPregForm
    fields = (
        "maternal_visit",
        "took_arv",
        "sd_nvp",
        "start_pp")
    radio_fields = {
        "took_arv": admin.VERTICAL,
        "sd_nvp": admin.VERTICAL,
        "start_pp": admin.VERTICAL}
admin.site.register(MaternalArvPreg, MaternalArvPregAdmin)


class MaternalArvPregHistoryAdmin(MyMaternalArvPregHistoryAdmin):

    form = MaternalArvPregHistoryForm
    fields = (
        "maternal_visit",
        "maternal_arv_preg",
        "is_interrupt",
        "interrupt",
        "interrupt_other",
        "comment")
    radio_fields = {
        "is_interrupt": admin.VERTICAL,
        "interrupt": admin.VERTICAL, }
    inlines = [MaternalArvInlineAdmin, ]
admin.site.register(MaternalArvPregHistory, MaternalArvPregHistoryAdmin)


class MaternalArvPPHistoryAdmin(MyMaternalArvPPHistoryAdmin):

    form = MaternalArvPPHistoryForm
    fields = (
        "maternal_visit",
        "maternal_arv_preg",
        "comment")
    inlines = [MaternalArvInlineAdmin, ]
admin.site.register(MaternalArvPPHistory, MaternalArvPPHistoryAdmin)


class MaternalArvPostModInlineAdmin(BaseTabularInline):

    model = MaternalArvPostMod
    form = MaternalArvPostModForm
    extra = 1


class MaternalArvPostAdmin(MaternalVisitModelAdmin):

    form = MaternalArvPostForm

    fields = (
        "maternal_visit",
        "haart_last_visit",
        "haart_reason",
        "haart_reason_other",
        "arv_status"
    )

    radio_fields = {
        "haart_last_visit": admin.VERTICAL,
        "haart_reason": admin.VERTICAL,
        "arv_status": admin.VERTICAL}
    inlines = [MaternalArvPostModInlineAdmin, ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_visit":
            if request.GET.get('maternal_visit'):
                kwargs["queryset"] = MaternalVisit.objects.filter(id=request.GET.get('maternal_visit'))

        return super(MaternalArvPostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(MaternalArvPost, MaternalArvPostAdmin)


class MaternalArvPostModAdmin(BaseModelAdmin):

    form = MaternalArvPostModForm
    list_display = ('maternal_arv_post', 'arv_code', 'dose_status', 'modification_date', 'modification_code')

admin.site.register(MaternalArvPostMod, MaternalArvPostModAdmin)


class MaternalArvPostAdhAdmin(MyMaternalArvPostModelAdmin):

    form = MaternalArvPostAdhForm
    fields = (
        "maternal_visit",
        "maternal_arv_post",
        "missed_doses",
        "missed_days",
        "missed_days_discnt",
        "comment")
admin.site.register(MaternalArvPostAdh, MaternalArvPostAdhAdmin)
