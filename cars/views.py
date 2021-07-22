from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car


# Create your views here.
def cars(request):
    car = Car.objects.order_by('-created_date')
    paginator = Paginator(car, 3)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('car_model', flat=True).distinct()  # to get more precise search results
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    bodystyle_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()
    data = {'car': paged_cars, 'model_search': model_search, 'city_search': city_search, 'year_search': year_search,
            'bodystyle_search': bodystyle_search, 'transmission_search': transmission_search}
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    data = {'single_car': single_car, }
    return render(request, 'cars/car_detail.html', data)


def search(request):
    car = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('car_model', flat=True).distinct()  # to get more precise search results
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    bodystyle_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            car = car.filter(description__icontains=keyword)

    if 'car_model' in request.GET:
        car_model = request.GET['car_model']
        if car_model:
            car = car.filter(car_model__iexact=car_model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            car = car.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            car = car.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            car = car.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            car = car.filter(transmission__iexact=transmission)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            car = car.filter(price__gte=min_price, price__lte=max_price)

    data = {'car': car, 'model_search': model_search, 'city_search': city_search, 'year_search': year_search,
            'bodystyle_search': bodystyle_search, 'transmission_search': transmission_search}
    return render(request, 'cars/search.html', data)


