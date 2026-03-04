from django.db import models
class Artist(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='Albums')
    title = models.CharField(max_length=100)
    release_Year = models.PositiveIntegerField(blank=True, null=True)
    is_Concept_Album = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.artist.name})"

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='Tracks')
    title = models.CharField(max_length=100)
    duration_Seconds = models.PositiveIntegerField(blank=True, null=True)
    track_Number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.track_Number}.{self.title}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    artists = models.ManyToManyField(Artist, related_name='Genre')

    def __str__(self):
        return f"{self.name}"


# Create your models here.
