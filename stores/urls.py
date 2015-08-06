from django.conf.urls import patterns, url
from .views import store_list


urlpatterns = patterns(
    '',
    url(r'^stores/$', store_list, name='store_list'),
)