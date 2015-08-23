from django.contrib import admin
from .models import Store, Category, City, Area


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'city',
        'area',
        'address',
        'telephone',
        'website',
        'lat',
        'lng'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_in_cht', 'lat', 'lng')


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'lat', 'lng')


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)

