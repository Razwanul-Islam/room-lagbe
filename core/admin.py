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

    def get_queryset(self, request) :
        if request.user.is_superuser:
            return Hotel.objects.all()
        return Hotel.objects.filter(manager=request.user)
    # when a user create a hotel from admin panel then he is the manager
    def save_model(self, request, obj, form, change):
        obj.manager = request.user
        obj.save()
        return super().save_model(request, obj, form, change)

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

    def get_queryset(self, request) :
        if request.user.is_superuser:
            return RoomBook.objects.all()
        return RoomBook.objects.filter(room__hotel__manager=request.user)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    model = ContactMessage
    list_display = ['name','email','message','created_at']
    ordering = ['created_at']
    sortable_by = ['name','email']
    search_fields = ['id','name','email','created_at','message']
    
# Register your models here.
