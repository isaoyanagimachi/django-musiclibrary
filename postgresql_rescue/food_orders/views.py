
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Category, MenuItem, Order, OrderItem
from .forms import OrderForm, OrderItemForm, MenuItemSimpleForm, CategoryForm
from django.forms import formset_factory


def menu_home(request):
    """
    Display menu categories and items.
    """
    categories = Category.objects.prefetch_related("items").all()

    context = {
        "categories": categories,
    }
    return render(request, "food_orders/menu_home.html", context)
# Create your views here.

def order_create(request):
    """
    Create an order with one or more items (simple formset).
    """
    OrderItemFormSet = formset_factory(OrderItemForm, extra=2, max_num=5)

    if request.method == "POST":
        order_form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST)

        if order_form.is_valid() and formset.is_valid():
            order = order_form.save()
            items_created = 0
            for form in formset:
                menu_item = form.cleaned_data.get("menu_item")
                quantity = form.cleaned_data.get("quantity")
                if menu_item and quantity:
                    OrderItem.objects.create(
                        order=order, menu_item=menu_item, quantity=quantity
                    )
                    items_created += 1
            if items_created == 0:
                order.delete()
                messages.error(request, "Please add at least one menu item.")
            else:
                messages.success(
                    request,
                    f"Order #{order.id} placed for {order.customer.name}! ",
                )
                return redirect("order_detail", pk=order.pk)
    else:
        order_form = OrderForm()
        formset = OrderItemFormSet()

    context = {
        "order_form": order_form,
        "formset": formset,
    }
    return render(request, "food_orders/order_form.html", context)

def order_list(request):
    orders = Order.objects.order_by("-created_at")
    return render(request, "food_orders/order_list.html", {"orders": orders})


def order_detail(request, pk):
    order = get_object_or_404(Order.objects.prefetch_related("items__menu_item"), pk=pk)
    return render(request, "food_orders/order_detail.html", {"order": order})


def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category created.")
            return redirect("food_home")
    else:
        form = CategoryForm()
    return render(request, "food_orders/category_form.html", {"form": form})


def menuitem_create(request):
    if request.method == "POST":
        form = MenuItemSimpleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item created.")
            return redirect("food_home")
    else:
        form = MenuItemSimpleForm()
    return render(request, "food_orders/menuitem_form.html", {"form": form})
