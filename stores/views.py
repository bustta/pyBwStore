from django.shortcuts import render, redirect, get_object_or_404
from .models import Store
from .model_form import StoreForm


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
