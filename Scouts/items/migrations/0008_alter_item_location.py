# Generated by Django 4.1.3 on 2022-12-09 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_alter_item_location_alter_useditem_ages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='location',
            field=models.CharField(blank=True, help_text='Required / Location of the Item ', max_length=30, null=True),
        ),
    ]