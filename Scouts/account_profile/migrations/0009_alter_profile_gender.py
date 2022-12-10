# Generated by Django 4.1.3 on 2022-12-10 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0008_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('empty_label', 'Optional / Please choose gender'), ('male', 'Male'), ('female', 'Female')], default='empty_label', max_length=11, null=True),
        ),
    ]
