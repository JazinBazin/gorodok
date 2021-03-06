# Generated by Django 2.1.7 on 2019-02-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_auto_20190228_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialnetwork',
            name='image',
            field=models.ImageField(upload_to='agency/images/SocialNetworksImages', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='link',
            field=models.URLField(verbose_name='Ссылка'),
        ),
        migrations.AlterField(
            model_name='socialnetwork',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
