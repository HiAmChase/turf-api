from rest_framework import serializers
from .models import User, Turf, Image

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class TurfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turf
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"