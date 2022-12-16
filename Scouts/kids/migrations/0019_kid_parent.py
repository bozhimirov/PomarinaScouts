# Generated by Django 4.1.3 on 2022-12-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account_profile', '0018_alter_profile_gender'),
        ('kids', '0018_alter_kid_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='kid',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account_profile.profile'),
        ),
    ]
