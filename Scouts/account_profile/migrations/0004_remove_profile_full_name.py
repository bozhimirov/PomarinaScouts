# Generated by Django 4.1.3 on 2022-12-06 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0003_profile_full_name_alter_profile_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
    ]
