from django.contrib import admin
from bhp_export_data.actions import export_as_csv_action
from bhp_base_admin.admin import BaseModelAdmin
from forms import ResultForm, ResultItemForm
from models import Receive, Aliquot, Result, ResultItem, Review, Order, Panel, TestCode
from models import AliquotType, TestCodeGroup, AliquotCondition
from actions import recalculate_grading, flag_as_reviewed, unflag_as_reviewed, refresh_order_status


class ReceiveAdmin(BaseModelAdmin):
    date_hierarchy = 'receive_datetime'
    list_display = ('registered_subject', 'to_order', "receive_identifier", "receive_datetime", "requisition_identifier", "drawn_datetime", 'created', 'modified', 'import_datetime')
    search_fields = ('registered_subject__subject_identifier', "receive_identifier", "requisition_identifier",)
    list_filter = ('created', "receive_datetime", "drawn_datetime", 'modified', 'import_datetime', )
    list_per_page = 15

    def get_readonly_fields(self, request, obj):
        return [field.name for field in obj._meta.fields if field.editable and field.name not in ['requisition_identifier']]

admin.site.register(Receive, ReceiveAdmin)


class AliquotAdmin(BaseModelAdmin):
    list_display = ("aliquot_identifier", 'to_receive', 'subject_identifier', 'drawn', "aliquot_type", 'aliquot_condition', 'created', 'modified', 'import_datetime')
    search_fields = ('aliquot_identifier', 'receive__receive_identifier', 'receive__registered_subject__subject_identifier')
    list_filter = ('created', 'import_datetime', 'aliquot_type', 'aliquot_condition')
    list_per_page = 15

    def get_readonly_fields(self, request, obj):
        return [field.name for field in obj._meta.fields if field.editable]

admin.site.register(Aliquot, AliquotAdmin)


class OrderAdmin(BaseModelAdmin):
    date_hierarchy = 'order_datetime'
    list_display = ("order_identifier", "receive_identifier", "req", "to_receive", "to_result", "subject_identifier", "panel", "order_datetime", 'status', 'created', 'modified', 'import_datetime')
    search_fields = ('aliquot__receive__registered_subject__subject_identifier', "order_identifier", "aliquot__receive__receive_identifier")
    list_filter = ('status', 'import_datetime', 'aliquot__aliquot_condition', 'panel__edc_name')
    list_per_page = 15
    actions = [refresh_order_status, ]

    def get_readonly_fields(self, request, obj):
        return ['aliquot', 'status', 'order_datetime', 'comment']
admin.site.register(Order, OrderAdmin)


class AliquotTypeAdmin(BaseModelAdmin):
    list_display = ('name', 'alpha_code', 'numeric_code')
admin.site.register(AliquotType, AliquotTypeAdmin)


class AliquotConditionAdmin(BaseModelAdmin):
    list_display = ('display_index', 'name', 'short_name')
admin.site.register(AliquotCondition, AliquotConditionAdmin)


class PanelAdmin(BaseModelAdmin):
    list_display = ('name', 'edc_name', 'panel_type')
    filter_horizontal = ("test_code", "aliquot_type", )
    list_filter = ('panel_type', )
admin.site.register(Panel, PanelAdmin)


class TestCodeAdmin(BaseModelAdmin):
    list_display = ('code', 'name', 'edc_code', 'edc_name')
    list_filter = ('test_code_group', )
    search_fields = ('code', 'name', 'edc_code', 'edc_name', 'test_code_group__code', 'test_code_group__name')
admin.site.register(TestCode, TestCodeAdmin)


class TestCodeGroupAdmin(BaseModelAdmin):
    list_display = ('code', 'name')
admin.site.register(TestCodeGroup, TestCodeGroupAdmin)


class ReviewAdmin(BaseModelAdmin):
    list_display = ('title', 'review_status', 'created', 'modified', 'user_created', 'user_modified')
    fields = ('title', 'review_status', 'comment')
    search_fields = ('title', 'comment')
    list_filter = ('review_status', 'created', 'modified', 'user_created', 'user_modified')
    readonly_fields = ('title', 'review_status')
admin.site.register(Review, ReviewAdmin)


class ResultAdmin(BaseModelAdmin):
    date_hierarchy = 'result_datetime'
    actions = [flag_as_reviewed, unflag_as_reviewed]
    form = ResultForm
    search_fields = ("result_identifier", "subject_identifier",
                     "receive_identifier",
                     "order__order_identifier",
                     'order__panel__name')
    list_display = (
        "result_identifier",
        'report',
        'reviewed',
        "subject_identifier",
        'panel',
        "result_datetime",
        'to_order',
        'to_items',
        "release_status",
        "release_datetime",
        'import_datetime')
    radio_fields = {"release_status": admin.VERTICAL}
    list_filter = ("release_status", 'reviewed', "result_datetime", 'import_datetime')
    list_per_page = 15

    def get_readonly_fields(self, request, obj):
        return [field.name for field in obj._meta.fields if field.editable]

admin.site.register(Result, ResultAdmin)


class ResultItemAdmin(BaseModelAdmin):

    def __init__(self, *args, **kwargs):
        super(ResultItemAdmin, self).__init__(*args, **kwargs)
    date_hierarchy = 'result_item_datetime'
    form = ResultItemForm
    list_display = (
        "test_code",
        "result",
        "subject_identifier",
        'subject_type',
        "result_item_value",
        "result_item_value_as_float",
        "result_item_datetime",
        "to_result",
        "grade_range",
        "grade_flag",
        "reference_range",
        "reference_flag",
        'validation_status',
        "created",
        "modified",
        'import_datetime')
    list_filter = ('grade_flag', 'reference_flag', "validation_status", 'subject_type', "result_item_datetime", "created", "modified", 'import_datetime', "test_code")
    search_fields = ('id', 'test_code__code',
                     'result__result_identifier',
                     "subject_identifier",
                     "receive_identifier",
                     "result_item_value")
    radio_fields = {
        "result_item_quantifier": admin.VERTICAL,
        "validation_status": admin.VERTICAL}
    actions = [
        export_as_csv_action("CSV Export: (adds subject_identifier, gender, dob",
            fields=[],
            exclude=['id', ],
            extra_fields=[
                {'gender': 'result__order__aliquot__receive__registered_subject__gender'},
                {'dob': 'result__order__aliquot__receive__registered_subject__dob'},
                ]),
       recalculate_grading, ]
    list_per_page = 35

    def get_readonly_fields(self, request, obj):
        return [field.name for field in obj._meta.fields if field.editable]

admin.site.register(ResultItem, ResultItemAdmin)
