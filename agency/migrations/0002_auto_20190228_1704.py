# Generated by Django 2.1.7 on 2019-02-28 14:04

import agency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentimage',
            name='image',
            field=models.ImageField(upload_to=agency.models.real_estate_image_path),
        ),
        migrations.AlterField(
            model_name='commercialimage',
            name='image',
            field=models.ImageField(upload_to=agency.models.real_estate_image_path),
        ),
        migrations.AlterField(
            model_name='garageimage',
            name='image',
            field=models.ImageField(upload_to=agency.models.real_estate_image_path),
        ),
        migrations.AlterField(
            model_name='houseimage',
            name='image',
            field=models.ImageField(upload_to=agency.models.real_estate_image_path),
        ),
        migrations.AlterField(
            model_name='landimage',
            name='image',
            field=models.ImageField(upload_to=agency.models.real_estate_image_path),
        ),
    ]
