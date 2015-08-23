from django.conf.urls import patterns, url
from .views import store_list, store_create, store_detail, store_update, store_delete
from .views import get_area_by_city, get_stores, get_city, get_stores_by_city

urlpatterns = patterns(
    '',
    url(r'^$', store_list, name='index'),
    url(r'^stores/$', store_list, name='store_list'),
    url(r'^store/$', store_create, name='store_create'),
    url(r'^stores/(?P<pk>\d+)/$', store_detail, name='store_detail'),
    url(r'^stores/(?P<pk>\d+)/update$', store_update, name='store_update'),
    url(r'^stores/(?P<pk>\d+)/delete$', store_delete, name='store_delete'),

    url(r'^api/area/(?P<city>\w+)/$', get_area_by_city, name='get_area_by_city'),
    url(r'^api/stores/$', get_stores, name='get_stores'),
    url(r'^api/city/(?P<pk>\d+)$', get_city, name='get_city'),
    url(r'^api/stores/(?P<pk>\d+)$', get_stores_by_city, name='get_stores_by_city'),

)