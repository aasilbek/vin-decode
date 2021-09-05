from django.contrib import admin

from .models import Vehicle


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
        "vin",
        "model",
        "make",
        "vehicle_type",
        "year",
        "created_at",
    )
    list_filter = ("year",)
    search_fields = ("search_vector",)
