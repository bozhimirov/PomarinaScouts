import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from Scouts.accounts.models import AppUser
from Scouts.kids.models import Kid

UserModel = get_user_model()


class Payment(models.Model):
    ANNUAL_TAX = 40
    MONTHLY_TAX = 30
    MAX_NAME_LENGTH = 100
    MAX_DESCRIPTION_LENGTH = 300
    CHOICES = [
        (None, 'Required / Select payment type'),
        ('Monthly Tax', 'Monthly Tax'),
        ('Annual Fee', 'Annual Fee')
    ]

    model_name = models.CharField(
        null=False,
        blank=False,
        choices=CHOICES,
        max_length=MAX_NAME_LENGTH,
    )

    staff_member = models.CharField(
        max_length=MAX_NAME_LENGTH,
    )

    kid = models.ForeignKey(
        Kid,
        null=True,
        blank=True,
        related_name='user_kid_type',
        on_delete=models.SET_NULL,
        help_text='Required / Select Kid to generate payment',
    )
    parent = models.ForeignKey(
        UserModel,
        null=True,
        blank=True,
        related_name='payment_parent',
        on_delete=models.SET_NULL,
    )

    tax_per_kid = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text='Required / Tax depending of number of kids per parent',
    )

    period_billed = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_NAME_LENGTH,
        help_text='Required / Billed period',
    )

    comments = models.TextField(
        null=True,
        blank=True,
        help_text='Optional / Comments on payment',
    )

    generated_date = models.DateField(
        # Automatically sets current date on `save` (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )

    confirmed_by_user = models.DateTimeField(
        null=True,
        blank=True,
    )

    paid = models.BooleanField(
        default=False,
    )

    confirmed_by_staff = models.DateTimeField(
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        null=False,
        blank=True,

    )

    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.pk}-{self.kid}')

        return super().save(*args, **kwargs)

    class Meta:
        ordering = [
            '-paid',
            'confirmed_by_user',
            'generated_date',
        ]
