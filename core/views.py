from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from .models import FeaturedHotel

class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["featured_hotels"] = FeaturedHotel.objects.all().filter(active=True).select_related("hotel")
        return context
    
# Create your views here.
