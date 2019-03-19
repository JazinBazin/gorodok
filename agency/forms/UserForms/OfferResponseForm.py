from django.core.mail import send_mail
from .UserBasicForm import UserBasicForm


class OfferResponseForm(UserBasicForm):

    def send_mail(self, vendor_code):
        message = \
            "Артикул: " + vendor_code + "\n" + \
            "Имя: " + self.cleaned_data['user_name'] + "\n" + \
            "Номер телефона: " + self.cleaned_data['user_phone'] + "\n"

        if self.cleaned_data['user_email'] is not None:
            message += 'email: ' + self.cleaned_data['user_email'] + "\n"

        if self.cleaned_data['user_message'] is not None:
            message += 'Сообщение пользователя: ' + \
                self.cleaned_data['user_message'] + "\n"

        send_mail(
            'Отклик на объявление. Артикул: ' + vendor_code,
            message,
            'gorodok@gorodok-krym.com',
            ['gorodok@gorodok-krym.com'],
            fail_silently=False,
        )
