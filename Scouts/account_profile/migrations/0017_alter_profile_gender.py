# Generated by Django 4.1.3 on 2022-12-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0016_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'Optional / Please choose gender'), ('Male', 'Male'), ('Female', 'Female')], max_length=31, null=True),
        ),
    ]
