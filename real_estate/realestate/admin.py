from django.contrib import admin
from .models import Property, Inquiry

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "status", "price", "is_published", "created_at")
    list_filter = ("status", "city", "property_type", "is_published")
    search_fields = ("title", "city", "area_name")
    prepopulated_fields = {"slug": ("title",)}

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("property", "name", "email", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "property__title")