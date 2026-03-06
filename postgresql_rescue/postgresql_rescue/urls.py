"""
URL configuration for postgresql_rescue project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from core.views import home, about, album_detail, contact, roadmap, greet
from music_library import views as ml_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('album/', album_detail, name='album_detail'),
    #path('albums/', ml_views.album_list, name='album_list'),
    path('albums/', ml_views.AlbumListView.as_view(), name='album_list'),
    path('albums/<int:pk>/', ml_views.AlbumDetailView.as_view(), name='album_detail'),
   # path('albums/create/', ml_views.album_create, name='album_create'),
    #path('albums/<int:pk>/', ml_views.album_detail, name='album_detail'),
    #path('albums/<int:pk>/edit/', ml_views.album_update, name='album_update'),
    #path('albums/<int:pk>/delete/', ml_views.album_delete, name='album_delete'),
    path("albums/<int:pk>/delete/", ml_views.AlbumDeleteView.as_view(), name="album_delete"),
    #path('artists/', ml_views.artist_list, name='artist_list'),
    #path('artists/<int:pk>/', ml_views.artist_detail, name='artist_detail'),
    path('contact/', contact, name='contact'),
    path('roadmap/', roadmap, name='roadmap'),
    path('greet/<str:name>', greet, name='greet'),
	path('albums/create/', ml_views.AlbumCreateView.as_view(), name='album_create'),
    path('albums/<int:pk>/edit/', ml_views.AlbumUpdateView.as_view(), name='album_update'),
    path('artists/', ml_views.ArtistListView.as_view(), name='artist_list'),
    path('artists/<int:pk>/', ml_views.ArtistDetailView.as_view(), name='artist_detail'),
]
