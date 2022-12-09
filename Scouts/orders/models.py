from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from Scouts.accounts.models import AppUser
from Scouts.core.model_mixins import AgeGroup, Size, Gender, ItemCategory, Delivery
from Scouts.core.validators import validate_gt_zero
from Scouts.items.models import Item

UserModel = get_user_model()


class Order(models.Model):
    MIN_DESCRIPTION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300

    MAX_NAME_LENGTH = 100
    MAX_LOCATION_LENGTH = 30

    category = models.CharField(
        null=True,
        blank=True,
        choices=ItemCategory.choices(),
        max_length=MAX_NAME_LENGTH,
        help_text='Required / Please choose category of the item',
    )

    item_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_NAME_LENGTH,
        help_text='Optional / Name of the item',

    )

    ages = models.CharField(
        null=False,
        blank=False,
        choices=AgeGroup.choices(),
        max_length=AgeGroup.max_len(),
        help_text='Required / Please choose ages category',
    )

    size = models.CharField(
        null=True,
        blank=True,
        choices=Size.choices(),
        max_length=Size.max_len(),
        help_text='Optional / Please choose size category',
    )

    gender = models.CharField(
        null=True,
        blank=True,
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        help_text='Optional / Please choose gender category',
    )

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validate_gt_zero,
        ),
        help_text='Required / Please choose quantity of item',
    )

    place_to_deliver = models.CharField(
        null=False,
        blank=False,
        choices=Delivery.choices(),
        max_length=Delivery.max_len(),
        help_text='Required / Please choose place to receive item',
    )

    comments = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
        help_text='Comments on order or place to receive',
    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )
    #
    # price = models.ForeignKey(
    #
    # )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    staff_member = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    staff_member_finished = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_NAME_LENGTH,
    )

    sent = models.BooleanField(
        default=False,
    )

    confirmed_by_staff = models.DateTimeField(
        null=True,
        blank=True,
    )

    received = models.BooleanField(
        default=False,
    )

    received_by_user = models.DateTimeField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=False,
        blank=True,
    )

    additional_comment = models.CharField(
        default='ok',
        blank=True,
        null=True,
        max_length=MAX_DESCRIPTION_LENGTH,
    )

    def save(self, *args, **kwargs):
        # Create/Update

        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk}-{self.category}-{self.item_name}-{self.user}')

        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['slug']
