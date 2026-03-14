from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ["category__name", "name"]

    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id} for {self.customer_name}"

    @property
    def total_amount(self):
        return sum(item.subtotal for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="items"
    )
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ("order", "menu_item")

    @property
    def subtotal(self):
        return self.menu_item.price * self.quantity