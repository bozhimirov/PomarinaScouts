# Generated by Django 4.1.3 on 2022-12-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0013_alter_kid_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='gender',
            field=models.CharField(choices=[('required', 'Required / Please choose gender'), ('male', 'Male'), ('female', 'Female')], default='required', max_length=8),
        ),
    ]
