from rest_framework import serializers
from emergency_response_system.agencies.models import (
    Agency,
    Service
)

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'service_type',
            'description'
        ] 


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = [
            'service',
            'agency_name',
            'contactPerson',
            'address'
        ]