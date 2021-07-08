from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


# Create your models here.
class Car(models.Model):
    cityChoices = (('KLA', 'Kampala'), ('EBB', 'Entebbe'), ('MSK', 'Masaka'), ('MBR', 'Mbarara'), ('GLU', 'Gulu'),
                   ('MBL', 'Mbale'), ('JNJ', 'Jinja'), ('SRT', 'Soroti'))

    features_choices = (('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'),
                        ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('LED lights', 'LED lights'),
                        ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('BullBar', 'BullBar'),
                        ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'),
                        ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'),
                        ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'),
                        ('Bluetooth Handset', 'Bluetooth Handset'), ('Leather seats', 'Leather seats'),
                        ('Keyless entry', 'Keyless entry'), )

    bodyStyleChoices = (('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Sports Car', 'Sports Car'),
                        ('Station Wagon', 'Station Wagon'), ('Hatch Back', 'Hatch Back'), ('Convertible', 'Convertible'),
                        ('SUV', 'SUV'), ('MiniVan', 'MiniVan'), ('Pickup Truck', 'Pickup Truck'),)

    condition_choices = (('Firsthand', 'Firsthand'), ('Second Hand', 'Second Hand'),
                         ('Locally used', 'Locally used'), )

    transmission_choices = (('MT', 'Manual transmission'), ('AT', 'Automatic Transmission'),
                            ('AM', 'Automated Manual Transmission'), ('CVT', 'Continuosly Variable Transmission'),)

    fuelType_choices = (('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric'))

    door_choices = (('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),)

    year_choice = []
    for r in range(1990, (datetime.now().year + 1)):
        year_choice.append((r, r))

    car_name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    car_colour = models.CharField(max_length=100)
    transmission = models.CharField(choices=transmission_choices, max_length=100)
    fuel_Type = models.CharField(choices=fuelType_choices, max_length=50)
    year = models.IntegerField('year', choices=year_choice)
    body_style = models.CharField(choices=bodyStyleChoices, max_length=100)
    features = MultiSelectField(choices=features_choices)
    condition = models.CharField(choices=condition_choices, max_length=100)
    city = models.CharField(choices=cityChoices, max_length=100)
    doors = models.CharField(choices=door_choices, max_length=100)
    passengers = models.IntegerField()
    car_photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/')
    car_photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/')
    engine_capacity = models.CharField(max_length=100)
    VIN = models.CharField(max_length=100, blank=True)
    mileage = models.IntegerField()
    price = models.IntegerField()
    negotiable = models.BooleanField(default=False)
    description = RichTextField()
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_name

