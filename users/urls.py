from django.urls import path
from .views import permission_user

urlpatterns = [
    path('create_permissions/', permission_user, name='create_permissions'),
]