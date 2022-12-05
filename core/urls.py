from django.urls import path,include
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path("hotels/filter",FilterHotelView.as_view(),name="hotel_filter"),
    path("hotel/<int:pk>",HotelView.as_view(),name="hotel"),
    path("hotel/<int:pk>/availability",HotelAvailabilityView.as_view(),name="hotel_availability")
]