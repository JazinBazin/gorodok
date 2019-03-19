from django import forms


class RealEstatePropertiesForm(forms.Form):

    purchase_or_rent = forms.ChoiceField(
        label='Услуга:',
        required=True,
        choices=(
            ('Покупка', 'Покупка'),
            ('Аренда', 'Аренда')
        ),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    service_type = forms.ChoiceField(
        required=True,
        choices=(
            ('Квартира', 'Квартира'),
            ('Дом/Дача', 'Дом/Дача'),
            ('Земля', 'Земля'),
            ('Гараж', 'Гараж'),
            ('Коммерция', 'Коммерция')
        ),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    number_of_rooms_from = forms.IntegerField(
        label="Количество комнат:",
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'От'
        })
    )

    number_of_rooms_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'До'
        })
    )

    floor_number_from = forms.IntegerField(
        label='Номер этажа:',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'От'
        })
    )

    floor_number_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'До'
        })
    )

    floor_count_from = forms.IntegerField(
        label="Количество этажей:",
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'От'
        })
    )

    floor_count_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'До'
        })
    )

    square_from = forms.IntegerField(
        label='Площадь:',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'От'
        })
    )

    square_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'До'
        })
    )

    square_units = forms.ChoiceField(
        required=True,
        choices=(
            ('м²', 'м²'),
            ('га', 'га')
        ),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    price_from = forms.IntegerField(
        label='Цена:',
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'От'
        })
    )

    price_to = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'До'
        })
    )
