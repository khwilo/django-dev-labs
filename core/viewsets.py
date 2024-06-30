from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer


# Define the behavior of the API endpoint
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
