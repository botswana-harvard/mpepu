from datetime import datetime, timedelta
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from bhp_sync.models import OutgoingTransaction, IncomingTransaction
from bhp_sync.classes import TransactionProducer


class Command(BaseCommand):

    args = ('num_days')
    help = 'Purge transactions already consumed. '
    option_list = BaseCommand.option_list + (
        make_option('--incoming',
            action='store_true',
            dest='incoming',
            default=False,
            help=('Purge incoming transactions.')),
         )
    option_list += (
        make_option('--outgoing',
            action='store_true',
            dest='outgoing',
            default=False,
            help=('Purge outgoing transactions.')),
        )

    def handle(self, *args, **options):
        if not args:
            args = [None]
        if options['incoming']:
            self.purge_incoming(*args)
        elif options['outgoing']:
            self.purge_outgoing(*args)
        else:
            raise CommandError('Unknown option, Try --help for a list of valid options')

    def purge_incoming(self, *args):
        n = 0
        tot = 0
        transactions = None

        #in days
        age = 0

        if args[0]:
            if args[0].isdigit():
                value = float(args[0])
                if value > 0:
                    age = int(value)
        print "Deleting incoming transaction older than {0} day(s)".format(age)
        cut_off_date = datetime.now() - timedelta(days=age)
#        transactions = IncomingTransaction.objects.filter(
#                            is_consumed=True,consumed_datetime__isnull=False,
#                            consumed_datetime__lte=cut_off_date
#                        )
        transactions = IncomingTransaction.objects.filter(
                            tx_name="ScheduledEntryBucket",
                        )
        tot = transactions.count()
        if tot == 0:
            print "    No transactions older than {0} were found".format(cut_off_date)
        else:
            for incoming_transaction in transactions:
                n += 1
                print '{0} / {1} {2} {3}'.format(
                    n,
                    tot,
                    incoming_transaction.producer,
                    incoming_transaction.tx_name)

                incoming_transaction.save(using='archive')
                print '    Saved on the archive db'

                incoming_transaction.delete(using='default')
                print '    Deleted from local db'
    '''
        Delete all outgoing transaction older than the specified number of days
        (default=0). If we are on a netbook delete only those that have been
        consumed.
    '''
    def purge_outgoing(self, *args):
        n = 0
        tot = 0
        transactions = None
        producer = TransactionProducer()
        is_server = True
        #in days
        age = 0

        if args:
            if args[0].isdigit():
                value = float(args[0])
                if value > 0:
                    age = int(value)
        print "Deleting outgoing transaction older than {0} day(s)".format(age)
        cutoff_date = datetime.now() - timedelta(days=age)
        #cutoff_timestamp = (datetime.now() - timedelta(days=age)).strftime('%Y%m%d%H%M%S%f')


        if 'DEVICE_ID' in dir(settings):
            if settings.DEVICE_ID.isdigit():
                if float(settings.DEVICE_ID) >= 98:
                    #We are on a server
                    transactions = OutgoingTransaction.objects.filter(
                                        created__lte=cutoff_date
                                    )
                    #tot = transactions.count()
                    #print '    {0} found on a server {1}'.format(tot,producer)
                else:
                    raise ValueError('The command should on be ran on server! .')
                    #We are on a netbook so delete consumed tx
#                    transactions = OutgoingTransaction.objects.exclude(
#                                        producer=producer,
#                                        created__gte=cutoff_date
                    #                )
                    #tot = transactions.count()
                    #is_server = False
                    
                    #print '    {0} found on a netbook {1}'.format(tot,producer)
                #if tot == 0:
                #    print "    No transactions older than {0} were found".format(cutoff_date)
                #else:
                for outgoing_transaction in transactions:
                    n += 1
                    print '{0} / {1} {2}'.format(n,outgoing_transaction.producer,outgoing_transaction.tx_name)
                    if is_server == True:
                        outgoing_transaction.save(using='archive')
                        print '    Saved on the archive db'

                    outgoing_transaction.delete(using='default')
                    print '    Deleted'
            else:
                raise ValueError('DEVICE_ID global value should be a number .')
        else:
            raise ValueError('DEVICE_ID global value should be set on the settings.py file.')

