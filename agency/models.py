import os
from django.db import models
from django.utils import timezone
from colorful.fields import RGBColorField


class Background(models.Model):
    class Meta:
        verbose_name = 'Фон'
        verbose_name_plural = 'Фон'

    page_name = models.CharField(max_length=100, verbose_name='Страница')

    def __str__(self):
        return self.page_name


class BackgroundData(models.Model):
    class Meta:
        verbose_name = 'Цвет и изображение'
        verbose_name_plural = 'Цвет и изображение'

    background = models.ForeignKey(
        Background, on_delete=models.CASCADE, related_name='data')
    background_color = RGBColorField(verbose_name='Цвет', default='#ffffff')
    background_image = models.ImageField(
        upload_to="agency/images/BackgroundImages", blank=True, verbose_name='Изображение')


class SocialNetwork(models.Model):
    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'

    title = models.CharField(max_length=100, verbose_name='Название')
    link = models.CharField(max_length=100, verbose_name='Ссылка')
    image = models.ImageField(
        upload_to="agency/images/SocialNetworksImages", verbose_name='Изображение')

    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    class Meta:
        verbose_name = 'Вид недвижимого имущества'
        verbose_name_plural = 'Виды недвижимого имущества'

    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(
        upload_to="agency/images/ProductCategoriesImages", verbose_name='Изображение')
    link = models.CharField(max_length=100, verbose_name='Ссылка')

    def __str__(self):
        return self.title


class Advantage(models.Model):
    class Meta:
        verbose_name = 'Вид преимущества'
        verbose_name_plural = 'Преимущества'

    title = models.CharField(
        max_length=100, verbose_name='Титульный заголовок')
    image = models.ImageField(
        upload_to="agency/images/AdvantagesImages", verbose_name='Изображение')

    def __str__(self):
        return self.title


class AdvantageListItem(models.Model):
    class Meta:
        verbose_name = 'Пункт списка'
        verbose_name_plural = 'Описание преимущества'

    advantage = models.ForeignKey(
        Advantage, related_name='list_items', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Пункт списка')

    def __str__(self):
        return self.text


class Feedback(models.Model):
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    author = models.CharField(max_length=100, verbose_name='Автор')
    image = models.ImageField(
        upload_to="agency/images/FeedbacksImages", verbose_name='Фото',
        blank=True)
    feedback_text = models.TextField(verbose_name='Текст отзыва', blank=True)
    video_link = models.URLField(verbose_name='Видео', blank=True)

    def __str__(self):
        return self.author


class Contact(models.Model):
    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    email = models.CharField(max_length=100, verbose_name='Электронная почта')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    working_days = models.CharField(max_length=100, verbose_name='Рабочие дни')
    working_time = models.CharField(
        max_length=100, verbose_name='Рабочее время')
    break_time = models.CharField(max_length=100, verbose_name='Перерыв')
    ogrn = models.CharField(max_length=100, verbose_name='ОГРН', blank=True)
    inn = models.CharField(max_length=100, verbose_name='ИНН', blank=True)

    def __str__(self):
        return "Контакты агенства недвижимости"


class ContactPhone(models.Model):
    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'

    contact = models.ForeignKey(
        Contact, related_name='phones', on_delete=models.CASCADE)
    phone = models.CharField(max_length=100, verbose_name='Номер телефона')

    def __str__(self):
        return self.phone


def real_estate_title_image_path(instance, filename):
    return 'agency/images/{0}/{1}'.format(instance.title_image_directory, filename)


class Service(models.Model):
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    title = models.CharField(
        max_length=100, verbose_name='Титульный заголовок услуги')

    def __str__(self):
        return self.title


class ServiceListItem(models.Model):
    class Meta:
        verbose_name = 'Пункт списка'
        verbose_name_plural = 'Описание услуги'

    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name='list_items')
    text = models.TextField(verbose_name='Пункт списка')

    def __str__(self):
        return self.text


class AboutCompanyBlock(models.Model):
    class Meta:
        verbose_name = 'Блок описания'
        verbose_name_plural = 'О нас'

    title = models.CharField(
        max_length=100, verbose_name='Титульный заголовок')
    image = models.ImageField(
        upload_to='agency/images/AboutCompanyImages', blank=True, verbose_name='Изображение')
    text = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class RealEstate(models.Model):
    class Meta:
        abstract = True
        indexes = [
            models.Index(fields=['status', 'is_hot_offer'])
        ]
    status = models.CharField(
        max_length=20,
        choices=(('published', 'Опубликовано'),
                 ('archived', 'В архиве'),
                 ('application', 'Заявка пользователя')),
        default='published',
        verbose_name='Статус')
    is_hot_offer = models.BooleanField(
        default=False, verbose_name='Горячее предложение')
    title_text = models.CharField(
        max_length=100, verbose_name='Титульный заголовок')
    image = models.ImageField(
        upload_to=real_estate_title_image_path,
        verbose_name='Титульное изображение')
    description = models.TextField(verbose_name='Описание')
    vendor_code = models.CharField(
        max_length=20, unique=True, verbose_name='Артикул')
    type_of_transaction = models.CharField(
        max_length=8, choices=(
            ('purchase', 'Продажа'),
            ('rent', 'Аренда'),
            ('swap', 'Обмен')),
        default='purchase', verbose_name='Вид сделки')
    address = models.CharField(max_length=200, verbose_name='Адрес')
    owner_phone = models.CharField(
        max_length=100, verbose_name='Номер телефона владельца')
    price = models.IntegerField(verbose_name='Цена')
    square = models.DecimalField(
        max_digits=19, decimal_places=10, verbose_name='Площадь')
    area_units = models.CharField(
        max_length=20,
        choices=(
            ('square meters', 'м²'),
            ('hectares', 'га')
        ),
        default='square meters',
        verbose_name='Единицы измерения площади'
    )
    edit_date = models.DateTimeField(
        auto_now=True, verbose_name='Дата последнего редактирования')

    def __str__(self):
        return "Арт. " + self.vendor_code + " (" + self.title_text + ")"


