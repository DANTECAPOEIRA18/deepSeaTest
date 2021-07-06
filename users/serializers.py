from .models import customUser
from rest_framework import serializers


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = '__all__'
