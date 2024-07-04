# django
from django.db import models
from django_measurement.fields import MeasurementField


class MeasurementTestModel(models.Model):
    value = MeasurementField()
