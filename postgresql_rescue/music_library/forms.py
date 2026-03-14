from django import forms
from .models import Album

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        # Adjust these field names to match your actual Album model
        fields = ["title", "artist", "release_Year", "is_Concept_Album"]

        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Album title"}
            ),
            "artist": forms.Select(attrs={"class": "form-control"}),
            "release_Year": forms.NumberInput(
                attrs={"class": "form-control", "min": 1900, "max": 2100}
            ),
            "is_Concept_Album": forms.CheckboxInput(
                attrs={"class": "form-control"}
            ),

        }
        help_texts = {
            "release_Year": "Enter a 4‑digit year between 1900 and 2100."
        }

    def clean_release_Year(self):
        year = self.cleaned_data["release_Year"]
        if year < 1900 or year > 2100:
            raise forms.ValidationError("Release year must be between 1900 and 2100.")
        return year