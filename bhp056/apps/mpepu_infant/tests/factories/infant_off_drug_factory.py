import factory
from datetime import date, datetime

from edc.subject.registration.tests.factories import RegisteredSubjectFactory

from apps.mpepu_infant.models import InfantOffDrug


class InfantOffDrugFactory(RegisteredSubjectFactory):
    FACTORY_FOR = InfantOffDrug

    report_datetime = datetime.today()
    last_dose_date = date.today()
    reason_off = 'off-study'
    