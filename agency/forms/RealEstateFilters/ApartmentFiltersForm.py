import sys
from django import forms
from .RealEstateFiltersForm import RealEstateFiltersForm
from agency.models import Apartment


class ApartmentFiltersForm(RealEstateFiltersForm):

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

    def get_filtered(self):
        filtered_apartments = super().get_filtered(Apartment)
        filtered_apartments = filtered_apartments.filter(
            floor_number__gte=self.cleaned_data['floor_number_from'],
            floor_number__lte=self.cleaned_data['floor_number_to'],
            number_of_rooms__gte=self.cleaned_data['number_of_rooms_from'],
            number_of_rooms__lte=self.cleaned_data['number_of_rooms_to'])

        return filtered_apartments

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['floor_number_from'] is None:
            cleaned_data['floor_number_from'] = -(sys.maxsize + 1)
        if cleaned_data['floor_number_to'] is None:
            cleaned_data['floor_number_to'] = sys.maxsize
        if cleaned_data['number_of_rooms_from'] is None:
            cleaned_data['number_of_rooms_from'] = 0
        if cleaned_data['number_of_rooms_to'] is None:
            cleaned_data['number_of_rooms_to'] = sys.maxsize
        return cleaned_data
