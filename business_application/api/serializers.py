from rest_framework import serializers
from business_application.models import BusinessApplication

class BusinessApplicationSerializer(serializers.ModelSerializer):
    """
    Serializer for the BusinessApplication model.
    Provides representation for API interactions.
    """
    class Meta:
        model = BusinessApplication
        fields = [
            'id',
            'name',
            'appcode',
            'description',
            'owner',
            'delegate',
            'servicenow',
        ]