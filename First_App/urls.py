from django.conf.urls import url
from django.urls import path
from First_App import views

app_name = "First_App"
urlpatterns =[
    path('',views.index,name='index'),
    path('Add_musician/',views.musician_form,name='musician_form'),
    path('Add_Album/',views.Album_form,name='Album_form'),
    path('album_list/<int:artist_id>/',views.Album_list,name='Album_list'),
    path('edit_artist/<int:artist_id>/',views.edit_artist,name='edit_artist'),
    path('edit_album/<int:album_id>/',views.edit_album,name='edit_album'),
    path('delete_album/<int:album_id>/',views.delete_album,name='delete_album'),
    path('delete_artist/<int:artist_id>/',views.delete_artist,name='delete_artist'),

]
