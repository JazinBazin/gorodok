# Generated by Django 2.1.7 on 2019-03-01 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_auto_20190301_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartmentimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='commercialimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='garageimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='houseimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterModelOptions(
            name='landimage',
            options={'verbose_name': 'Фотография', 'verbose_name_plural': 'Фотографии'},
        ),
    ]
