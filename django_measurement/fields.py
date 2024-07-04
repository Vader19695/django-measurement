# django
from django.db.models import JSONField

# thirdparty
from measurement.base import MeasureBase


class MeasurementField(JSONField):
    """
    This field is used to store measurements in the database.

    We will store the measurement in three parts:
    """

    @staticmethod
    def get_cls_from_name(name: str) -> MeasureBase:
        """
        This function will return the class from the name.

        :param name: The name of the class.
        :return: The class.
        """
        return getattr(__import__("measurement.measures", fromlist=[name]), name)

    def from_db_value(self, value: dict, expression, connection) -> MeasureBase:
        """
        Converts the value from the database to a Measurement instance.
        """
        if value is None:
            return value

        value = super().from_db_value(value, expression, connection)

        return MeasurementField.get_cls_from_name(value["class"])(**{value["unit"]: value["value"]})

    def get_prep_value(self, value: MeasureBase) -> dict:
        """
        This function will convert the value to a dictionary for storage in the database.

        :param value: The value to convert.
        :return: The dictionary.
        """

        if issubclass(value.__class__, MeasureBase):
            return {
                "standard": float(value.standard),
                "value": float(value.value),
                "unit": value.unit,
                "class": value.__class__.__name__,
            }
        return value

    def to_python(self, value: dict) -> MeasureBase:
        """
        Converts the value from the database to a Measurement instance.
        """
        if value is None:
            return value
        return MeasurementField.get_cls_from_name(value["class"])(**{value["unit"]: value["value"]})
