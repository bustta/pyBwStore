from django.shortcuts import render, redirect, get_object_or_404
from .models import Store, Area, City
from .model_form import StoreForm
from django_ajax.decorators import ajax
import json


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores.html', {'stores': stores})


def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
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
    result = []
    for area in areas:
        result.append(area.name)
    res = json.dumps(result,  ensure_ascii=False)
    return res

