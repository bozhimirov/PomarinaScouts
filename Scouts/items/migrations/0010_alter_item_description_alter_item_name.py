# Generated by Django 4.1.3 on 2022-12-09 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_alter_item_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.CharField(blank=True, help_text='Optional / Description of the Item ', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, help_text='Optional / Name of the item ', max_length=30, null=True),
        ),
    ]
