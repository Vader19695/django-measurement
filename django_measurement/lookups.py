# django
from django.db.models import Lookup

# thirdparty
from measurement.base import MeasureBase


class LessThan(Lookup):
    lookup_name = "lt"

    def __init__(self, lhs, rhs):
        # Ensure both sides are Measurement instances and of the same class
        if not issubclass(rhs.__class__, MeasureBase):
            raise ValueError("Invalid measurement. Please provide a valid Measurement class.")
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        # Generate the SQL for comparing the standard values of the two measurements

        lhs_sql, _ = compiler.compile(self.lhs)
        _, rhs_params = self.process_rhs(compiler, connection)
        params = [rhs_params[0]["standard"], rhs_params[0]["class"]]

        return (
            f"CAST({lhs_sql} ->> 'standard' AS NUMERIC) < %s AND CAST({lhs_sql} ->> 'class' AS TEXT) = %s",
            params,
        )


class LessThanOrEqual(Lookup):
    lookup_name = "lte"

    def __init__(self, lhs, rhs):
        # Ensure both sides are Measurement instances and of the same class
        if not issubclass(rhs.__class__, MeasureBase):
            raise ValueError("Invalid measurement. Please provide a valid Measurement class.")
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        # Generate the SQL for comparing the standard values of the two measurements

        lhs_sql, _ = compiler.compile(self.lhs)
        _, rhs_params = self.process_rhs(compiler, connection)
        params = [rhs_params[0]["standard"], rhs_params[0]["class"]]

        return (
            f"CAST({lhs_sql} ->> 'standard' AS NUMERIC) <= %s AND CAST({lhs_sql} ->> 'class' AS TEXT) = %s",
            params,
        )


class GreaterThan(Lookup):
    lookup_name = "gt"

    def __init__(self, lhs, rhs):
        # Ensure both sides are Measurement instances and of the same class
        if not issubclass(rhs.__class__, MeasureBase):
            raise ValueError("Invalid measurement. Please provide a valid Measurement class.")
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        # Generate the SQL for comparing the standard values of the two measurements

        lhs_sql, _ = compiler.compile(self.lhs)
        _, rhs_params = self.process_rhs(compiler, connection)
        params = [rhs_params[0]["standard"], rhs_params[0]["class"]]

        return (
            f"CAST({lhs_sql} ->> 'standard' AS NUMERIC) > %s AND CAST({lhs_sql} ->> 'class' AS TEXT) = %s",
            params,
        )


class GreaterThanOrEqual(Lookup):
    lookup_name = "gte"

    def __init__(self, lhs, rhs):
        # Ensure both sides are Measurement instances and of the same class
        if not issubclass(rhs.__class__, MeasureBase):
            raise ValueError("Invalid measurement. Please provide a valid Measurement class.")
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        # Generate the SQL for comparing the standard values of the two measurements

        lhs_sql, _ = compiler.compile(self.lhs)
        _, rhs_params = self.process_rhs(compiler, connection)
        params = [rhs_params[0]["standard"], rhs_params[0]["class"]]

        return (
            f"CAST({lhs_sql} ->> 'standard' AS NUMERIC) >= %s AND CAST({lhs_sql} ->> 'class' AS TEXT) = %s",
            params,
        )


class Equal(Lookup):
    lookup_name = "exact"

    def __init__(self, lhs, rhs):
        # Ensure both sides are Measurement instances and of the same class
        if not issubclass(rhs.__class__, MeasureBase):
            raise ValueError("Invalid measurement. Please provide a valid Measurement class.")
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        # Generate the SQL for comparing the standard values of the two measurements

        lhs_sql, _ = compiler.compile(self.lhs)
        _, rhs_params = self.process_rhs(compiler, connection)
        params = [rhs_params[0]["standard"], rhs_params[0]["class"]]

        return (
            f"CAST({lhs_sql} ->> 'standard' AS NUMERIC) = %s AND CAST({lhs_sql} ->> 'class' AS TEXT) = %s",
            params,
        )


class Range(Lookup):
    lookup_name = "range"

    def __init__(self, lhs, rhs):
        # Ensure both sides are Measurement instances and of the same class
        if not issubclass(rhs[0].__class__, MeasureBase) and not issubclass(rhs[1].__class__, MeasureBase):
            raise ValueError("Invalid measurement. Please provide a valid Measurement class.")

        if rhs[0].__class__ != rhs[1].__class__:
            raise ValueError("Invalid range. Range must be of the same class")
        super().__init__(lhs, rhs)

    def as_sql(self, compiler, connection):
        # Generate the SQL for comparing the standard values of the two measurements

        lhs_sql, _ = compiler.compile(self.lhs)
        _, rhs_params = self.process_rhs(compiler, connection)
        params = [
            float(rhs_params[0][0].standard),
            float(rhs_params[0][1].standard),
            rhs_params[0][0].__class__.__name__,
        ]

        return (
            f"CAST({lhs_sql} ->> 'standard' AS NUMERIC) BETWEEN %s AND %s AND CAST({lhs_sql} ->> 'class' AS TEXT) = %s",
            params,
        )
