"""
Sets up the Django app configuration for the DjangoMeasurement app.
"""

# django
from django.apps import AppConfig


class DjangoMeasurementApp(AppConfig):
    """
    Django app configuration for the DjangoMeasurement app.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "django_measurement"

    def ready(self) -> None:
        from .fields import MeasurementField
        from .lookups import LessThan, LessThanOrEqual, GreaterThan, GreaterThanOrEqual, Equal, Range

        for k, v in MeasurementField.get_lookups().items():
            try:
                MeasurementField._unregister_lookup(lookup_name=k, lookup=v)
            except KeyError:
                pass

        MeasurementField.register_lookup(LessThan)
        MeasurementField.register_lookup(LessThanOrEqual)
        MeasurementField.register_lookup(GreaterThan)
        MeasurementField.register_lookup(GreaterThanOrEqual)
        MeasurementField.register_lookup(Equal)
        MeasurementField.register_lookup(Range)
