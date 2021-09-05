from rest_framework.generics import RetrieveAPIView
from rest_framework.serializers import ModelSerializer

from .models import Vehicle
from .service import get_vehicle_by_vin


class DetailVehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = (
            "vin",
            "model",
            "make",
            "vehicle_type",
            "year",
            "color",
            "dimensions",
            "weight",
        )


class DetailVehicleView(RetrieveAPIView):
    serializer_class = DetailVehicleSerializer

    def get_object(self):
        return get_vehicle_by_vin(self.kwargs["vin"])
