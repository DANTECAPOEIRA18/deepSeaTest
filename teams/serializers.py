from .models import teams
from rest_framework import serializers


class team_serializer(serializers.ModelSerializer):
    class Meta:
        model = teams
        fields = '__all__'
