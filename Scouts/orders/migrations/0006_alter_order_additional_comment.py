# Generated by Django 4.1.3 on 2022-12-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_additional_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='additional_comment',
            field=models.CharField(blank=True, default='ok', max_length=300),
        ),
    ]
