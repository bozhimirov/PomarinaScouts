from enum import Enum

from django.contrib.auth import models as auth_models
from django.core import validators
from django.db import models
from django.utils import timezone

from Scouts.accounts.managers import AppUserManager
from Scouts.core.model_mixins import Gender
from Scouts.core.validators import validate_only_letters, validate_only_numbers, validate_file_less_than_5mb


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        error_messages={
            "unique": "A user with that email already exists.",
        },
    )
    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    date_joined = models.DateTimeField(
        "date joined",
        default=timezone.now
    )

    objects = AppUserManager()

    USERNAME_FIELD = 'email'
