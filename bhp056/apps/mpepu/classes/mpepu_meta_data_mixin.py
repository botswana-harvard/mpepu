from edc.entry_meta_data.models import ScheduledEntryMetaData, RequisitionMetaData
from edc.subject.entry.models import Entry, LabEntry


class MpepuMetaDataMixin(object):

    def query_entry(self, model_name, visit_definition):
        return Entry.objects.get(model_name=model_name, visit_definition=visit_definition)

    def query_scheduled_meta_data(self, appointment, entry, registered_subject):
        scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=appointment, entry=entry, registered_subject=registered_subject)
        if scheduled_meta_data.count() == 1:
            return scheduled_meta_data[0]
        return scheduled_meta_data

    def create_scheduled_meta_data(self, appointment, entry, registered_subject):
        scheduled_meta_data = self.query_scheduled_meta_data(appointment, entry, registered_subject)
        if not scheduled_meta_data:
            scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=appointment, entry=entry, registered_subject=registered_subject)
        scheduled_meta_data.entry_status = 'NEW'
        scheduled_meta_data.save()
        return scheduled_meta_data

    def query_lab_entry(self, model_name, panel, visit_definition):
        return LabEntry.objects.get(model_name=model_name, requisition_panel=panel, visit_definition=visit_definition)

    def query_requisition_meta_data(self, appointment, lab_entry, registered_subject):
        requisition_meta_data = RequisitionMetaData.objects.filter(appointment=appointment, lab_entry=lab_entry, registered_subject=registered_subject)
        if requisition_meta_data.count() == 1:
            return requisition_meta_data[0]
        return requisition_meta_data

    def create_requisition_meta_data(self, appointment, lab_entry, registered_subject):
        requisition_meta_data = self.query_requisition_meta_data(appointment, lab_entry, registered_subject)
        if not requisition_meta_data:
            requisition_meta_data = RequisitionMetaData.objects.create(appointment=appointment, lab_entry=lab_entry, registered_subject=registered_subject)
        requisition_meta_data.entry_status = 'NEW'
        requisition_meta_data.save()
        return requisition_meta_data
