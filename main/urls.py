from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^song_write/$', song_write, name="song_write"),
    url(r'^song_add/$', song_add, name="song_add"),
    url(r'^song_added/(?P<song_id>\d+)/$', song_added, name="song_added"),
]