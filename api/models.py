from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True) 
    password = models.CharField(max_length=255)
    ROLE_ENUM = [
        ("ADMIN", "ADMIN"),
        ("USER", "USER"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_ENUM, default="USER")
    phone = models.CharField(max_length=15)

class Turf(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    TYPE_ENUM = [
        ("TURF5", "TURF5"),
        ("TURF7", "TURF7"),
    ]
    type = models.CharField(max_length=10, choices=TYPE_ENUM, default="TURF5")
    price = models.FloatField(default=0.0)
    rating = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])

class Image(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE, related_name="turf_image")
    image = models.ImageField(blank=True, null=True, upload_to='turf_image')