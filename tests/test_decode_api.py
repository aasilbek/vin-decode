import pytest
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from vin_decoder.models import Vehicle


@pytest.mark.django_db
def test_decode_api(django_assert_num_queries):
    client = APIClient()
    vin_number = "2C4RC1DG3HR711964"
    url = reverse("vin_decoder:detail", kwargs={"vin": vin_number})
    with django_assert_num_queries(3):
        response = client.get(url)
    vehicle = Vehicle.objects.filter(vin=vin_number).first()

    assert response.status_code == status.HTTP_200_OK
    assert vehicle.vin == vin_number
