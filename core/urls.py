from django.urls import path,include
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path("hotels/filter",FilterHotelView.as_view(),name="hotel_filter")
]