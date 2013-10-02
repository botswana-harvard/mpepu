from django.contrib import admin
from bhp_identifier.classes import InfantIdentifier
from bhp_base_admin.admin import BaseTabularInline, BaseModelAdmin
from mpepu_maternal.models import MaternalLabDel, MaternalLabDelMed, MaternalLabDelDx, MaternalLabDelDxT, MaternalLabDelClinic
from mpepu_maternal.forms import MaternalLabDelMedForm, MaternalLabDelClinicForm, MaternalLabDelDxForm, MaternalLabDelForm
from mpepu_maternal.filters import GaListFilter
from maternal_visit_model_admin import MaternalVisitModelAdmin


class BaseMaternalLabDelModelAdmin (MaternalVisitModelAdmin):
    """ For other sections of MaternalLabDel; that is, related to MaternalLabDel model. """
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "maternal_lab_del":
            kwargs["queryset"] = MaternalLabDel.objects.filter(maternal_visit__exact=request.GET.get('maternal_visit', 0))
        return super(BaseMaternalLabDelModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    #override to disallow subject to be changed
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('maternal_lab_del',) + self.readonly_fields
        else:
            return self.readonly_fields


class MaternalLabDelAdmin(MaternalVisitModelAdmin):
    
    form = MaternalLabDelForm

    def __init__(self, *args, **kwargs):
        super(MaternalLabDelAdmin, self).__init__(*args, **kwargs)
        self.list_filter.append(GaListFilter)

# moved to post save signal
#     def save_model(self, request, obj, form, change):
#
#         if not change:
#             obj.user_created = request.user
#             obj.save()
#             if obj.live_infants_to_register > 0:
#                 #Allocate Infant Identifier
#                 infant_identifier = InfantIdentifier()
#                 for self.infant_order in range(0, obj.live_infants_to_register):
#                     infant_identifier.get_identifier(
#                         add_check_digit=False,
#                         is_derived=True,
#                         maternal_identifier=obj.maternal_visit.appointment.registered_subject.subject_identifier,
#                         maternal_study_site=obj.maternal_visit.appointment.registered_subject.study_site,
#                         user=request.user,
#                         birth_order=self.infant_order,
#                         live_infants=obj.live_infants,
#                         live_infants_to_register=obj.live_infants_to_register,
#                         subject_type='infant')
#         return super(MaternalLabDelAdmin, self).save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if obj:  # In edit mode
            return ('visit', 'live_infants', 'delivery_datetime',) + self.readonly_fields
        else:
            return self.readonly_fields

    fields = (
        "maternal_visit",
        "delivery_datetime",
        "del_time_is_est",
        "labour_hrs",
        "del_mode",
        "has_ga",
        "ga",
        "del_hosp",
        "del_hosp_other",
        "has_urine_tender",
        "labr_max_temp",
        "has_chorioamnionitis",
        "has_del_comp",
        "del_comp",
        "del_comp_other",
        "live_infants",
        "live_infants_to_register",
        "still_borns",
        "still_born_has_congen_abn",
        "still_born_congen_abn",
        "del_comment",
        "comment")
    radio_fields = {
        "del_time_is_est": admin.VERTICAL,
        "labour_hrs": admin.VERTICAL,
        "del_mode": admin.VERTICAL,
        "del_hosp": admin.VERTICAL,
        "has_urine_tender": admin.VERTICAL,
        "has_chorioamnionitis": admin.VERTICAL,
        "has_del_comp": admin.VERTICAL,
        "still_born_has_congen_abn": admin.VERTICAL}
    filter_horizontal = ("del_comp",)
admin.site.register(MaternalLabDel, MaternalLabDelAdmin)


class MaternalLabDelMedAdmin(BaseMaternalLabDelModelAdmin):

    form = MaternalLabDelMedForm
    fields = (
        "maternal_visit",
        "maternal_lab_del",
        "has_health_cond",
        "health_cond",
        "health_cond_other",
        "has_ob_comp",
        "ob_comp",
        "ob_comp_other",
        "comment")
    radio_fields = {
        "has_health_cond": admin.VERTICAL,
        "has_ob_comp": admin.VERTICAL}
    filter_horizontal = (
        "health_cond",
        "ob_comp")
admin.site.register(MaternalLabDelMed, MaternalLabDelMedAdmin)


class MaternalLabDelDxTInlineAdmin(BaseTabularInline):
    model = MaternalLabDelDxT


class MaternalLabDelDxTAdmin(BaseModelAdmin):
    fields = (
        'lab_del_dx',
        'lab_del_dx_specify',
        'grade',
        'hospitalized')
admin.site.register(MaternalLabDelDxT, MaternalLabDelDxTAdmin)


class MaternalLabDelDxAdmin(BaseMaternalLabDelModelAdmin):

    form = MaternalLabDelDxForm
    fields = (
        "maternal_visit",
        "maternal_lab_del",
        "has_preg_dx",
        "has_who_dx",
        "wcs_dx_adult")
    radio_fields = {
        "has_preg_dx": admin.VERTICAL,
        "has_who_dx": admin.VERTICAL}
    filter_horizontal = ("wcs_dx_adult",)
    inlines = [MaternalLabDelDxTInlineAdmin, ]
admin.site.register(MaternalLabDelDx, MaternalLabDelDxAdmin)


class MaternalLabDelClinicAdmin(BaseMaternalLabDelModelAdmin):

    form = MaternalLabDelClinicForm
    fields = (
        "maternal_visit",
        "maternal_lab_del",
        "has_cd4",
        "cd4_date",
        "cd4_result",
        "has_vl",
        "vl_date",
        "vl_result",
        "took_suppliments",
        "suppliment",
        "comment")
    radio_fields = {
        "has_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL,
        "took_suppliments": admin.VERTICAL}
    filter_horizontal = ("suppliment", )
admin.site.register(MaternalLabDelClinic, MaternalLabDelClinicAdmin)
