# Generated by Django 2.1.7 on 2019-02-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_delete_socialnetwork'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='agency/images/SocialNetworksImages', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Социальная сеть',
                'verbose_name_plural': 'Социальные сети',
            },
        ),
    ]
