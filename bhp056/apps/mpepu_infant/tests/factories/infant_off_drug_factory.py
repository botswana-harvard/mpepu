import factory
from datetime import date, datetime

from edc.subject.registration.models import RegisteredSubject
from edc.subject.registration.tests.factories import RegisteredSubjectFactory

from apps.mpepu_infant.models import InfantOffDrug, InfantVisit


class InfantOffDrugFactory(RegisteredSubjectFactory):
    FACTORY_FOR = InfantOffDrug

    infant_visit = factory.SubFactory(InfantVisit)
    registered_subject = factory.SubFactory(RegisteredSubject)
    report_datetime = datetime.today()
    last_dose_date = date.today()
    reason_off = 'off-study'
