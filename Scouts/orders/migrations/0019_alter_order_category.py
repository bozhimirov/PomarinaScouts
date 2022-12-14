# Generated by Django 4.1.3 on 2022-12-13 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_order_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='category',
            field=models.CharField(blank=True, choices=[('Hoodies', 'Hoodies'), ('Tshirts', 'T-shirts'), ('Shirts', 'Shirts'), ('Hats', 'Hats'), ('Scarves', 'Scarves'), ('Trousers', 'Trousers'), ('SoftShell', 'Soft Shell'), ('Others', 'Others')], help_text='Required / Please choose category of the item', max_length=100, null=True),
        ),
    ]
