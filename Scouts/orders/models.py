from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from Scouts.accounts.models import AppUser
from Scouts.core.validators import validate_gt_zero, validate_max_quantity
from Scouts.items.models import Item

UserModel = get_user_model()


class Order(models.Model):
    MIN_DESCRIPTION_LENGTH = 5
    MAX_DESCRIPTION_LENGTH = 300

    MAX_NAME_LENGTH = 100
    MAX_LOCATION_LENGTH = 30

    CHOICES_CATEGORY = [
        (None, 'Required / Please choose category of the item'), ('Hoodies', 'Hoodies'), ('T-shirts', 'T-shirts'),
        ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Trousers', 'Trousers'),
        ('Soft Shell', 'Soft Shell'), ('Others', 'Others')
    ]

    category = models.CharField(
        null=False,
        blank=False,
        choices=CHOICES_CATEGORY,
        max_length=MAX_NAME_LENGTH,
    )

    item_name = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_NAME_LENGTH,
        help_text='Optional / Name of the item',

    )

    CHOICES_AGE = [
        (None, 'Required / Please choose ages category'), ('Beavers', 'Beavers'), ('Cubs', 'Cubs'),
        ('Scouts', 'Scouts'), ('Ventures', 'Ventures'), ('Rovers', 'Rovers'), ('Adult Volunteer', 'Adult Volunteer'),
        ('Beavers & Cubs', 'Beavers & Cubs'), ('Scouts & Ventures', 'Scouts & Ventures'),
        ('Rovers & Volunteers', 'Rovers & Volunteers')
    ]
    ages = models.CharField(
        null=False,
        blank=False,
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

    quantity = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=(
            validate_gt_zero,
            validate_max_quantity,
        ),
        help_text='Required / Please choose quantity of item',
    )

    CHOICES_DELIVERY = [
        (None, 'Required / Please choose place to receive items'), ('Office', 'Office'),
        ('I will provide details in comments', 'I will provide details in comments')
    ]
    place_to_deliver = models.CharField(
        null=False,
        blank=False,
        choices=CHOICES_DELIVERY,
        max_length=MAX_NAME_LENGTH,
    )

    comments = models.TextField(
        max_length=MAX_DESCRIPTION_LENGTH,
        null=True,
        blank=True,
        help_text='Comments on order or place to receive',
    )

    publication_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        verbose_name='date created',
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
