from django.shortcuts import render, redirect, get_object_or_404
from .models import Store, Area, City
from .model_form import StoreForm
from django_ajax.decorators import ajax
import json
import googlemaps
import os
from django.core import serializers


def get_full_address(city, area, address):
    mytuple = (city, area, address)
    return ''.join(mytuple)


def get_geocode(form):
    gmaps = googlemaps.Client(key=os.environ['GOOGLE_KEY'])

    area = Area.objects.get(pk=form.data['area'])
    full_address = get_full_address(area.city.name_in_cht, area.name, form.data['address'])
    geocode = gmaps.geocode(full_address)
    geo_dict = {'lat': geocode[0]['geometry']['location']['lat'],
                'lng': geocode[0]['geometry']['location']['lng']}
    return geo_dict


def set_store_lag_and_lng(form):
    geo_dict = get_geocode(form)
    setattr(form.instance, 'lat', geo_dict['lat'])
    setattr(form.instance, 'lng', geo_dict['lng'])
    return form


def store_list(request):
    stores = Store.objects.all()
    for store in stores:
        store.full_address = get_full_address(
            store.city.name_in_cht, store.area.name, store.address)

    return render(request, 'stores.html', {'stores': stores})


def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        form = set_store_lag_and_lng(form)

        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())

    form = StoreForm()
    return render(request, 'store_create.html', {'form': form})


def store_detail(request, pk):
    store = get_object_or_404(Store, pk=pk)
    return render(request, 'store_detail.html', {'store': store})


def store_update(request, pk):
    store = get_object_or_404(Store, pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        form = set_store_lag_and_lng(form)

        if form.is_valid():
            form.save()
            return redirect('store_list')

    return render(request, 'store_update.html', {'store': store})


def store_delete(request, pk):
    store = get_object_or_404(Store, pk=pk)
    store.delete()
    return redirect('store_list')


@ajax
def get_area_by_city(request, city):
    areas = Area.objects.filter(city__name=city)
    result = {}
    for area in areas:
        result[area.id] = area.name
    res = json.dumps(result, ensure_ascii=False)
    return res


@ajax
def get_stores(request):
    stores = Store.objects.all()
    res = serializers.serialize('json', stores, ensure_ascii=False)
    return res


@ajax
def get_stores_by_city(request, pk):
    stores = Store.objects.filter(city__id=pk)
    res = serializers.serialize('json', stores, ensure_ascii=False)
    return res


@ajax
def get_city(request, pk):
    city = City.objects.get(pk=pk)
    res = serializers.serialize('json', [city, ], ensure_ascii=False)
    return res

