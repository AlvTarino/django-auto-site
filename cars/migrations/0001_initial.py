# Generated by Django 3.1.7 on 2021-07-05 23:26

import ckeditor.fields
import datetime
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_model', models.CharField(max_length=100)),
                ('car_colour', models.CharField(max_length=100)),
                ('transmission', models.CharField(choices=[('MT', 'Manual transmission'), ('AT', 'Automatic Transmission'), ('AM', 'Automated Manual Transmission'), ('CVT', 'Continuosly Variable Transmission')], max_length=100)),
                ('fuelType', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], max_length=50)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021)], verbose_name=('year',))),
                ('body_style', models.CharField(choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('Sports Car', 'Sports Car'), ('Station Wagon', 'Station Wagon'), ('Hatch Back', 'Hatch Back'), ('Convertible', 'Convertible'), ('SUV', 'SUV'), ('MiniVan', 'MiniVan'), ('Pickup Truck', 'Pickup Truck')], max_length=100)),
                ('features', multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('LED lights', 'LED lights'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('BullBar', 'BullBar'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Leather seats', 'Leather seats'), ('Keyless entry', 'Keyless entry')], max_length=242)),
                ('condition', models.CharField(choices=[('Firsthand', 'Firsthand'), ('Second Hand', 'Second Hand'), ('Locally used', 'Locally used')], max_length=100)),
                ('city', models.CharField(choices=[('KLA', 'Kampala'), ('EBB', 'Entebbe'), ('MSK', 'Masaka'), ('MBR', 'Mbarara'), ('GLU', 'Gulu'), ('MBL', 'Mbale'), ('JNJ', 'Jinja'), ('SRT', 'Soroti')], max_length=100)),
                ('car_photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('car_photo_1', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('car_photo_2', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('car_photo_3', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('car_photo_4', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('engine', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=100)),
                ('passengers', models.IntegerField()),
                ('VIN', models.CharField(blank=True, max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]