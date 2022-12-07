# Generated by Django 4.1.3 on 2022-12-06 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0005_alter_kid_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
