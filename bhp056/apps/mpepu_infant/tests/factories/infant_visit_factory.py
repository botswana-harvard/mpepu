import factory

from edc.subject.visit_tracking.tests.factories import BaseVisitTrackingFactory
from edc.subject.appointment.tests.factories import AppointmentFactory

from apps.mpepu_infant.models import InfantVisit


class InfantVisitFactory(BaseVisitTrackingFactory):
    FACTORY_FOR = InfantVisit
    
    appointment = factory.SubFactory(AppointmentFactory)
    information_provider = 'Mother'
    study_status = 'onstudy rando ondrug'
