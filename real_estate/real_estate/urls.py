"""
URL configuration for real_estate project.

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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from realestate import views as re_views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Auth
    path("login/", auth_views.LoginView.as_view(
        template_name="realestate/login.html"
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Property views
    path("", re_views.PropertyListView.as_view(), name="property_list"),
    path("properties/new/", re_views.property_create, name="property_create"),
    path("properties/<slug:slug>/", re_views.PropertyDetailView.as_view(),
         name="property_detail"),
    path("properties/<slug:slug>/inquire/", re_views.property_inquiry,
         name="property_inquiry"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)