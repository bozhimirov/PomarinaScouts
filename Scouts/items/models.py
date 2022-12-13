from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from Scouts.core.model_mixins import StrFromFieldsMixin, ItemCategory, AgeGroup, Size, Gender
from Scouts.core.validators import validate_file_less_than_5mb, validate_only_letters, validate_gt_zero, \
    validate_only_numbers

UserModel = get_user_model()


class Item(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'category')
    MIN_DESCRIPTION_LENGTH = 5
    MIN_LOCATION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30
    MAX_NAME = 30
    MIN_NAME = 3

    photo = CloudinaryField(
        null=False,
        blank=False,
        # validators=(
        #     validate_file_less_than_5mb,
        # ),
        help_text='Upload photo of your Item here!'

    )

    category = models.CharField(
        null=False,
        blank=False,
        choices=ItemCategory.choices(),
        max_length=ItemCategory.max_len(),
        help_text='Required / Please choose category of the item'

    )

    name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_NAME,
        help_text='Optional / Name of the item '

    )

    # consider Float-field if necessary for price
    price = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text='Required / Price of the item ',
        validators=(
            validate_gt_zero,
        ),

    )

    ages = models.CharField(
        null=True,
        blank=True,
        choices=AgeGroup.choices(),
        max_length=AgeGroup.max_len(),
        help_text='Optional / Please choose Age category '

    )

    size = models.CharField(
        null=True,
        blank=True,
        choices=Size.choices(),
        max_length=Size.max_len(),
        help_text='Optional / Please choose Size category '

    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        help_text='Optional / Please choose Gender category '

    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
        help_text='Optional / Description of the Item '

    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
        help_text='Optional / Location of the Item '

    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        # Create/Update

        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk}-{self.category}-{self.name}')

        if not self.name:
            self.name = self.slug

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['slug']


class UsedItem(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'category')
    MIN_DESCRIPTION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30
    MAX_NAME = 30

    photo = CloudinaryField(
        null=False,
        blank=False,
        # validators=(
        #     validate_file_less_than_5mb,
        # ),
        help_text='Required / Upload photo of your Item here!',

    )

    category = models.CharField(
        null=False,
        blank=False,
        choices=ItemCategory.choices(),
        max_length=ItemCategory.max_len(),
        help_text='Required / Please choose category of the item'

    )

    ages = models.CharField(
        null=True,
        blank=True,
        choices=AgeGroup.choices(),
        max_length=AgeGroup.max_len(),
        help_text='Optional / Please choose Age category '

    )

    size = models.CharField(
        null=True,
        blank=True,
        choices=Size.choices(),
        max_length=Size.max_len(),
        help_text='Optional / Please choose Size category '

    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        help_text='Optional / Please choose Gender category '
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
        help_text='Required / Description of the Item '
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
        help_text='Optional / Location of the Item '
    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk}-{self.category}')

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['slug']
