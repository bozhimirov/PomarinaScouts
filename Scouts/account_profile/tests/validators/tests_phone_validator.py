from unittest import TestCase

from django.core.exceptions import ValidationError

from Scouts.core.validators import validate_mobile_number


class PhoneValidator(TestCase):

    def test_phone__when_valid_expect_ok(self):
        validate_mobile_number('0987654321')

    def test_phone__when_9digits_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_mobile_number('098765432')

        self.assertIsNotNone(context.exception)

    def test_phone__when_11digits_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_mobile_number('09876543211')

        self.assertIsNotNone(context.exception)













