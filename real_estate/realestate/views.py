from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Property, Inquiry
from .forms import PropertyForm

class PropertyListView(ListView):
    model = Property
    template_name = "realestate/property_list.html"
    context_object_name = "properties"
    paginate_by = 9

    def get_queryset(self):
        qs = Property.objects.filter(is_published=True)
        city = self.request.GET.get("city")
        status = self.request.GET.get("status")
        ptype = self.request.GET.get("type")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if city:
            qs = qs.filter(city__icontains=city)
        if status:
            qs = qs.filter(status=status)
        if ptype:
            qs = qs.filter(property_type=ptype)
        if min_price:
            qs = qs.filter(price__gte=min_price)
        if max_price:
            qs = qs.filter(price__lte=max_price)
        return qs
class PropertyDetailView(DetailView):
    model = Property
    template_name = "realestate/property_detail.html"
    context_object_name = "property"


def property_inquiry(request, slug):
    prop = get_object_or_404(Property, slug=slug, is_published=True)
    if request.method == "POST":
        Inquiry.objects.create(
            property=prop,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            message=request.POST.get("message", ""),
        )
        messages.success(request, "Thank you! The agent will contact you soon.")
        return redirect("property_detail", slug=prop.slug)
    return redirect("property_detail", slug=prop.slug)
@login_required
def property_create(request):
    if request.method == "POST":
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(commit=False)
            prop.agent = request.user
            prop.save()
            messages.success(request, "Property created successfully.")
            return redirect("property_detail", slug=prop.slug)
    else:
        form = PropertyForm()
    return render(request, "realestate/property_form.html", {"form": form})
