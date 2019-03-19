from django import forms
from .UserBasicForm import UserBasicForm
from .RealEstatePropertiesForm import RealEstatePropertiesForm

# Необходима регистрация для контроля количества объявлений
# Не допустима почта без привязкии к номеру телефона
# Необходим контроль размера и формата загружаемых изображений

# Добавить поля:
# 1) Титульное изображение
# 2) Изображения
class AdvertForm(UserBasicForm, RealEstatePropertiesForm):
    title_text = forms.CharField(
        label="Заголовок:",
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))

    description = forms.CharField(
        label='Описание:',
        max_length=500,
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ваши пожелания',
            'rows': '5'
        }))

    address = forms.CharField(
        label="Адрес:",
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
