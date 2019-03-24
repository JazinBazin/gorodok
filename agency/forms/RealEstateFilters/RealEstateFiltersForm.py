import sys
from django import forms


class RealEstateFiltersForm(forms.Form):

    sort_type = forms.ChoiceField(
        label='Сортировка:',
        choices=(
            ('Do not sort', 'Не сортировать'),
            ('price', 'По цене'),
            # ('number_of_rooms', 'По количеству комнат'),
            # ('floor_number', 'По номеру этажа')
        ),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    sort_order = forms.ChoiceField(
        label='Тип сортировки:',
        choices=(
            ('Ascending', 'По возрастанию'),
            ('Descending', 'По убыванию')
        ),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    type_of_transaction = forms.ChoiceField(
        label='Вид сделки:',
        choices=(
            ('Any', 'Не важно'),
            ('purchase', 'Покупка'),
            ('rent', 'Аренда'),
            ('swap', 'Обмен')
        ),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    square_from = forms.IntegerField(
        label="Площадь:",
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

    def get_filtered(self, real_estate_type):
        filtered = real_estate_type.objects.filter(
            status='published',
            price__gte=self.cleaned_data['price_from'],
            price__lte=self.cleaned_data['price_to'],
            square__gte=self.cleaned_data['square_from'],
            square__lte=self.cleaned_data['square_to'])

        if self.cleaned_data['type_of_transaction'] != 'Any':
            filtered = filtered.filter(
                type_of_transaction=self.cleaned_data['type_of_transaction'])

        if self.cleaned_data['sort_type'] != 'Do not sort':
            if self.cleaned_data['sort_order'] == 'Ascending':
                filtered = filtered.order_by(
                    self.cleaned_data['sort_type'])
            else:  # Descending
                filtered = filtered.order_by(
                    "-" + self.cleaned_data['sort_type'])

        return filtered

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['square_from'] is None:
            cleaned_data['square_from'] = 0
        if cleaned_data['square_to'] is None:
            cleaned_data['square_to'] = sys.maxsize
        if cleaned_data['price_from'] is None:
            cleaned_data['price_from'] = 0
        if cleaned_data['price_to'] is None:
            cleaned_data['price_to'] = sys.maxsize
        return cleaned_data
