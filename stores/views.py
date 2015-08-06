from django.shortcuts import render


def store_list(request):
    return render(request, 'stores.html')
