from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core import validators
from django.db import models
from django.utils.text import slugify

from Scouts.account_profile.models import Profile
from Scouts.accounts.models import AppUser
from Scouts.core.model_mixins import StrFromFieldsMixin, GenderKids
from Scouts.core.utils import calculate_age
from Scouts.core.validators import validate_only_numbers, validate_file_less_than_5mb, validate_only_letters, \
    validate_birth_credentials, validate_age, validate_mobile_number

UserModel = get_user_model()


class Kid(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'first_name', 'last_name')
    MAX_NAME = 30
    MIN_NAME = 3
    MIN_LEN_PHONE = 10
    MAX_LEN_PHONE = 10

    id = models.AutoField(primary_key=True)

    first_name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_NAME),
        )
    )

    last_name = models.CharField(
        max_length=MAX_NAME,
        null=True,
        blank=True,
        help_text='Optional / Last Name',
        validators=(
            validators.MinLengthValidator(MIN_NAME),
        )
    )

    gender = models.CharField(
        null=False,
        blank=False,
        choices=GenderKids.choices(),
        max_length=GenderKids.max_len(),
        help_text='Required / Please choose gender',
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        null=False,
        blank=False,
        help_text='Please Use Format YYYY-MM-DD:',
        validators=(
            validate_birth_credentials,
        ),
    )

    profile_picture = CloudinaryField(
        null=True,
        blank=True,
        help_text='Optional / Upload Profile Picture',
        # validators=(
        #     validate_file_less_than_5mb,
        # ),
    )

    phone_number = models.CharField(
        null=True,
        blank=True,
        help_text="Optional / Kid's Personal Phone Number",
        max_length=MAX_LEN_PHONE,
        validators=(
            validate_mobile_number,
            validate_only_numbers,
        ),
    )

    users = models.ForeignKey(
        UserModel,
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
    )

    parent_phone = models.CharField(
        max_length=MAX_LEN_PHONE,
        null=True,
        blank=True,
    )

    parent_name = models.CharField(
        max_length=MAX_NAME*2,
        null=True,
        blank=True,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.date_of_birth}'

    def save(self, *args, **kwargs):
        # Create/Update

        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.first_name}-{self.last_name}')

        if not self.parent_phone:
            user = Profile.objects.filter(pk=self.users.pk).get()
            self.parent_phone = user.phone_number

        if not self.parent_name:
            user = Profile.objects.filter(pk=self.users.pk).get()
            self.parent_name = f'{user.first_name} {user.last_name}'

        if not self.age:
            age = calculate_age(born=self.date_of_birth)
            validate_age(age)
            self.age = age

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-age']
