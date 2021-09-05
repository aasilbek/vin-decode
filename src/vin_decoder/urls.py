from django.urls import path

from vin_decoder.views import DetailVehicleView

urlpatterns = [path("<str:vin>/", DetailVehicleView.as_view(), name="detail")]
