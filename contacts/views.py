from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


# Create your views here.
def inquiry(request):
   # capturing data from inquiry form
   if request.method == 'POST':
      car_id = request.POST['car_id']
      car_name = request.POST['car_name']
      user_id = request.POST['user_id']
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      customer_need = request.POST['customer_need']
      city = request.POST['city']
      email = request.POST['email']
      phone = request.POST['phone']
      message = request.POST['message']

      # to check if a user has already made an inquiry
      if request.user.is_authenticated:
         user_id = request.user.id
         has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
         if has_contacted:
            messages.error(request, 'You have already made an inquiry about this vehicle. '
                                    'We shall get back to you shortly')
            return redirect('/cars/' + car_id)

      contact = Contact(car_id=car_id, car_name=car_name, user_id=user_id, firstname=firstname, lastname=lastname,
                        customer_need=customer_need, city=city, email=email, phone=phone, message=message)

      admin_info = User.objects.get(is_superuser=True)  # to grab information of the admin like email, username etc
      admin_email = admin_info.email
      send_mail('Your car inquiry', 'You have a new inquiry for a car' + car_name +
                '. Please login into your admin panel for more detailed information',
                'cheiftester90@gmail.com', [admin_email], fail_silently=False)

      contact.save()
      messages.success(request, 'Your message has been received, we will get back to you shortly')
      return redirect('/cars/' + car_id)
