from unittest import TestCase

from django.core.exceptions import ValidationError

from Scouts.core.validators import validate_only_numbers


class NumbersValidator(TestCase):

    def test_nums__when_valid_expect_ok(self):
        validate_only_numbers('0987654321')

    def test_nums__when_has_letter_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_numbers('09876s5432')

        self.assertIsNotNone(context.exception)

    def test_nums__when_has_spec_char_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_numbers('098765!43211')

        self.assertIsNotNone(context.exception)













