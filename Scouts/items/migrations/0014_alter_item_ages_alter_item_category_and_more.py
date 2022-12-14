# Generated by Django 4.1.3 on 2022-12-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0013_alter_item_ages_alter_item_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='ages',
            field=models.CharField(blank=True, choices=[('optional', 'Optional / Please choose'), ('Beavers', 'Beavers'), ('Cubs', 'Cubs'), ('Scouts', 'Scouts'), ('Ventures', 'Ventures'), ('Rovers', 'Rovers'), ('AdultVolunteer', 'Adult Volunteer'), ('SmallKids', 'Beavers & Cubs'), ('TeenKids', 'Scouts & Ventures'), ('Adults', 'Rovers & Volunteers')], default='optional', help_text='Optional / Please choose Age category ', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('required', 'Required / Please choose'), ('Hoodies', 'Hoodies'), ('Tshirts', 'T-shirts'), ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Others', 'Others')], default='required', help_text='Required / Please choose category of the item', max_length=8),
        ),
        migrations.AlterField(
            model_name='item',
            name='gender',
            field=models.CharField(blank=True, choices=[('optional', 'Optional / Please choose'), ('male', 'Male'), ('female', 'Female')], default='optional', help_text='Optional / Please choose Gender category ', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, default='optional', help_text='Optional / Name of the item ', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, choices=[('optional', 'Optional / Please choose'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='optional', help_text='Optional / Please choose Size category ', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='useditem',
            name='ages',
            field=models.CharField(blank=True, choices=[('optional', 'Optional / Please choose'), ('Beavers', 'Beavers'), ('Cubs', 'Cubs'), ('Scouts', 'Scouts'), ('Ventures', 'Ventures'), ('Rovers', 'Rovers'), ('AdultVolunteer', 'Adult Volunteer'), ('SmallKids', 'Beavers & Cubs'), ('TeenKids', 'Scouts & Ventures'), ('Adults', 'Rovers & Volunteers')], default='optional', help_text='Optional / Please choose Age category ', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='useditem',
            name='category',
            field=models.CharField(choices=[('required', 'Required / Please choose'), ('Hoodies', 'Hoodies'), ('Tshirts', 'T-shirts'), ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Others', 'Others')], default='required', help_text='Required / Please choose category of the item', max_length=8),
        ),
        migrations.AlterField(
            model_name='useditem',
            name='gender',
            field=models.CharField(blank=True, choices=[('optional', 'Optional / Please choose'), ('male', 'Male'), ('female', 'Female')], default='optional', help_text='Optional / Please choose Gender category ', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='useditem',
            name='size',
            field=models.CharField(blank=True, choices=[('optional', 'Optional / Please choose'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], default='optional', help_text='Optional / Please choose Size category ', max_length=8, null=True),
        ),
    ]
