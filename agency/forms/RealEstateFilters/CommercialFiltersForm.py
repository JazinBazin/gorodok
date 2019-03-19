from .RealEstateFiltersForm import RealEstateFiltersForm
from agency.models import Commercial


class CommercialFiltersForm(RealEstateFiltersForm):

    def get_filtered(self):
        filtered_commercial = super().get_filtered(Commercial)
        return filtered_commercial

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
