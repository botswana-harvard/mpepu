from lab_reference.models import BaseReferenceList


class GradingList(BaseReferenceList):

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = "lab_grading"
        db_table = 'lab_grading_gradinglist'
        ordering = ['name']
