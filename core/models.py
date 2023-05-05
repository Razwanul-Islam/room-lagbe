from django.db import models
from django.contrib.auth.models  import User
from tinymce.models import HTMLField

class AutoModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Hotel(AutoModel):
    name = models.CharField(max_length=150)
    description = HTMLField()
    moto = models.TextField(null=True,default="Catchy moto goes here...")
    location = models.CharField(max_length=300)
    cover_photo = models.ImageField( upload_to="images/")
    tag = models.CharField(max_length=120,default="Bangladesh,3 star")
    per_night_cost = models.DecimalField( max_digits=10, decimal_places=2,default=0)
    manager = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.id)+"-"+self.name

class Room(AutoModel):
    CHOICES= (("single","single"),("double","double"))
    room_number = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField( max_length=50,choices=CHOICES,blank=True,null=True)
    is_booked = models.BooleanField(default=False)
    class Meta:
        unique_together = ["room_number","hotel"]
    def __str__(self) -> str:
        return self.hotel.__str__()+"-"+self.room_number

class FeaturedHotel(AutoModel):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    active = models.BooleanField(default=True)

class RoomBook(AutoModel):
    CHOICES = (("pending","pending"),("booked","booked"),("checked_in","checked_in"),("checked_out","checked_out"),("cancelled","cancelled"))
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField( auto_now=False, auto_now_add=False)
    check_out_date = models.DateField( auto_now=False, auto_now_add=False)
    status = models.CharField( max_length=50,choices=CHOICES)
    total_cost = models.DecimalField( max_digits=10, decimal_places=2,default=0)
    stripe_session_id = models.CharField(max_length=255,null=True, blank=True)
    stripe_checkout_url = models.CharField(max_length=400,null=True, blank=True)

class ContactMessage(AutoModel):
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    

# Create your models here.
