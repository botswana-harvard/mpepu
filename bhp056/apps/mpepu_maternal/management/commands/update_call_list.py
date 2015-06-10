from django.core.management.base import BaseCommand, CommandError
from django.db.models import get_model

from apps.mpepu_maternal.utils.update_call_list import update_call_list


class Command(BaseCommand):

    args = 'label'
    help = 'Add to the call list info from all subject consents from the specified survey.'

    def handle(self, *args, **options):
        CallList = get_model('mpepu_maternal', 'CallList')
        count = CallList.objects.all().count()
        try:
            label = args[0]
        except IndexError:
            raise CommandError('Specify a label')
        update_call_list(label, verbose=True)
        new_count = CallList.objects.all().count()
        print 'Added {} records to the Call List for {}.'.format(new_count - count, label)
