from unittest import TestCase
from datetime import date

from django.core.exceptions import ValidationError


def validate_birth_credentials(born):
    today = date.today()

    if 4 > (today.year - born.year()) or (today.year - born.year()) > 26:
        raise ValidationError(f'Invalid year declared')
    if 1 > born.month() or born.month() > 12:
        raise ValidationError(f'Invalid month declared')
    if 1 > born.day() or born.day() > 31:
        raise ValidationError(f'Invalid day declared')


class Born:
    def __init__(self, value):
        self.value = value

    def year(self):
        split_value = self.value.split('-')
        # strip_int_value = [int(x) for x in strip_value]
        # print(strip_int_value)
        # print(strip_int_value[0])
        return int(split_value[0])
        # return strip_int_value[0]

    def month(self):
        split_value = self.value.split('-')
        split_int_value = [int(x) for x in split_value]
        # return strip_value[1]
        return split_int_value[1]

    def day(self):
        split_value = self.value.split('-')
        split_int_value = [int(x) for x in split_value]
        # return strip_value[2]
        return split_int_value[2]


class BirthValidator(TestCase):

    def test_birth_credentials__when_all_valid_expect_ok(self):
        born = Born('2010-10-10')
        validate_birth_credentials(born)

    def test_birth_credentials__when_year_less__expect_error(self):
        born = Born('1900-10-10')
        with self.assertRaises(ValidationError) as context:
            validate_birth_credentials(born)

        self.assertIsNotNone(context.exception)

    def test_birth_credentials__when_year_more__expect_error(self):
        born = Born('2030-10-10')
        with self.assertRaises(ValidationError) as context:
            validate_birth_credentials(born)

        self.assertIsNotNone(context.exception)

    def test_birth_credentials__when_month_less__expect_error(self):
        born = Born('2010-0-10')
        with self.assertRaises(ValidationError) as context:
            validate_birth_credentials(born)

        self.assertIsNotNone(context.exception)

    def test_birth_credentials__when_month_more__expect_error(self):
        born = Born('2010-15-10')
        with self.assertRaises(ValidationError) as context:
            validate_birth_credentials(born)

        self.assertIsNotNone(context.exception)

    def test_birth_credentials__when_day_less__expect_error(self):
        born = Born('2010-10-0')
        with self.assertRaises(ValidationError) as context:
            validate_birth_credentials(born)

        self.assertIsNotNone(context.exception)

    def test_birth_credentials__when_day_more__expect_error(self):
        born = Born('2010-10-40')
        with self.assertRaises(ValidationError) as context:
            validate_birth_credentials(born)

        self.assertIsNotNone(context.exception)
