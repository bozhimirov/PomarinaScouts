from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from Scouts.core.model_mixins import StrFromFieldsMixin, ItemCategory, AgeGroup, Size, Gender
from Scouts.core.validators import validate_file_less_than_5mb

UserModel = get_user_model()


class Item(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'category')
    MIN_DESCRIPTION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30
    MAX_NAME = 30

    photo = models.ImageField(
        upload_to='items_photos/',
        null=False,
        blank=True,
        validators=(
            validate_file_less_than_5mb,
        ),
        # on_delete=...
        # https: // stackoverflow.com / questions / 16041232 / django - delete - filefield
    )

    name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_NAME,
    )

    category = models.CharField(
        null=False,
        blank=False,
        choices=ItemCategory.choices(),
        max_length=ItemCategory.max_len(),
    )
    # consider Float-field if necessary for price
    price = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    ages = models.CharField(
        null=True,
        blank=True,
        choices=AgeGroup.choices(),
        max_length=AgeGroup.max_len(),
    )

    size = models.CharField(
        null=True,
        blank=True,
        choices=Size.choices(),
        max_length=Size.max_len(),
    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
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
            self.name = slugify(f'{self.pk}-{self.category}-{self.price}')

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['slug']


class UsedItem(StrFromFieldsMixin, models.Model):
    str_fields = ('pk', 'photo', 'category')
    MIN_DESCRIPTION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300
    MAX_LOCATION_LENGTH = 30
    MAX_NAME = 30

    photo = models.ImageField(
        upload_to='used_items_photos/',
        null=False,
        blank=True,
        validators=(
            validate_file_less_than_5mb,
        ),
    )

    category = models.CharField(
        null=False,
        blank=False,
        choices=ItemCategory.choices(),
        max_length=ItemCategory.max_len(),
    )

    ages = models.CharField(
        null=True,
        blank=True,
        choices=AgeGroup.choices(),
        max_length=AgeGroup.max_len(),
    )

    size = models.CharField(
        null=True,
        blank=True,
        choices=Size.choices(),
        max_length=Size.max_len(),
    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_len(),
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=False,
        blank=False,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
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
