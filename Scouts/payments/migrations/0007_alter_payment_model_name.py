# Generated by Django 4.1.3 on 2022-12-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_payment_model_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='model_name',
            field=models.CharField(choices=[('required', 'Required / Please choose type of payment'), ('MonthlyTax', 'Monthly Tax'), ('AnnualFee', 'Annual Fee')], help_text='Required / Select payment type', max_length=10),
        ),
    ]
