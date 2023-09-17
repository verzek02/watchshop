from rest_framework import serializers
from .models import Watch
from rest_framework_simplejwt.authentication import JWTAuthentication

class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = '__all__'