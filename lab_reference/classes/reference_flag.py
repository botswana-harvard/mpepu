from django.conf import settings
from lab_flag.classes import Flag


class ReferenceFlag(Flag):

    def check_list_prep(self, list_items):
        """Runs additional checks for the reference table.

        Should be a single range only."""
        ranges = []
        for list_item in list_items:
            ranges.append(str(list_item.value_low) + '-' + str(list_item.value_high))
            ranges = list(ranges)
        if len(ranges) != 1:
            raise TypeError('Multiple reference ranges items for test code {0} gender {1}. Expected 1. Is there overlap in the age categories? Got "{2}".'.format(self.test_code, self.gender, ranges))

    def get_list_prep(self, value, test_code, gender, hiv_status, age_in_days):
        """Returns list of normal range list items filtered on test_code, gender, age_in_days.

        .. note:: Normal ranges do not consider HIV status."""

        if not self.list_item_model_cls:
            list_items = []
        else:
            list_items = self.list_item_model_cls.objects.filter(
                **{'{0}__name__iexact'.format(self.list_name): settings.REFERENCE_RANGE_LIST,
                   'reference_range_list__name__iexact': settings.REFERENCE_RANGE_LIST,
                   'test_code': test_code,
                   'gender__icontains': gender,
                   'active': True})
        # return a filtered list of list_item instances
        return self.filter_list_items_by_age(list_items, age_in_days)

    def get_evaluate_prep(self, value, list_item):
        """ Determines if the value falls outside of the reference range after all values are rounded up."""
        flag = None
        val, value_low, value_high = self.round_off(value, list_item)
        return self.get_flg(val, value_low, value_high, flag)

    def get_flg(self, val, value_low, value_high, flg):
        if not flg:
            flg = ''
        if val < value_low:
            flg += 'LO'
        if val > value_high:
            flg += 'HI'
        if len(flg) > 2:
            raise ValueError('Reference ranges overlap (HI/LO) for test code {0} age {1} gender {2}.'.format(self.test_code.code, self.age_in_days, self.gender))
        if flg == '':
            flg = None
        # flag should be None, LO or HI -- but not ''
        return flg, value_low, value_high
