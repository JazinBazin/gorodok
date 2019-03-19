from django import forms


class UserBasicForm(forms.Form):

    user_name = forms.CharField(
        label='Ваше имя:',
        min_length=2,
        max_length=100,
        strip=True,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        })
    )

    user_phone = forms.CharField(
        min_length=11,
        max_length=11,
        label="Номер телефона:",
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'phoneNumber'
        })
    )

    user_email = forms.EmailField(
        label='Ваш email:',
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        })
    )

    user_message = forms.CharField(
        label='Сообщение:',
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Ваши пожелания',
            'rows': '5'
        })
    )
