# Generated by Django 4.1.3 on 2022-12-13 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_order_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ages',
            field=models.CharField(choices=[(None, 'Required / Please choose ages category'), ('Beavers', 'Beavers'), ('Cubs', 'Cubs'), ('Scouts', 'Scouts'), ('Ventures', 'Ventures'), ('Rovers', 'Rovers'), ('Adult Volunteer', 'Adult Volunteer'), ('Beavers & Cubs', 'Beavers & Cubs'), ('Scouts & Ventures', 'Scouts & Ventures'), ('Rovers & Volunteers', 'Rovers & Volunteers')], max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(choices=[(None, 'Required / Please choose category of the item'), ('Hoodies', 'Hoodies'), ('T-shirts', 'T-shirts'), ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Trousers', 'Trousers'), ('Soft Shell', 'Soft Shell'), ('Others', 'Others')], default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'Optional / Please choose gender category'), ('Male', 'Male'), ('Female', 'Female')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='place_to_deliver',
            field=models.CharField(choices=[(None, 'Required / Please choose place to receive items'), ('Office', 'Office'), ('I will provide details in comments', 'I will provide details in comments')], max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(blank=True, choices=[(None, 'Optional / Please choose size category'), ('XXS', 'XXS'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL'), ('XXXL', 'XXXL')], max_length=100, null=True),
        ),
    ]
