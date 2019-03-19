from .RealEstateFiltersForm import RealEstateFiltersForm
from agency.models import Garage


class GarageFiltersForm(RealEstateFiltersForm):

    def get_filtered(self):
        filtered_garages = super().get_filtered(Garage)
        return filtered_garages

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
