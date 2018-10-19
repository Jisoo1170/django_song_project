from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.db import IntegrityError


def song_write(request):
    if request.method == 'GET':
        return render(request, 'song/song_write.html')
    # else:
    #     # title = request.POST.get('title')
    #     # singer = request.POST.get('singer')
    #     # message = request.POST.get('message')
    #     # store = request.POST.get('store')
    #     # result = song.objects.create(title=title, singer=singer, message=message, store_id=int(store))

    #     # request.session['temp_data'] = form.cleaned_data
    #     # web_input = {'title': title, 'singer': singer, 'store': store}

    #     # return render(request, 'greetings/greetings.html', web_input)
    #     # return redirect('/song_add', web_input)
    #     # return render(request, song_add, web_input)
    #     return render(request, 'song/song_write.html')

def song_add(request):
    if request.method == 'GET':
        return render(request, 'song/song_write.html')
    else:
        title = request.POST.get('title')
        singer = request.POST.get('singer')
        message = request.POST.get('message')
        store_id = int(request.POST.get('store'))
        song.objects.create(title=title, singer=singer, message=message, store_id=store_id)
        
        delay_time = store.objects.get(pk=store_id).delay

        context = {"title": title, "singer": singer, "delay_time": delay_time}
        return render(request, 'song/song_add.html', context)