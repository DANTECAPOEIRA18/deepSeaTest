from django.shortcuts import render
from rest_framework import viewsets
from .models import teams
from .serializers import team_serializer


# Create your views here.

class team_view_set(viewsets.ModelViewSet):
    queryset = teams.objects.all()
    serializer_class = team_serializer
