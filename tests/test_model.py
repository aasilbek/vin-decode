import pytest

from vin_decoder.models import Vehicle


@pytest.mark.django_db
def test_vehicle_model():
    Vehicle.objects.create(
        vin="2C4RC1DG3HR711964",
        make="Plymouth",
        model="Prowler",
        year=1997,
        vehicle_type="CONVERTIBLE 2-DR",
    )
    assert Vehicle.objects.count() == 1
