from django import forms
from .UserBasicForm import UserBasicForm
from .RealEstatePropertiesForm import RealEstatePropertiesForm
from django.core.mail import send_mail
from datetime import date


class ApplicationForm(UserBasicForm, RealEstatePropertiesForm):

    def send_mail(self):

        for key in self.cleaned_data:
            if self.cleaned_data[key] is None:
                self.cleaned_data[key] = "\'Не указано\'"

        message = \
            "Имя: " + self.cleaned_data['user_name'] + "\n" + \
            "Телефон: " + self.cleaned_data['user_phone'] + "\n" + \
            "email: " + self.cleaned_data['user_email'] + "\n" + \
            "Услуга: " + self.cleaned_data['purchase_or_rent'] + ", " + \
            self.cleaned_data['service_type'] + "\n"

        if self.cleaned_data['purchase_or_rent'] == "Аренда":
            date_from = self.cleaned_data['rent_period_from']
            date_to = self.cleaned_data['rent_period_to']
            if isinstance(date_from, date):
                date_from = date_from.strftime('%d.%m.%Y')
            if isinstance(date_to, date):
                date_to = date_to.strftime('%d.%m.%Y')
            message += \
                "Период аренды c " + date_from + " до " + date_to + "\n"

        if self.cleaned_data['service_type'] == "Квартира":
            message += \
                "Количество комнат от " + \
                str(self.cleaned_data['number_of_rooms_from']) + \
                " до " + str(self.cleaned_data['number_of_rooms_to']) + "\n" + \
                "Номер этажа от " + str(self.cleaned_data['floor_number_from']) + \
                " до " + str(self.cleaned_data['floor_number_to']) + "\n"

        if self.cleaned_data['service_type'] == "Дом":
            message += \
                "Количество комнат от " + \
                str(self.cleaned_data['number_of_rooms_from']) + \
                " до " + str(self.cleaned_data['number_of_rooms_to']) + "\n" + \
                "Количество этажей от " + \
                str(self.cleaned_data['floor_count_from']) + \
                " до " + str(self.cleaned_data['floor_count_to']) + "\n"

        message += \
            "Площадь от " + str(self.cleaned_data['square_from']) + \
            " до " + str(self.cleaned_data['square_to']) + \
            " " + self.cleaned_data['square_units'] + "\n" + \
            "Цена от " + str(self.cleaned_data['price_from']) + \
            " до " + str(self.cleaned_data['price_to']) + " ₽\n"

        if self.cleaned_data['user_message']:
            message += "Сообщение пользователя:\n" + \
                self.cleaned_data['user_message'] + "\n"

        send_mail(
            'Заявка от пользователя ' + self.cleaned_data['user_name'],
            message,
            'gorodok@gorodok-krym.com',
            ['gorodok@gorodok-krym.com'],
            fail_silently=False,
        )

    rent_period_from = forms.DateField(
        label='Период аренды:',
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )

    rent_period_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
        })
    )
