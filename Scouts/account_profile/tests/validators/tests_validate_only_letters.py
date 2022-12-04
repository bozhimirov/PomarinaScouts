from unittest import TestCase

from django.core.exceptions import ValidationError

from Scouts.core.validators import validate_only_letters


class LettersValidator(TestCase):

    def test_letters__when_valid_expect_ok(self):
        validate_only_letters('skjfFDSADfadl')

    def test_letters__with_digits_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_letters('sdSD0ds')

        self.assertIsNotNone(context.exception)

    def test_letters__with_spec_char_expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            validate_only_letters('sdSD!sd')

        self.assertIsNotNone(context.exception)













