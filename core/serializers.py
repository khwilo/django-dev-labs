from django.contrib.auth.models import User
from rest_framework import serializers


# Define the fields to be exposed by the API endpoints
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]
        extra_kwargs = {
            "url": {"view_name": "core_api:user-detail", "lookup_field": "pk"}
        }
