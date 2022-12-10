# Generated by Django 4.1.3 on 2022-12-10 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0009_alter_kid_first_name_alter_kid_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='Required / Please choose', help_text='Please choose', max_length=6),
        ),
    ]