def real_estate_image_path(instance, filename):
    return 'agency/images/{0}/{1}/'.format(instance.image_directory, filename)


class RealEstateImage(models.Model):
    class Meta:
        abstract = True
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'

    image = models.ImageField(
        upload_to=real_estate_image_path, verbose_name='Фотография')

    def __str__(self):
        return "{0}".format(self.image)


class Apartment(RealEstate):
    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

    title_image_directory = 'ApartmentsTitleImages'
    number_of_rooms = models.IntegerField(verbose_name='Количество комнат')
    floor_number = models.IntegerField(verbose_name='Номер этажа')


class ApartmentImage(RealEstateImage):
    apartment = models.ForeignKey(
        Apartment, on_delete=models.CASCADE, related_name='images')
    image_directory = 'ApartmentsImages'


class House(RealEstate):
    class Meta:
        verbose_name = 'Дом/Дача'
        verbose_name_plural = 'Дома/Дачи'

    title_image_directory = 'HousesTitleImages'
    house_type = models.CharField(
        max_length=13, choices=(('house', 'Дом'), ('country_house', 'Дача')),
        default='house', verbose_name='Дом/Дача')
    number_of_rooms = models.IntegerField(verbose_name='Количество комнат')
    floor_count = models.IntegerField(verbose_name='Количество этажей')


class HouseImage(RealEstateImage):
    house = models.ForeignKey(
        House, on_delete=models.CASCADE, related_name='images')
    image_directory = 'HousesImages'


class Land(RealEstate):
    class Meta:
        verbose_name = 'Земля'
        verbose_name_plural = 'Земли'
    title_image_directory = 'LandsTitleImages'


class LandImage(RealEstateImage):
    land = models.ForeignKey(
        Land, on_delete=models.CASCADE, related_name='images')
    image_directory = 'LandsImages'


class Garage(RealEstate):
    class Meta:
        verbose_name = 'Гараж'
        verbose_name_plural = 'Гаражи'
    title_image_directory = 'GaragesTitleImages'


class GarageImage(RealEstateImage):
    garage = models.ForeignKey(
        Garage, on_delete=models.CASCADE, related_name='images')
    image_directory = 'GaragesImages'


class Commercial(RealEstate):
    class Meta:
        verbose_name = 'Коммерческая недвижимость'
        verbose_name_plural = 'Коммерческая недвижимость'
    title_image_directory = 'CommercialsTitleImages'


class CommercialImage(RealEstateImage):
    commercial = models.ForeignKey(
        Commercial, on_delete=models.CASCADE, related_name='images')
    image_directory = 'CommercialsImages'


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    status = models.CharField(max_length=20,
                              choices=(
                                  ('published', 'Опубликовано'),
                                  ('archived', 'В архиве')),
                              default='archived',
                              verbose_name='Статус')
    headline = models.CharField(max_length=200, verbose_name='Заголовок')
    publication_date = models.DateTimeField(default=timezone.now,
                                            verbose_name='Дата публикации')
    image = models.ImageField(upload_to='agency/images/NewsImages',
                              verbose_name='Изображение')
    text = models.TextField(verbose_name='Текст новости')
    link_to_source = models.URLField(verbose_name="Ссылка на источник",
                                     blank=True)

    def __str__(self):
        return self.headline


class Partner(models.Model):
    class Meta:
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

    image = models.ImageField(
        upload_to='agency/images/PartnersImages', verbose_name='Логотип')
    link = models.URLField(verbose_name='Ссылка', blank=True)
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name


list_of_models_with_image = (
    SocialNetwork, ProductCategory, Advantage, Feedback, AboutCompanyBlock,
    News, Partner, Apartment, ApartmentImage, House, HouseImage, Land,
    LandImage, Garage, GarageImage, Commercial, CommercialImage)


def receiver_with_multiple_senders(signal, senders, **kwargs):
    def decorator(receiver_function):
        for sender in senders:
            signal.connect(receiver_function, sender=sender, **kwargs)
        return receiver_function
    return decorator


@receiver_with_multiple_senders(models.signals.post_delete,
                                list_of_models_with_image)
def delete_image_file_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver_with_multiple_senders(models.signals.pre_save,
                                list_of_models_with_image)
def delete_image_file_on_save(sender, instance, **kwargs):
    if not instance.pk:
        return

    old_image = sender.objects.get(pk=instance.pk).image
    if not old_image:
        return

    new_image = instance.image
    if not old_image == new_image:
        if os.path.isfile(old_image.path):
            os.remove(old_image.path)
