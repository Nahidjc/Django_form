from django.shortcuts import render
from django.http import HttpResponse
from First_App import views
from First_App.models import Musician,Album
from First_App import forms
from django.db.models import Avg

def index(request):
    musician_list = Musician.objects.order_by("id")
    diction = {'title':'Home Page','musician_list':musician_list}
    return render(request,'First_App/index.html',context=diction)

def musician_form(request):
    form = forms.Musicianform()

    if request.method == "POST":
        form = forms.Musicianform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)


    diction = {'title':'Form of Musician','musician_form':form}
    return render(request,'First_App/musician_form.html',context=diction)
def Album_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_list = Album.objects.filter(Artist=artist_id).order_by("num_stars")
    artist_rating = Album.objects.filter(Artist = artist_id).aggregate(Avg('num_stars'))
    diction = {'title':'List of Album','artist_info':artist_info,'album_list':album_list,'artist_rating':artist_rating}
    diction.update({'artist_id':artist_id})

    return render(request,'First_App/album_list.html',context=diction)


def Album_form(request):
    form = forms.AlbumForm()

    if request.method == "POST":
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title':'Add Album','album_form':form}
    return render(request,'First_App/album_form.html',context=diction)
def edit_artist(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    form = forms.Musicianform(instance=artist_info)

    if request.method == "POST":
        form = forms.Musicianform(request.POST,instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return Album_list(request,artist_id)
    diction ={'edit_artist':form}
    return render(request,"First_App/edit_artist.html",context=diction)
def delete_artist(request,artist_id):
    musician = Musician.objects.get(pk=artist_id).delete()
    diction = {'delete_success':'This Musician Successfully Deleted!'}
    return render(request,'First_App/delete.html',context=diction)
def edit_album(request,album_id):
    album_info = Album.objects.get(pk=album_id)
    form = forms.AlbumForm(instance=album_info)
    diction ={}
    if request.method == "POST":
        form = forms.AlbumForm(request.POST,instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            diction.update({'success_update':'Successfully Updated!'})

    diction.update({'edit_form':form})
    diction.update({'album_id':album_id})
    return render(request,"First_App/edit_album.html",context=diction)
def delete_album(request,album_id):
    album = Album.objects.get(pk=album_id).delete()
    diction = {'delete_success':'This Album Successfully Deleted!'}
    return render(request,'First_App/delete.html',context=diction)
