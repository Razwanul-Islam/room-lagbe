from django.contrib import admin
from .models import Hotel,Room

class RoomInHotel(admin.TabularInline):
    model = Room

class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    list_display = ["id","name","location"]
    inlines = [RoomInHotel]

admin.site.register(Hotel,HotelAdmin)
    
    
# Register your models here.
