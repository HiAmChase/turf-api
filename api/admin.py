from django.contrib import admin
from .models import User, Turf, Image
# Register your models here.
admin.site.register(User)
admin.site.register(Turf)
admin.site.register(Image)