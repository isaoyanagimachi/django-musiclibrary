from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Order, OrderItem, Category, MenuItem


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["customer_name", "customer_phone"]
        widgets = {
            "customer_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Your name"}
            ),
            "customer_phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Phone number"}
            ),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["menu_item", "quantity"]
        widgets = {
            "menu_item": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(
                attrs={"class": "form-control", "min": 1}
            ),
        }
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

class MenuItemSimpleForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ["category", "name", "description", "price", "is_available"]
