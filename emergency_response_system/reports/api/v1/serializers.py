from rest_framework import serializers
from emergency_response_system.reports.models import (
    EmergencyReport
)
from emergency_response_system.agencies.api.v1.serializers import (
    AgencySerializer
)


class EmergencyReportSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', required=False)

    class Meta:
        model = EmergencyReport
        fields = [
            'agency',
            'latitude',
            'longitude',
            'description',
            'status'
        ]
        
    def create(self, validated_data):
        return super().create(validated_data)


class AgencyEmergencySerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display', required=False)
    class Meta:
        model = EmergencyReport
        fields =[
            'id',
            'agency',
            'description',
            'status',
        ]

class ChangeEmergencyReportStatusSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EmergencyReport
        fields = [
            'status',
        ]

