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
    location = models.CharField(max_length=300)
    cover_photo = models.ImageField( upload_to="images/")
    
    def __str__(self):
        return str(self.id)+"-"+self.name

class Room(AutoModel):
    CHOICES= (("single","single"),("double","double"))
    room_number = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField( max_length=50,choices=CHOICES,blank=True,null=True)
    is_booked = models.BooleanField(default=False)

class FeaturedHotel(AutoModel):
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    active = models.BooleanField(default=True)

class RoomBook(AutoModel):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField( auto_now=False, auto_now_add=False)
    check_out_date = models.DateField( auto_now=False, auto_now_add=False)
    status = models.CharField( max_length=50)
    

# Create your models here.
