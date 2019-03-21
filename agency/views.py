from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms.RealEstateFilters.ApartmentFiltersForm \
    import ApartmentFiltersForm
from .forms.RealEstateFilters.HouseFiltersForm \
    import HouseFiltersForm
from .forms.RealEstateFilters.LandFiltersForm \
    import LandFiltersForm
from .forms.RealEstateFilters.GarageFiltersForm \
    import GarageFiltersForm
from .forms.RealEstateFilters.CommercialFiltersForm \
    import CommercialFiltersForm
from .forms.UserForms.OfferResponseForm \
    import OfferResponseForm
from .forms.UserForms.ApplicationForm \
    import ApplicationForm
from .models import \
    SocialNetwork, ProductCategory, \
    Advantage, Feedback, \
    Contact, Apartment, \
    House, Land, \
    Garage, Commercial, \
    News, Partner, \
    Service, AboutCompanyBlock


def index(request):
    return render(request, 'agency/Pages/index.html', {
        'social_networks': SocialNetwork.objects.all(),
        'products_categories': ProductCategory.objects.all(),
        'advantages': Advantage.objects.all(),
        'feedbacks': Feedback.objects.all(),
        'partners': Partner.objects.all(),
        'contacts': Contact.objects.first()
    })


def services(request):
    return render(request, 'agency/Pages/services.html', {
        'social_networks': SocialNetwork.objects.all(),
        'services': Service.objects.all()
    })


def about(request):
    return render(request, 'agency/Pages/about.html', {
        'social_networks': SocialNetwork.objects.all(),
        'about_company_blocks': AboutCompanyBlock.objects.all()
    })


def contacts(request):
    return render(request, 'agency/Pages/contacts_page.html', {
        'social_networks': SocialNetwork.objects.all(),
        'contacts': Contact.objects.first()
    })


def news(request):
    return render(request, 'agency/Pages/news.html', {
        'social_networks': SocialNetwork.objects.all(),
        'news': News.objects.filter(
            status='published').order_by('-publication_date')
    })


def news_details(request, pk):
    piece_of_news = get_object_or_404(News, pk=pk)
    return render(request, 'agency/Pages/news_details.html', {
        'social_networks': SocialNetwork.objects.all(),
        'piece_of_news': piece_of_news
    })


def application(request):
    if request.method == "POST":
        application_form = ApplicationForm(request.POST)
        if application_form.is_valid():
            application_form.send_mail()
            return HttpResponseRedirect(reverse('agency:success_message'))

    application_form = ApplicationForm()
    return render(request, 'agency/Pages/application.html', {
        'application_form': application_form,
        'social_networks': SocialNetwork.objects.all(),
    })


def offer_response(request, title, vendor_code):
    if request.method == 'POST':
        offer_response_form = OfferResponseForm(request.POST)
        if offer_response_form.is_valid():
            offer_response_form.send_mail(vendor_code)
            return HttpResponseRedirect(reverse('agency:success_message'))

    offer_response_form = OfferResponseForm()
    return render(request, 'agency/Pages/offer_response.html', {
        'real_estate_title': title,
        'offer_response_form': offer_response_form,
        'social_networks': SocialNetwork.objects.all(),
    })


def advert(request):
    return render(request, 'agency/Pages/advert.html', {
        'social_networks': SocialNetwork.objects.all(),
        'contacts': Contact.objects.first()
    })


def success_message(request):
    return render(request, 'agency/Messages/success_message.html', {
        'social_networks': SocialNetwork.objects.all(),
        'products_categories': ProductCategory.objects.all()
    })


def get_real_estate_data(request, FiltersForm, RealEstateType):

    if request.method != 'POST':
        if 'real-estate-filters' in request.session:
            request.POST = request.session['real-estate-filters']
            request.method = 'POST'

    if request.method == 'POST':
        filters_form = FiltersForm(request.POST)
        request.session['real-estate-filters'] = request.POST
        if filters_form.is_valid():
            real_estate = filters_form.get_filtered()
    else:
        filters_form = FiltersForm()
        real_estate = RealEstateType.objects.filter(status='published')

    paginator = Paginator(real_estate, 2, allow_empty_first_page=True)
    page = request.GET.get('page')
    real_estate_for_page = paginator.get_page(page)

    return (real_estate, real_estate_for_page, filters_form)


def apartments(request):
    real_estate, real_estate_for_page, filters_form = get_real_estate_data(
        request, ApartmentFiltersForm, Apartment)

    return render(request, 'agency/RealEstate/apartments.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': real_estate_for_page,
        'hot_real_estate': real_estate.filter(is_hot_offer=True),
        'apartment_filters_form': filters_form,
        'details_page': 'agency:apartment_details'
    })


def apartment_details(request, pk):
    apartment = get_object_or_404(Apartment, pk=pk)
    return render(request, 'agency/RealEstate/apartment_details.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': apartment
    })


def houses(request):
    real_estate, real_estate_for_page, filters_form = get_real_estate_data(
        request, HouseFiltersForm, House)

    return render(request, 'agency/RealEstate/houses.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': real_estate_for_page,
        'hot_real_estate': real_estate.filter(is_hot_offer=True),
        'house_filters_form': filters_form,
        'details_page': 'agency:house_details'
    })


def house_details(request, pk):
    house = get_object_or_404(House, pk=pk)
    return render(request, 'agency/RealEstate/house_details.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': house
    })


def lands(request):
    real_estate, real_estate_for_page, filters_form = get_real_estate_data(
        request, LandFiltersForm, Land)

    return render(request, 'agency/RealEstate/lands.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': real_estate_for_page,
        'hot_real_estate': real_estate.filter(is_hot_offer=True),
        'land_filters_form': filters_form,
        'details_page': 'agency:land_details'
    })


def land_details(request, pk):
    land = get_object_or_404(Land, pk=pk)
    return render(request, 'agency/RealEstate/land_details.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': land
    })


def garages(request):
    real_estate, real_estate_for_page, filters_form = get_real_estate_data(
        request, GarageFiltersForm, Garage)

    return render(request, 'agency/RealEstate/garages.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': real_estate_for_page,
        'hot_real_estate': real_estate.filter(is_hot_offer=True),
        'garage_filters_form': filters_form,
        'details_page': 'agency:garage_details'
    })


def garage_details(request, pk):
    garage = get_object_or_404(Garage, pk=pk)
    return render(request, 'agency/RealEstate/garage_details.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': garage
    })


def commercial(request):
    real_estate, real_estate_for_page, filters_form = get_real_estate_data(
        request, CommercialFiltersForm, Commercial)

    return render(request, 'agency/RealEstate/commercial.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': real_estate_for_page,
        'hot_real_estate': real_estate.filter(is_hot_offer=True),
        'commercial_filters_form': filters_form,
        'details_page': 'agency:commercial_details'
    })


def commercial_details(request, pk):
    commercial = get_object_or_404(Commercial, pk=pk)
    return render(request, 'agency/RealEstate/commercial_details.html', {
        "social_networks": SocialNetwork.objects.all(),
        'real_estate': commercial
    })
