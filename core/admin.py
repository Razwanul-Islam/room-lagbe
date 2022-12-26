from django.contrib import admin
from .models import Hotel,Room,FeaturedHotel,RoomBook,ContactMessage

class RoomInHotel(admin.TabularInline):
    model = Room
    extra = 0

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    model = Hotel
    list_display = ["id","name","location"]
    sortable_by = ["name","location"]
    search_fields = ["id","name","location"]
    inlines = [RoomInHotel]

@admin.register(FeaturedHotel)
class FeaturedHotelAdmin(admin.ModelAdmin):
    model = FeaturedHotel
    list_display = ["id","hotel","created_at","active","updated_at"]
    ordering = ["hotel","created_at","updated_at","active"]
    sortable_by = ["hotel","created_at","updated_at"]
    search_fields = ["id","hotel__name","hotel__location"]

@admin.register(RoomBook)
class RoomBookAdmin(admin.ModelAdmin):
    model = RoomBook
    list_display = ["id","room","status","check_in_date","check_out_date"]
    ordering = ["id","room","status","check_in_date","check_out_date"]
    sortable_by = ["id","room","status","check_in_date","check_out_date"]
    search_fields = ["id","room","status","check_in_date","check_out_date"]

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    model = ContactMessage
    list_display = ['name','email','message','created_at']
    ordering = ['created_at']
    sortable_by = ['name','email']
    search_fields = ['id','name','email','created_at','message']
    
# Register your models here.
