from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ["title", "artist", "release_Year", "is_Concept_Album"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "artist": forms.Select(attrs={"class": "form-control"}),
            "release_Year": forms.NumberInput(attrs={"class": "form-control"}),
            "is_Concept_Album": forms.CheckboxInput(),
        }