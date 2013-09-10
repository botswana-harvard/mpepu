from django.contrib import admin
from bhp_base_admin.admin import BaseModelAdmin
from models import GradingList, GradingListItem


class GradingListAdmin(BaseModelAdmin):
    pass
admin.site.register(GradingList, GradingListAdmin)


class GradingListItemAdmin(BaseModelAdmin):
    list_display = ('test_code', 'gender', 'hiv_status', 'grade', 'value_low', 'value_high', 'age_low', 'age_low_unit', 'age_low_quantifier',
                    'age_high', 'age_high_unit', 'age_high_quantifier', 'grading_list')
    search_fields = ['grade', 'test_code__code', 'test_code__name', 'value_low', 'value_high', 'hiv_status']
admin.site.register(GradingListItem, GradingListItemAdmin)
