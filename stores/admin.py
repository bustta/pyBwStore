from django.contrib import admin
from .models import Store


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

admin.site.register(Store, StoreAdmin)
