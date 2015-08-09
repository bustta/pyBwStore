from django.contrib import admin
from .models import Store, Category, City, Area


class StoreAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'city',
        'area',
        'address',
        'post_code',
        'telephone',
        'website'
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'sub_category')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'post_code_in_3')


class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')


admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Area, AreaAdmin)

