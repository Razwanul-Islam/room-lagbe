from django.shortcuts import render
from django.views.generic import TemplateView,ListView,View
from django.db.models import Q
from .models import FeaturedHotel, Hotel

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
    

# Create your views here.
