from django.shortcuts import render, redirect
from .models import *
from django.db import IntegrityError

def song_add(request):
    if request.method == 'GET':
        return render(request, 'song/song_write.html')
    else:
        title = request.POST.get('title')
        singer = request.POST.get('singer')
        message = request.POST.get('message')
        store_id = int(request.POST.get('store'))
        new_song = song.objects.create(title=title, singer=singer, message=message, store_id=store_id)
        return redirect("main:song_added", song_id=new_song.pk)

def song_added(request, song_id):
    context = {'song' : song.objects.get(pk=song_id)}
    return render(request, 'song/song_add.html', context)

def store_index(request, store_id):
    context = {'song' : store.objects.get(pk=store_id).song_set.all, 'store_id' : store_id }
    return render(request, 'song/store_index.html', context)

def song_delete(request, song_id):
    context = song.objects.get(pk=song_id)
    context.delete()
    store_id = context.store.id
    return redirect('main:store_index', store_id=store_id)

def song_all_delete(request, store_id):
    store.objects.get(pk=store_id).song_set.all().delete()
    return redirect('main:store_index', store_id=store_id)