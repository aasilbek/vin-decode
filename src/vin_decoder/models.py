from django.contrib.postgres.indexes import BrinIndex, GinIndex
from django.contrib.postgres.search import SearchVector, SearchVectorField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Vehicle(models.Model):
    vin = models.CharField(max_length=17, unique=True)
    model = models.CharField(max_length=50)
    make = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=255, blank=True)
    year = models.PositiveIntegerField()
    color = models.JSONField(default=dict, blank=True)
    dimensions = models.JSONField(default=dict, blank=True)
    weight = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    search_vector = SearchVectorField(blank=True, null=True, editable=False)

    class Meta:
        db_table = "vehicles"
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"
        indexes = [
            models.Index(fields=["vin"]),
            models.Index(fields=["model"]),
            models.Index(fields=["make"]),
            models.Index(fields=["vehicle_type"]),
            GinIndex(fields=["search_vector"]),
            BrinIndex(fields=["created_at"]),
        ]


@receiver(post_save, sender=Vehicle)
def update_search_vector_for_vehicle_model(sender, **kwargs):
    Vehicle.objects.filter(pk=kwargs["instance"].id).update(
        search_vector=(SearchVector("vin", "model", "make", "vehicle_type"))
    )
