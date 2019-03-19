from django.urls import path
from . import views

app_name = 'agency'
urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('news/', views.news, name='news'),
    path('<int:pk>news_details/', views.news_details, name='news_details'),
    path('application/', views.application, name='application'),
    path('advert/', views.advert, name='advert'),
    path('<str:title>/<str:vendor_code>/offer_response/',
         views.offer_response, name='offer_response'),
    path('success_message/', views.success_message,
         name='success_message'),
    path('apartments/', views.apartments, name='apartments'),
    path('houses/', views.houses, name='houses'),
    path('lands/', views.lands, name='lands'),
    path('garages/', views.garages, name='garages'),
    path('commercial/', views.commercial, name='commercial'),
    path('<int:pk>apartment_details/',
         views.apartment_details, name='apartment_details'),
    path('<int:pk>house_details/',
         views.house_details, name='house_details'),
    path('<int:pk>land_details/',
         views.land_details, name='land_details'),
    path('<int:pk>garage_details/',
         views.garage_details, name='garage_details'),
    path('<int:pk>commercial_details/',
         views.commercial_details, name='commercial_details'),
]
