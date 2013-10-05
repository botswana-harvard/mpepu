from django.core.management.base import BaseCommand, CommandError

from apps.mpepu_list.models import MaternalFeedingInfluence, MaternalBfFfRisksBenefits, MaternalUndecidedFeeding
from apps.mpepu_maternal.choices import FEEDING_INFLUENCE, FEEDING_TRAINING, FEEDING_INDECISION


class Command(BaseCommand):

    args = ()
    help = 'Populate lists'

    def handle(self, *args, **options):
        print 'Populating lists ...'
        model_list = [(MaternalFeedingInfluence, FEEDING_INFLUENCE), (MaternalBfFfRisksBenefits, FEEDING_TRAINING), (MaternalUndecidedFeeding, FEEDING_INDECISION)]
        for tpl in model_list:
            model, choices = tpl
            for t in choices:
                short_name, name = t
                if not model.objects.filter(name=name):
                    model.objects.create(short_name=short_name, name=name)
