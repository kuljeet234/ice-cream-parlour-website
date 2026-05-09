from django.contrib import admin

from .models import ContactSubmission, IceCream, Order


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ("name", "flavor", "price", "is_available")
    list_filter = ("is_available",)
    search_fields = ("name", "flavor")


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("tracking_id", "customer_name", "ice_cream", "quantity", "status", "created_at")
    list_filter = ("status", "ice_cream")
    search_fields = ("customer_name", "customer_email", "tracking_id")
    readonly_fields = ("tracking_id", "created_at", "updated_at")
