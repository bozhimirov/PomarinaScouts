# from enum import Enum


class StrFromFieldsMixin:
    str_fields = ()

    def __str__(self):
        fields = [(str_field, getattr(self, str_field, None)) for str_field in self.str_fields]
        return ', '.join(f'{name}={value}' for (name, value) in fields)


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())

#
#
# class TaxType(ChoicesEnumMixin, Enum):
#     MONTHLY_TAX = '30'
#     ANNUAL_TAX = '35'

#
# class Months(ChoicesEnumMixin, Enum):
#     January = 'January'
#     February = 'February'
#     Merch = 'Merch'
#     April = 'April'
#     May = 'May'
#     June = 'June'
#     July = 'July'
#     August = 'August'
#     September = 'September'
#     October = 'October'
#     November = 'November'
#     December = 'December'
