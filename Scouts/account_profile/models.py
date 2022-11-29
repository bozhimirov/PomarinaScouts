from django.core import validators
from django.db import models

from Scouts.accounts.models import AppUser
from Scouts.core.model_mixins import Gender
from Scouts.core.validators import validate_only_letters, validate_only_numbers, validate_file_less_than_5mb


class Profile(models.Model):
    MIN_LEN_FIRST_NAME = 2
    MAX_LEN_FIRST_NAME = 30
    MIN_LEN_LAST_NAME = 2
    MAX_LEN_LAST_NAME = 30
    MIN_LEN_PHONE = 10
    MAX_LEN_PHONE = 10

    first_name = models.CharField(
        max_length=MAX_LEN_FIRST_NAME,
        help_text="Please use only letters.",
        validators=(
            validators.MinLengthValidator(MIN_LEN_FIRST_NAME),
            validate_only_letters,
        ),
    )

    last_name = models.CharField(
        max_length=MAX_LEN_LAST_NAME,
        help_text="Please use only letters.",
        validators=(
            validators.MinLengthValidator(MIN_LEN_LAST_NAME),
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
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    phone_number = models.CharField(
        max_length=MAX_LEN_PHONE,
        validators=(
            validators.MinLengthValidator(MIN_LEN_PHONE),
            validate_only_numbers,
        ),
        null=False,
        blank=False,
    )

    profile_image = models.ImageField(
        upload_to='users_photos',
        null=True,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    # USERNAME_FIELD = 'email'

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()
