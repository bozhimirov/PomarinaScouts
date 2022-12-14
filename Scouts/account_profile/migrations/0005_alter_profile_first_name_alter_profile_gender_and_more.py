# Generated by Django 4.1.3 on 2022-12-08 23:50

import Scouts.core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0004_remove_profile_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Scouts.core.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], help_text='Optional / Please choose', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), Scouts.core.validators.validate_only_letters]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(error_messages={'required': 'Place phone number in format: 0987654321'}, max_length=10, validators=[Scouts.core.validators.validate_mobile_number, Scouts.core.validators.validate_only_numbers]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, help_text='Optional / Upload your photo here', null=True, upload_to='users_photos', validators=[Scouts.core.validators.validate_file_less_than_5mb]),
        ),
    ]
