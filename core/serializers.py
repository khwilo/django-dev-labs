from rest_framework import serializers

from core.user.models import User


# Define the fields to be exposed by the API endpoints
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]
        extra_kwargs = {
            "url": {"view_name": "core_api:user-detail", "lookup_field": "pk"}
        }
