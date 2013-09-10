from django.contrib import admin
from bhp_base_admin.admin import BaseModelAdmin
from lab_test_code.models import TestCode, TestCodeGroup, TestCodeReferenceList, TestCodeReferenceListItem, TestCodeInterfaceMapping


class TestCodeAdmin(BaseModelAdmin):
    list_display = ('code', 'name', 'test_code_group', 'units', 'display_decimal_places')
    search_fields = ('code', 'name', 'test_code_group__code', 'units', 'display_decimal_places')

admin.site.register(TestCode, TestCodeAdmin)


class TestCodeReferenceListAdmin(BaseModelAdmin):
    pass
admin.site.register(TestCodeReferenceList, TestCodeReferenceListAdmin)


class TestCodeReferenceListItemAdmin(BaseModelAdmin):
    list_display = ('test_code', 'gender', 'value_low', 'value_high', 'age_low', 'age_low_unit', 'age_low_quantifier', 'age_high', 'age_high_unit', 'age_high_quantifier', 'panic_value_low', 'panic_value_high', 'test_code_reference_list')
    search_fields = ['test_code__code', 'test_code__test_code_group__code', 'gender', 'age_low', 'age_high', ]
admin.site.register(TestCodeReferenceListItem, TestCodeReferenceListItemAdmin)


class TestCodeInterfaceMappingAdmin(BaseModelAdmin):
    pass
admin.site.register(TestCodeInterfaceMapping, TestCodeInterfaceMappingAdmin)


class TestCodeGroupAdmin(BaseModelAdmin):
    list_display = ('code', 'name',)
    search_fields = ('code', 'name',)
admin.site.register(TestCodeGroup, TestCodeGroupAdmin)
