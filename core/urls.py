from django.urls import path,include
from .views import IndexView,FilterHotelView,HotelView,OrderView,HotelAvailabilityView,SuccessPaymentView,CancelPaymentView,UserBooking, ContactView

urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path("hotels/filter",FilterHotelView.as_view(),name="hotel_filter"),
    path("hotel/<int:pk>",HotelView.as_view(),name="hotel"),
    path("hotel/<int:pk>/availability",HotelAvailabilityView.as_view(),name="hotel_availability"),
    path("hotel/book/<int:pk>",OrderView.as_view(),name="hotel_book"),
    path("mybookings",UserBooking.as_view(),name="user_bookings"),
    path("payment/success/<int:pk>",SuccessPaymentView.as_view(),name="payment_success"),
    path("payment/cancel",CancelPaymentView.as_view(),name="payment_cancel"),
    path("contact",ContactView.as_view(),name="contact")
]