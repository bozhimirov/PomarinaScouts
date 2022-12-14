from cloudinary.models import CloudinaryField
from django.core import validators
from django.db import models
from Scouts.accounts.models import AppUser
from Scouts.core.validators import validate_only_letters, validate_only_numbers, validate_mobile_number


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MAX_LEN_PHONE = 10
    MAX_NAME_LENGTH = 100
    CHOICES = [
        (None, 'Optional / Please choose gender'),
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        validators=(
            validators.MinLengthValidator(
                MIN_LEN_FIRST_NAME
            ),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        validators=(
            validators.MinLengthValidator(
                MIN_LEN_LAST_NAME
            ),
            validate_only_letters,
        ),
    )

    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES,
        max_length=MAX_NAME_LENGTH
    )

    phone_number = models.CharField(
        max_length=MAX_LEN_PHONE,
        validators=(
            validate_mobile_number,
            validate_only_numbers,
        ),
        error_messages={
            'required': 'Place phone number in format: 0987654321'
        },
        null=False,
        blank=False,
    )

    profile_image = CloudinaryField(
        null=True,
        blank=True,
        help_text="Optional / Upload your photo here",
        # validators=(
        #     validate_file_less_than_5mb,
        # ),
    )

    USERNAME_FIELD = 'user'

    # USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()


