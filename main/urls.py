from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^song_add/$', song_add, name="song_add"),
    url(r'^song_added/(?P<song_id>\d+)/$', song_added, name="song_added"),

    url(r'^store/(?P<store_id>\d+)/$', store_index, name="store_index"),
    url(r'^song/delete/(?P<song_id>\d+)/$', song_delete, name='song_delete'),
    url(r'^(?P<store_id>\d+)/song/all_delete/$', song_all_delete, name='song_all_delete'),
    url(r'^song/listen/(?P<song_id>\d+)/$', song_listen, name='song_listen'),
    url(r'^song/return/(?P<song_id>\d+)/$', song_return, name='song_return'),
]