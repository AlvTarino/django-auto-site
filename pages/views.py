from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from cars.models import Car


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    cars_for_rent = Car.objects.order_by('-created_date').filter(for_rent=True)
    all_cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('car_model', 'city', 'year', 'body_style')
    model_search = Car.objects.values_list('car_model', flat=True).distinct()  # to get more precise search results
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    bodystyle_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    data = {'teams': teams, 'featured_cars': featured_cars, 'all_cars': all_cars, 'cars_for_rent': cars_for_rent,
            'model_search': model_search, 'city_search': city_search, 'year_search': year_search,
            'bodystyle_search': bodystyle_search, 'transmission_search': transmission_search}
    return render(request, 'pages/home.html', data)


def about(request):
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
