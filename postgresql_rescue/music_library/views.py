from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Album
from django.contrib import messages

# def album_list(request):
#     # Displays list of all albums
#
#     albums = Album.objects.select_related("artist").all().order_by("title")
#
#     context = {
#         "albums": albums,
#         "total": albums.count(),
#     }
#
#     return render(request, "music_library/album_list.html", context)


def album_list(request):

    artist_id = request.GET.get("artist_id")

    albums = Album.objects.select_related("artist").all().order_by("title")

    selected_artist = None
    if artist_id:
        albums = albums.filter(artist_id=artist_id)
        selected_artist = get_object_or_404(Artist, pk=artist_id)

    context = {
        "albums": albums,
        "selected_artist": selected_artist,
    }

    return render(request, "music_library/album_list.html", context)

# Create your views here.
def album_create(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        artist_id = request.POST.get("artist_id")
        release_year = request.POST.get("release_Year") or None
        is_concept = request.POST.get("is_Concept_Album") == "on"

        artist = get_object_or_404(Artist, pk = artist_id)
        album = Album.objects.create(
            title = title,
            artist = artist,
            release_Year = release_year,
            is_Concept_Album = is_concept,
        )

        messages.success(request, f"Album '{album.title}' created.")

        return redirect("album_detail", pk=album.pk)

    return render(request, "music_library/album_form.html", {"album" : None})

def album_detail(request, pk):
    """
    Show one album and its tracks.
    """
    album = get_object_or_404(
        Album.objects.select_related('artist').prefetch_related('Tracks'),
        pk=pk
    )
    context = {
        "album": album,
        "tracks": album.Tracks.all().order_by('track_Number'),
    }
    return render(request, "music_library/album_detail.html", context)

def album_update(request, pk):
    """
    Edit an existing album.
    """
    album = get_object_or_404(Album, pk=pk)

    if request.method == "POST":
        album.title = request.POST.get("title")
        artist_id = request.POST.get("artist_id")
        album.artist = get_object_or_404(Artist, pk=artist_id)
        album.release_Year = request.POST.get("release_Year") or None
        album.is_Concept_Album = request.POST.get("is_Concept_Album") == "on"
        album.save()
        messages.success(request, f'Album "{album.title}" updated.')
        return redirect("album_detail", pk=album.pk)

    # GET – show form with existing data
    return render(request, "music_library/album_form.html", {"album": album})

def album_delete(request, pk):
    """
    Delete an album, with confirmation page.
    """
    album = get_object_or_404(Album, pk=pk)

    if request.method == "POST":
        title = album.title
        album.delete()
        messages.success(request, f'Album "{title}" deleted.')
        return redirect("album_list")

    # GET – show confirmation
    return render(request, "music_library/album_confirm_delete.html", {"album": album})


def artist_list(request):
    """List all artists."""

    artists = Artist.objects.prefetch_related('genre').all().order_by('name')
    return render(request, "music_library/artist_list.html", {"artists": artists})


def artist_detail(request, pk):
    """Show one artist, their genres, and all their albums."""

    artist = get_object_or_404(
        Artist.objects.prefetch_related('genre', 'Albums'),
        pk=pk
    )

    albums = artist.Albums.all()

    context = {
        "artist": artist,
        "albums": albums,
    }

    return render(request, "music_library/artist_detail.html", context)