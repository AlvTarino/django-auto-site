# Generated by Django 3.1.7 on 2021-07-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20210709_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_photo_4',
            field=models.ImageField(blank=True, upload_to='photos/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(choices=[('Kampala', 'Kampala'), ('Entebbe', 'Entebbe'), ('Masaka', 'Masaka'), ('Mbarara', 'Mbarara'), ('Gulu', 'Gulu'), ('Mbale', 'Mbale'), ('Jinja', 'Jinja'), ('Soroti', 'Soroti')], max_length=100),
        ),
    ]