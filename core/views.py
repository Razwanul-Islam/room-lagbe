from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse
from django.views.generic import TemplateView,ListView,View,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from datetime import datetime
from .models import FeaturedHotel, Hotel, Room, RoomBook, ContactMessage
from django.conf import settings
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY
MY_DOMAIN = "http://localhost:8000"
class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_hotels"] = FeaturedHotel.objects.all().filter(active=True).select_related("hotel")
        return context
    
class FilterHotelView(View):
    template_name = "filter_result.html"
    def post(self,request,*args, **kwargs):
        # select hotel where location or tag matched and if room is not booked or currently booked but free on checkin to chekout date range 
        queryset = Hotel.objects.filter((Q(location__icontains = request.POST.get("location")) | Q(tag__icontains=request.POST.get("location"))) & (Q(room__is_booked = False) | (Q(room__roombook__check_in_date__gt=request.POST.get("check_in_date")) & Q(room__roombook__check_in_date__gt=request.POST.get("check_out_date")) & Q(room__is_booked=True)) | (Q(room__roombook__check_out_date__lt=request.POST.get("check_in_date")) & Q(room__roombook__check_out_date__lt=request.POST.get("check_out_date"))  & Q(room__is_booked=True)) )).distinct()
        context = {}
        context["location"] =  request.POST.get("location")
        context["check_in_date"] = request.POST.get("check_in_date")
        context["check_out_date"] = request.POST.get("check_out_date")
        context["hotels"] = queryset
        return render(request,self.template_name,context)

# Hotel view description and check availability form
class HotelView(DetailView):
    model = Hotel
    template_name = "single_hotel.html"
    context_object_name = "hotel"
# Hotel Availability result and book form
class HotelAvailabilityView(View):
    template_name = "hotel_availability.html"
    def post(self,request,*args, **kwargs):
        context = {}
        date_format = "%Y-%m-%d"
        delta = datetime.strptime(request.POST.get("check_out_date"),date_format) - datetime.strptime(request.POST.get("check_in_date"),date_format)
        context["hotel"] = get_object_or_404(Hotel,id=kwargs.get("pk"))
        context["rooms"] = Room.objects.filter(Q(hotel=kwargs.get("pk"))&(Q(is_booked=False)| (Q(roombook__check_in_date__gt=request.POST.get("check_in_date")) & Q(roombook__check_in_date__gt=request.POST.get("check_out_date")) & Q(is_booked=True)) | (Q(roombook__check_out_date__lt=request.POST.get("check_in_date")) & Q(roombook__check_out_date__lt=request.POST.get("check_out_date"))  & Q(is_booked=True)))).distinct()
        context["check_in_date"] = request.POST.get("check_in_date")
        context["check_out_date"] = request.POST.get("check_out_date")
        context["total_cost"] = delta.days*context.get("hotel").per_night_cost
        return render(request,self.template_name,context)

# Hotel order
class OrderView(LoginRequiredMixin,View):
    login_url = '/accounts/login'
    redirect_field_name = "redirect_to"
    def post(self,request,*args,**kwargs):
        hotel = get_object_or_404(Hotel,id=kwargs.get("pk"))
        date_format = "%Y-%m-%d"
        delta = datetime.strptime(request.POST.get("check_out_date"),date_format) - datetime.strptime(request.POST.get("check_in_date"),date_format)
        room = get_object_or_404(Room,id=int(request.POST.get("room")))
        order = RoomBook.objects.create(
            room = room,
            user = request.user,
            check_in_date = request.POST.get("check_in_date"),
            check_out_date = request.POST.get("check_out_date"),
            status="pending",
            total_cost = float(hotel.per_night_cost*delta.days)
        )
        checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'name': hotel.name,
                        # convert dollar to cents
                        'amount': int(100*hotel.per_night_cost),
                        'currency': 'usd',
                        'quantity': delta.days
                    }
                ],
                payment_method_types=['card'],
                mode='payment',
                success_url=MY_DOMAIN + '/payment/success/'+str(order.id),
                cancel_url=MY_DOMAIN + '/payment/cancel',
            )
        order.stripe_session_id = checkout_session.id
        order.stripe_checkout_url = checkout_session.url
        order.save()
        return redirect(checkout_session.url, code=303)
# On successful payment
class SuccessPaymentView(LoginRequiredMixin,View):
    login_url = '/accounts/login'
    redirect_field_name = "redirect_to"
    template = 'single_text.html'
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        order = get_object_or_404(RoomBook,id = id,user=request.user)
        session = stripe.checkout.Session.retrieve(order.stripe_session_id)
        if session.payment_status == 'paid':
            order.status = 'booked'
            order.save()
            return render(request,self.template,{"text":"Your payment is successful ."})

        else:
            return render(request,self.template,{"text":"Your payment is not completed"})

class CancelPaymentView(LoginRequiredMixin,View):
    login_url = '/accounts/login'
    redirect_field_name = "redirect_to"
    template = 'single_text.html'
    def get(self,request,**kwargs):
        return render(request,self.template,{"text":"You cancelled the payment"})

class UserBooking(LoginRequiredMixin,ListView):
    login_url = '/accounts/login'
    redirect_field_name = "redirect_to"
    model = RoomBook
    template_name = "bookings.html"
    context_object_name = "orders"
    def get_queryset(self):
        status = ""
        if self.request.GET.get("status"):
            status = self.request.GET.get("status")
        return RoomBook.objects.filter(user=self.request.user,status__icontains=status).order_by("-created_at")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["status"] = ""
        if self.request.GET.get("status"):
            context["status"] = self.request.GET.get("status")
        return context

class ContactView(View):
    template_name = "contact.html"
    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)
    def post(self,request,*args, **kwargs):
        ContactMessage.objects.create(name=request.POST.get("name"),email=request.POST.get("email"),message=request.POST.get("message"))
        return render(request,self.template_name,{"sent_success":True})
