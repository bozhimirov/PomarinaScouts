from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from Scouts.core.model_mixins import StrFromFieldsMixin
from Scouts.core.validators import validate_gt_zero

UserModel = get_user_model()


class Item(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'category')
    MIN_DESCRIPTION_LENGTH = 5
    MIN_LOCATION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30
    MAX_NAME = 30
    MIN_NAME = 3
    MAX_NAME_LENGTH = 100

    photo = CloudinaryField(
        null=False,
        blank=False,
        # validators=(
        #     validate_file_less_than_5mb,
        # ),
        help_text='Upload photo of your Item here!'

    )

    CHOICES_CATEGORY = [
        (None, 'Optional / Please choose category of the item'), ('Hoodies', 'Hoodies'), ('T-shirts', 'T-shirts'),
        ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Trousers', 'Trousers'),
        ('Soft Shell', 'Soft Shell'), ('Others', 'Others')
    ]
    category = models.CharField(
        null=False,
        blank=False,
        choices=CHOICES_CATEGORY,
        max_length=MAX_NAME_LENGTH,
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
    CHOICES_AGE = [
        (None, 'Optional / Please choose ages category'), ('Beavers', 'Beavers'), ('Cubs', 'Cubs'),
        ('Scouts', 'Scouts'), ('Ventures', 'Ventures'), ('Rovers', 'Rovers'), ('Adult Volunteer', 'Adult Volunteer'),
        ('Beavers & Cubs', 'Beavers & Cubs'), ('Scouts & Ventures', 'Scouts & Ventures'),
        ('Rovers & Volunteers', 'Rovers & Volunteers')
    ]
    ages = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES_AGE,
        max_length=MAX_NAME_LENGTH,
    )

    CHOICES_SIZE = [
        (None, 'Optional / Please choose size category'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'),
        ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')
    ]
    size = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES_SIZE,
        max_length=MAX_NAME_LENGTH,
    )
    CHOICES_GENDER = [(None, 'Optional / Please choose gender category'), ('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES_GENDER,
        max_length=MAX_NAME_LENGTH,
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
    CHOICES_CATEGORY = [
        (None, 'Required / Please choose category of the item'), ('Hoodies', 'Hoodies'), ('T-shirts', 'T-shirts'),
        ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Trousers', 'Trousers'),
        ('Soft Shell', 'Soft Shell'), ('Others', 'Others')
    ]
    category = models.CharField(
        null=False,
        blank=False,
        choices=CHOICES_CATEGORY,
        max_length=(max(len(value) for _, value in CHOICES_CATEGORY)),
    )

    CHOICES_AGE = [
        (None, 'Optional / Please choose ages category'), ('Beavers', 'Beavers'), ('Cubs', 'Cubs'),
        ('Scouts', 'Scouts'), ('Ventures', 'Ventures'), ('Rovers', 'Rovers'), ('Adult Volunteer', 'Adult Volunteer'),
        ('Beavers & Cubs', 'Beavers & Cubs'), ('Scouts & Ventures', 'Scouts & Ventures'),
        ('Rovers & Volunteers', 'Rovers & Volunteers')
    ]
    ages = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES_AGE,
        max_length=(max(len(value) for _, value in CHOICES_AGE)),
    )
    CHOICES_SIZE = [
        (None, 'Optional / Please choose size category'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'),
        ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')
    ]
    size = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES_SIZE,
        max_length=(max(len(value) for _, value in CHOICES_SIZE)),

    )
    CHOICES_GENDER = [(None, 'Optional / Please choose gender category'), ('Male', 'Male'), ('Female', 'Female')]
    gender = models.CharField(
        null=True,
        blank=True,
        choices=CHOICES_GENDER,
        max_length=(max(len(value) for _, value in CHOICES_GENDER)),
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
