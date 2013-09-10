import logging
from django.db.models import get_model
from bhp_lock.classes import BaseLock

logger = logging.getLogger(__name__)


class NullHandler(logging.Handler):
    def emit(self, record):
        pass
nullhandler = logger.addHandler(NullHandler())


class SyncLock(BaseLock):

    def __init__(self, db):
        self.db = db
        SyncLockModel = get_model('bhp_sync', 'SyncLockModel')
        SyncImportHistoryModel = get_model('bhp_sync', 'SyncImportHistoryModel')
        super(SyncLock, self).__init__(db, SyncLockModel, SyncImportHistoryModel)
