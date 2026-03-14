from django.db import models

from django.contrib.auth.models import User
from django.utils.text import slugify

class Property(models.Model):
    PROPERTY_TYPES = [
        ("apartment", "Apartment"),
        ("villa", "Villa"),
        ("plot", "Plot / Land"),
        ("office", "Office"),
    ]
    STATUS_CHOICES = [
        ("sale", "For Sale"),
        ("rent", "For Rent"),
    ]
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()

    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    price = models.DecimalField(max_digits=12, decimal_places=2)
    city = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100, blank=True)

    bedrooms = models.PositiveIntegerField(default=1)
    bathrooms = models.PositiveIntegerField(default=1)
    carpet_area_sqft = models.PositiveIntegerField()

    main_image = models.ImageField(upload_to="properties/main/")
    floorplan_file = models.FileField(
        upload_to="properties/floorplans/",
        blank=True,
        null=True,
        help_text="Optional 2D floor plan image or PDF",
    )
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inquiries")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.property.title} by {self.name}"