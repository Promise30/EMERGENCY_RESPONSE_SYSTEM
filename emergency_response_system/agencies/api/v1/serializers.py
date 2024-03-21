from rest_framework import serializers
from emergency_response_system.agencies.models import (
    Agency,
    Service
)

class ServiceSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Service
        fields = [
            'id',
            'service_type',
            'description'
        ] 


class AgencySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Agency
        fields = [
            'id',
            'service',
            'agency_name',
            'address'
        ]

    
    def create(self, validated_data):
        validated_data['contact_person_id'] = self.context['request'].user.id
        return super().create(validated_data)