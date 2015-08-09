from django.conf.urls import patterns, url
from .views import store_list, store_create, store_detail, store_update, store_delete


urlpatterns = patterns(
    '',
    url(r'^$', store_list, name='index'),
    url(r'^stores/$', store_list, name='store_list'),
    url(r'^store/$', store_create, name='store_create'),
    url(r'^stores/(?P<pk>\d+)/$', store_detail, name='store_detail'),
    url(r'^stores/(?P<pk>\d+)/update$', store_update, name='store_update'),
    url(r'^stores/(?P<pk>\d+)/delete$', store_delete, name='store_delete'),

)