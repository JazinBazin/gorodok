# Generated by Django 2.1.7 on 2019-03-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0020_partner_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
    ]
