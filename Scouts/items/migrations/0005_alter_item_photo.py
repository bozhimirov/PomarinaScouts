# Generated by Django 4.1.3 on 2022-12-08 23:50

import Scouts.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_alter_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='items_photos/', validators=[Scouts.core.validators.validate_file_less_than_5mb]),
        ),
    ]
