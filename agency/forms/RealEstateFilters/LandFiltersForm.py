from .RealEstateFiltersForm import RealEstateFiltersForm
from agency.models import Land


class LandFiltersForm(RealEstateFiltersForm):
    
    def get_filtered(self):
        filtered_lands = super().get_filtered(Land)
        return filtered_lands

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
