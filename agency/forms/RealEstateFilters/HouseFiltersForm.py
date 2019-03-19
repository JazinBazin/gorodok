import sys
from django import forms
from .RealEstateFiltersForm import RealEstateFiltersForm
from agency.models import House


class HouseFiltersForm(RealEstateFiltersForm):
    
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

    floor_count_from = forms.IntegerField(
        label='Количество этажей:',
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

    def get_filtered(self):
        filtered_houses = super().get_filtered(House)
        filtered_houses = filtered_houses.filter(
            number_of_rooms__gte=self.cleaned_data['number_of_rooms_from'],
            number_of_rooms__lte=self.cleaned_data['number_of_rooms_to'],
            floor_count__gte=self.cleaned_data['floor_count_from'],
            floor_count__lte=self.cleaned_data['floor_count_to'])

        return filtered_houses

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['floor_count_from'] is None:
            cleaned_data['floor_count_from'] = 1
        if cleaned_data['floor_count_to'] is None:
            cleaned_data['floor_count_to'] = sys.maxsize
        if cleaned_data['number_of_rooms_from'] is None:
            cleaned_data['number_of_rooms_from'] = 0
        if cleaned_data['number_of_rooms_to'] is None:
            cleaned_data['number_of_rooms_to'] = sys.maxsize
        return cleaned_data
