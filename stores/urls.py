from django.conf.urls import patterns, url
from .views import store_list, store_create


urlpatterns = patterns(
    '',
    url(r'^stores/$', store_list, name='store_list'),
    url(r'^store/$', store_create, name='store_create'),
)