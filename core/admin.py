from django.contrib import admin
from .models import Hotel,Room,FeaturedHotel

class RoomInHotel(admin.TabularInline):
    model = Room
    min_num = 0
class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    list_display = ["id","name","location"]
    sortable_by = ["name","location"]
    search_fields = ["id","name","location"]
    inlines = [RoomInHotel]
class FeaturedHotelAdmin(admin.ModelAdmin):
    model = FeaturedHotel
    list_display = ["id","hotel","created_at","active","updated_at"]
    ordering = ["hotel","created_at","updated_at","active"]
    sortable_by = ["hotel","created_at","updated_at"]
    search_fields = ["id","hotel__name","hotel__location"]

admin.site.register(Hotel,HotelAdmin)
admin.site.register(FeaturedHotel,FeaturedHotelAdmin)
    
    
# Register your models here.
