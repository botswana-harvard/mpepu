from lab_requisition.classes import requisitions
from models import InfantRequisition, MaternalRequisition


requisitions.register('infant', InfantRequisition)
requisitions.register('maternal', MaternalRequisition)
