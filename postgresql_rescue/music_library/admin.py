from django.contrib import admin
from .models import Artist, Album, Track, Genre


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name','country', 'genre')
    search_fields = ('name','genre', 'country')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','artist', 'release_Year', 'is_Concept_Album')
    list_filter = ('title', 'release_Year', 'is_Concept_Album')
    search_fields = ('title', 'artist__name')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'track_Number', 'duration_Seconds')
    list_filter = ('album__title','title')
    search_fields = ('title', 'album__title')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_artists_names')
    search_fields = ('name',)

    def get_artists_names(self, obj):
        return ", ".join([g.name for g in obj.artists.all()])



# Register your models here.
