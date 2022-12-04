from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'email': 'test@test.test',
        'password1': 'password',
        'password2': 'password',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'phone_number': 'phone_number',
    }

    def test_signup__when_valid__expected_loggedin(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )

        self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'].username)


