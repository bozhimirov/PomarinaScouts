from unittest import TestCase

from django.core.exceptions import ValidationError

from Scouts.core.validators import validate_gt_zero


class NumbersValidator(TestCase):

    def test_nums__when_valid_expect_ok(self):
        validate_gt_zero(1)

    def test_nums__when_zero_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_gt_zero(0)

        self.assertIsNotNone(context.exception)

    def test_nums__when_negative_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_gt_zero(-1)

        self.assertIsNotNone(context.exception)

    def test_nums__when_float_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_gt_zero(0.1)

        self.assertIsNotNone(context.exception)













