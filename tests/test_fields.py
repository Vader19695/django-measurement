# django
from django.test import TestCase
from django_measurement.measurements import Area, Distance, Temperature

from .models import MeasurementTestModel


class TestMeasurementField(TestCase):
    def test__model_works_as_expected(self):
        # assign
        model = MeasurementTestModel.objects.create(value=Distance(mi=1))

        # assert
        self.assertTrue(isinstance(model.value, Distance))

    def test__query_by_distance_works_as_expected(self):
        # assign
        MeasurementTestModel.objects.create(value=Distance(mi=1))
        MeasurementTestModel.objects.create(value=Distance(mi=1.5))
        MeasurementTestModel.objects.create(value=Distance(mi=3))

        # act
        results = MeasurementTestModel.objects.filter(value__gte=Distance(mi=1.5))

        # assert
        self.assertEqual(results.count(), 2)

    def test___filter_by_area_works_as_expected(self):
        # assign
        expected_model = MeasurementTestModel.objects.create(value=Area(sq_mi=1))
        MeasurementTestModel.objects.create(value=Distance(mi=2))

        # act
        found_model = MeasurementTestModel.objects.filter(value__gte=Area(sq_mi=1))

        # assert
        self.assertEqual(expected_model.pk, found_model[0].pk)

    def test__filter_by_tempature_works_as_expected(self):
        # assign
        MeasurementTestModel.objects.create(value=Temperature(f=32))
        MeasurementTestModel.objects.create(value=Temperature(c=0))

        # act
        found_model = MeasurementTestModel.objects.filter(value=Temperature(f=32))

        # assert
        self.assertEqual(found_model.count(), 2)

    def test__filter_by_range_works_as_expected(self):
        # assign

        MeasurementTestModel.objects.create(value=Temperature(f=0))
        MeasurementTestModel.objects.create(value=Temperature(f=32))
        MeasurementTestModel.objects.create(value=Temperature(c=100))

        # act
        found_model = MeasurementTestModel.objects.filter(
            value__range=(
                Temperature(f=32),
                Temperature(f=212),
            )
        )

        # assert
        self.assertEqual(found_model.count(), 2)
        with self.assertRaises(ValueError):
            MeasurementTestModel.objects.filter(value__range=(Temperature(f=32), Distance(mi=1)))
