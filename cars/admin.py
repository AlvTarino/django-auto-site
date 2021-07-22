from django.contrib import admin
from django.utils.html import format_html
from .models import Car


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src = "{}" width ="40" style = "border-radius:50px;"/>'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Photo'

    list_display = ('id', 'thumbnail', 'car_name', 'car_model', 'transmission', 'fuel_Type', 'year',
                    'condition', 'city', 'engine_capacity', 'price', 'negotiable', 'is_featured', 'for_rent')
    list_display_links = ('id', 'thumbnail', 'car_name', 'car_model', 'year', 'condition', 'city', 'price',)
    list_editable = ('negotiable', 'is_featured', 'for_rent')
    search_fields = ('id', 'car_name', 'car_model', 'transmission', 'fuel_Type', 'year', 'condition',
                     'city', 'engine_capacity', 'price', 'negotiable', 'is_featured', 'for_rent')
    list_filter = ('id', 'car_model', 'transmission', 'fuel_Type', 'year', 'condition', 'city',
                   'engine_capacity', 'price', 'negotiable', 'is_featured', 'for_rent')


admin.site.register(Car, CarAdmin)

