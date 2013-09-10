from django.test import TestCase
from bhp_base_model.models import TestManyToMany
from bhp_base_model.models import TestForeignKey
from bhp_base_model.models import TestModel


class ModelsTests(TestCase):

    def setUp(self):
        pass

    def test_model_save(self):
        test_m2m = TestManyToMany.objects.create(name='test_m2m', short_name='test_m2m')
        test_fk = TestForeignKey.objects.create(name='test_fk', short_name='test_fk')
        test_model = TestModel(name='TEST', test_foreign_key=test_fk)
        test_model.save()
        test_model.test_many_to_many.add(test_m2m)
        test_model = TestModel.objects.get(name='TEST')
        self.assertEqual(test_model.test_foreign_key, test_fk)
        self.assertIsNotNone(test_model.test_foreign_key)
        #self.assertEqual(test_model.test_many_to_many, test_m2m)
        self.assertIsNotNone(test_model.test_many_to_many)
