from django.shortcuts import render, redirect
from .models import Store
from django.forms.models import modelform_factory


def store_list(request):
    stores = Store.objects.all()
    return render(request, 'stores.html', {'stores': stores})


def store_create(request):
    StoreForm = modelform_factory(Store, exclude=())
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect(store.get_absolute_url())

    form = StoreForm()
    return render(request, 'store_create.html', {'form': form})