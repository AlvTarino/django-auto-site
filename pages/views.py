from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        # we make a structure of the email and message bodies
        email_subject = 'You have a new message from Django Cars regarding '+subject
        message_body = 'Name ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: '+message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(email_subject, message_body, 'chieftester90@gmail.com', [admin_email], fail_silently=False,)
        messages.success(request, 'Thank you for contacting Django Cars. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')
