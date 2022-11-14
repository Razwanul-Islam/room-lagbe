from django.db import models
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

class Room(AutoModel):
    room_number = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField( max_length=50,blank=True,null=True)
    is_booked = models.BooleanField(default=False)

# Create your models here.
