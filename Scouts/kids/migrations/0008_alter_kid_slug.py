# Generated by Django 4.1.3 on 2022-12-09 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0007_alter_kid_date_of_birth_alter_kid_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kid',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]