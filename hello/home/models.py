import uuid
from django.db import models


class IceCream(models.Model):
    """A flavor on the menu."""
    name = models.CharField(max_length=80, unique=True)
    flavor = models.CharField(max_length=80, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.flavor})" if self.flavor else self.name


class ContactSubmission(models.Model):
    """A message submitted via the /contact form."""
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} <{self.email}> @ {self.created_at:%Y-%m-%d}"


class Order(models.Model):
    """A customer order. Tracking ID is auto-assigned."""
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("PREPARING", "Preparing"),
        ("READY", "Ready for pickup"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    ]

    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, db_index=True)
    customer_name = models.CharField(max_length=120)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20, blank=True)
    ice_cream = models.ForeignKey(IceCream, on_delete=models.PROTECT, related_name="orders")
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    @property
    def total_price(self):
        return self.ice_cream.price * self.quantity

    def __str__(self):
        return f"{self.tracking_id.hex[:8]} {self.ice_cream} x{self.quantity} ({self.status})"
