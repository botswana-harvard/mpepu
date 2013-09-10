from django.db import models
from django.db.models import DateTimeField, DateField, IntegerField, DecimalField, CharField
from django.db.models import Count, Sum, Avg, Max, Min, StdDev, Variance
from bhp_model_selector.classes import ModelSelector
from bhp_model_describer.models import Related, GroupingHint

"""
from bhp_describer.classes import DataDescriber
d = ModelDescriber('mochudi_subject', 'qn002sectionone')
d.summarize()
d.group()
d.group_m2m()
d.export_as_csv()
"""


class ModelDescriber(ModelSelector):

    def __init__(self, app_label, model_name):

        super(ModelDescriber, self).__init__(app_label, model_name)

        self.summary = {}
        self.grouping = {}
        self.grouping_m2m = {}

    def summarize(self):

        # basic summary
        summarize = {}
        if self.model:
            q = {}
            self.summary = {}
            for field in self.opts.fields:
                if isinstance(field, (DateTimeField, DateField)):
                    aggregates = self.model.objects.all().aggregate(Count(field.name), Max(field.name), Min(field.name))
                    new_aggregates = {}
                    for key, value in aggregates.items():
                        k = key.split('__')
                        new_aggregates[k[1]] = value
                    q = new_aggregates

                elif isinstance(field, (IntegerField, DecimalField)):
                    aggregates = self.model.objects.all().aggregate(Count(field.name), Sum(field.name), Avg(field.name), Max(field.name), Min(field.name), StdDev(field.name), Variance(field.name))
                    new_aggregates = {}
                    for key, value in aggregates.items():
                        k = key.split('__')
                        new_aggregates[k[1]] = value
                    q = new_aggregates
                else:
                    q = None

                if q:
                    self.summary[field.name] = q

                summarize = {'table': self.table, 'fields': self.summary}

        return summarize

    def group(self):

        grouping = {}
        if self.model:
            self.grouping = {}
            # basic grouping on char fields
            for field in self.opts.fields:
                if isinstance(field, CharField):
                    new_aggregates = []
                    # group on choices tuple or if listed in GroupingHint
                    grouping_hint = GroupingHint.objects.filter(app_label=self.app_label, model_name=self.model_name, field_name=field.name)
                    if grouping_hint:
                        aggregates = self.model.objects.values(field.name).annotate(count=Count(field.name)).order_by()
                        new_aggregates = []
                        for aggregate in aggregates:
                            new_aggregates.append({'count': aggregate['count'], 'label': aggregate[field.name]})
                        self.grouping[field.name] = new_aggregates
                    elif field.choices:
                        for choice in field.choices:
                            aggregates = self.model.objects.values(field.name).annotate(count=Count(field.name)).order_by()
                            new_aggregates = []
                            for aggregate in aggregates:
                                new_aggregates.append({'count': aggregate['count'], 'label': aggregate[field.name]})
                            self.grouping[field.name] = new_aggregates
                    else:
                        pass

                # group on foreignkey if related table has field 'name'
                elif isinstance(field, models.ForeignKey):
                    for fld in field.related.parent_model._meta.fields:

                        if Related.objects.filter(app_label=self.app_label, model_name=self.model_name, field_name=field.name, related_to_model=field.related.parent_model._meta.module_name):
                            related = Related.objects.get(app_label=self.app_label, model_name=self.model_name, field_name=field.name, related_to_model=field.related.parent_model._meta.module_name)
                            related_to_field_name = related.related_to_field_name
                        else:
                            related_to_field_name = 'name'

                        if fld.name == related_to_field_name:
                            fld_string = '%s__%s' % (field.name, fld.name)
                            aggregates = self.model.objects.values(fld_string).annotate(count=Count(fld_string)).order_by()
                            new_aggregates = []
                            # self.grouping[fld_string] = q
                            for aggregate in aggregates:
                                new_aggregates.append({'count': aggregate['count'], 'label': aggregate[fld_string]})
                            self.grouping[field.name] = new_aggregates

            grouping = {'table': self.table, 'fields': self.grouping}

        return grouping

    def group_m2m(self):

        for field in self.opts.local_many_to_many:
            for fld in field.related.parent_model._meta.fields:
                if Related.objects.filter(app_label=self.app_label, model_name=self.model_name, field_name=field.name, related_to_model=field.related.parent_model._meta.module_name):
                    related = Related.objects.get(app_label=self.app_label, model_name=self.model_name, field_name=field.name, related_to_model=field.related.parent_model._meta.module_name)
                    related_to_field_name = related.related_to_field_name
                else:
                    related_to_field_name = 'name'

                if fld.name == related_to_field_name:
                    fld_string = '%s__%s' % (field.name, fld.name)
                    aggregates = self.model.objects.values(fld_string).annotate(count=Count(fld_string)).order_by()
                    new_aggregates = []
                    for aggregate in aggregates:
                        new_aggregates.append({'count': aggregate['count'], 'label': aggregate[fld_string]})
                    self.grouping_m2m[field.name] = new_aggregates

        return {'table': self.table, 'fields': self.grouping_m2m}
