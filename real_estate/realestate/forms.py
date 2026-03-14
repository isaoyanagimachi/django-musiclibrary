from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            "title",
            "description",
            "property_type",
            "status",
            "price",
            "city",
            "area_name",
            "bedrooms",
            "bathrooms",
            "carpet_area_sqft",
            "main_image",
            "floorplan_file",
            "is_published",
        ]