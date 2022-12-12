# Generated by Django 4.1.3 on 2022-12-10 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0016_alter_item_ages_alter_item_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='optional', max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='useditem',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='optional', max_length=6, null=True),
        ),
    ]