from django.shortcuts import render, get_object_or_404, redirect
from .models import Artist, Album
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import AlbumForm

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

"""
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
"""
class AlbumListView(ListView):
    model = Album
    template_name = "music_library/album_list.html"
    context_object_name = "albums"
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['albums'].count()
        return context


    def get_queryset(self):
        qs = super().get_queryset().select_related('artist')
        artist_id = self.request.GET.get("artist_id")
        if artist_id:
            qs = qs.filter(artist_id=artist_id)
        return qs

class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "music_library/album_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Album "{self.object.title}" created.')
        return response

    def get_success_url(self):
        return reverse("album_detail", kwargs={"pk": self.object.pk})

class AlbumUpdateView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "music_library/album_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Album "{self.object.title}" updated.')
        return response

    def get_success_url(self):
        return reverse("album_detail", kwargs={"pk": self.object.pk})

# Create your views here.
# def album_create(request):
#     artists = Artist.objects.all().order_by("name")
#
#     if request.method == 'POST':
#         form = AlbumForm(request.POST)
#         # title = request.POST.get("title")
#         # artist_id = request.POST.get("artist_id")
#         # release_year = request.POST.get("release_Year") or None
#         # is_concept = request.POST.get("is_Concept_Album") == "on"
#         #
#         # artist = get_object_or_404(Artist, pk = artist_id)
#         # album = Album.objects.create(
#         #     title = title,
#         #     artist = artist,
#         #     release_Year = release_year,
#         #     is_Concept_Album = is_concept,
#         # )
#         #
#         # messages.success(request, f"Album '{album.title}' created.")
#         #
#         # return redirect("album_detail", pk=album.pk)
#
#         return render(request, "music_library/album_form.html",  {"form": form})
#
#     return render(request, "music_library/album_form.html", {
#         "album": None,
#         "artists": artists
#     })
"""
def album_detail(request, pk):
    
    album = get_object_or_404(
        Album.objects.select_related('artist').prefetch_related('Tracks'),
        pk=pk
    )
    context = {
        "album": album,
        "tracks": album.Tracks.all().order_by('track_Number'),
    }
    return render(request, "music_library/album_detail.html", context)
"""

class AlbumDetailView(DetailView):
    model = Album
    template_name = "music_library/album_detail.html"
    context_object_name = "album"

    def get_queryset(self):
        return (super()
                .get_queryset()
                .select_related("artist")
                .prefetch_related("Tracks"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = context["album"]
        context["tracks"] = album.Tracks.all().order_by("track_Number")
        return context

# def album_update(request, pk):
#     """
#     Edit an existing album.
#     """
#     album = get_object_or_404(Album, pk=pk)
#
#     if request.method == "POST":
#         album.title = request.POST.get("title")
#         artist_id = request.POST.get("artist_id")
#         album.artist = get_object_or_404(Artist, pk=artist_id)
#         album.release_Year = request.POST.get("release_Year") or None
#         album.is_Concept_Album = request.POST.get("is_Concept_Album") == "on"
#         album.save()
#         messages.success(request, f'Album "{album.title}" updated.')
#         return redirect("album_detail", pk=album.pk)
#
#     # GET – show form with existing data
#     return render(request, "music_library/album_form.html", {"album": album})

# def album_delete(request, pk):
#     """
#     Delete an album, with confirmation page.
#     """
#     album = get_object_or_404(Album, pk=pk)
#
#     if request.method == "POST":
#         title = album.title
#         album.delete()
#         messages.success(request, f'Album "{title}" deleted.')
#         return redirect("album_list")
#
#     # GET – show confirmation
#     return render(request, "music_library/album_confirm_delete.html", {"album": album})

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = "music_library/album_confirm_delete.html"
    success_url = reverse_lazy("album_list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        title = self.object.title
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'Album "{title}" deleted.')
        return response

# def artist_list(request):
#     """List all artists."""
#
#     artists = Artist.objects.prefetch_related('genre').all().order_by('name')
#     return render(request, "music_library/artist_list.html", {"artists": artists})
#
#
# def artist_detail(request, pk):
#     """Show one artist, their genres, and all their albums."""
#
#     artist = get_object_or_404(
#         Artist.objects.prefetch_related('genre', 'Albums'),
#         pk=pk
#     )
#
#     albums = artist.Albums.all()
#
#     context = {
#         "artist": artist,
#         "albums": albums,
#     }
#
#     return render(request, "music_library/artist_detail.html", context)

class ArtistListView(ListView):
    model = Artist
    template_name = "music_library/artist_list.html"
    context_object_name = "artists"
    ordering = ['name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = context['artists'].count()
        return context

    def get_queryset(self):
        return super().get_queryset().prefetch_related('genre')

class ArtistDetailView(DetailView):
    model = Artist
    template_name = "music_library/artist_detail.html"
    context_object_name = "artist"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('genre', 'Albums')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = self.object.Albums.all()
        return context

# class ArtistCreateView(CreateView):
#     model = Artist
#     form_class = ArtistForm
#     template_name = "music_library/artist_form.html"
#
#     def get_success_url(self):
#         return reverse(viewname="artist_detail", kwargs={"pk": self.object.pk})
#
#
# class ArtistUpdateView(UpdateView):
#     model = Artist
#     form_class = ArtistForm
#     template_name = "music_library/artist_form.html"
#
#     def get_success_url(self):
#         return reverse(viewname="artist_detail", kwargs={"pk": self.object.pk})