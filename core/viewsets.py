from rest_framework import viewsets

from core.user.models import User

from .serializers import UserSerializer


# Define the behavior of the API endpoint
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
