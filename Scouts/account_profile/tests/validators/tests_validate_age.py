from unittest import TestCase

from django.core.exceptions import ValidationError

from Scouts.core.validators import validate_age


class AgeValidator(TestCase):

    def test_age__when_valid_expect_ok(self):
        validate_age(5)

    def test_age__when_less_expect_error(self):
        with self.assertRaises(ValidationError) as context:
            validate_age(1)

        self.assertIsNotNone(context.exception)

    def test_age__when_more_expect_error(self):
        with self.assertRaises(ValidationError) as context:
            validate_age(27)

        self.assertIsNotNone(context.exception)
