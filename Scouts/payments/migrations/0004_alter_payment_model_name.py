# Generated by Django 4.1.3 on 2022-12-10 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_payment_comments_alter_payment_kid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='model_name',
            field=models.CharField(choices=[('required', 'Required / Please choose'), ('MonthlyTax', 'Monthly Tax'), ('AnnualFee', 'Annual Fee')], help_text='Required / Select payment type', max_length=10),
        ),
    ]
