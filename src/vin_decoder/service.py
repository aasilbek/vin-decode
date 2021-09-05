from abc import ABC, abstractmethod

from django.conf import settings

import requests

from .models import Vehicle


class DecodeInterface(ABC):
    @abstractmethod
    def decode(self, vin: str) -> Vehicle:
        pass


class PostmanMockDecoder(DecodeInterface):
    def _validate_status(self, result):
        if result["decode"]["status"] != "SUCCESS":
            raise ValueError("Invalid VIN")

    def decode(self, vin: str) -> Vehicle:
        vehicle = requests.get(settings.DECODER_SERVICE_URL + f"?vin={vin}")
        result = vehicle.json()
        self._validate_status(result)
        vehicle = result["decode"]["vehicle"][0]
        return Vehicle.objects.create(
            vin=vin,
            make=vehicle["make"],
            model=vehicle["model"],
            year=vehicle["year"],
            vehicle_type=vehicle["body"],
            color=vehicle.get("color"),
            weight=vehicle.get("weight"),
            dimensions=vehicle.get("dimensions"),
        )


def get_vehicle_by_vin(vin: str) -> Vehicle:
    vehicle = Vehicle.objects.filter(vin=vin)
    if vehicle.exists():
        return vehicle.first()
    decoder_service = PostmanMockDecoder()
    return decoder_service.decode(vin=vin)
