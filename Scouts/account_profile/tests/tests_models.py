from django.core.exceptions import ValidationError
from django.test import TestCase

from Scouts.account_profile.models import Profile
from Scouts.accounts.models import AppUser


class ProfileModelTests(TestCase):

    def test_profile_save__when_tel_is_valid__expected_correct_result(self):
        user = AppUser(
            email='user@user.user',
            password='password',
        )
        user.full_clean()
        user.save()
        profile = Profile(
            first_name='Test',
            last_name='Name',
            user=user,
            phone_number='0987654321',
        )

        profile.full_clean()
        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_save__when_tel_has_9_digits__expected_exception(self):
        user = AppUser(
            email='user@user.user',
            password='password',
        )
        user.full_clean()
        user.save()

        profile = Profile(
            first_name='Test',
            last_name='Name',
            user=user,
            phone_number='098765432',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

    def test_profile_save__when_tel_has_a_letter__expected_exception(self):
        user = AppUser(
            email='user@user.user',
            password='password',
        )
        user.full_clean()
        user.save()

        profile = Profile(
            first_name='Test',
            last_name='Name',
            user=user,
            phone_number='098765432a',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

