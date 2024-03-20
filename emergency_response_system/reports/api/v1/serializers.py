from rest_framework import serializers
from emergency_response_system.reports.models import (
    EmergencyReport
)


class EmergencyReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmergencyReport
        fields = [
            'agency',
            'latitude',
            'longitude',
            'description',
            'status'
        ]


class AgencyEmergencySerializer(serializers.ModelSerializer):

    class Meta:
        model = EmergencyReport
        fields =[
            'agency',
            'description',
            'status',
        ]

class ChangeEmergencyReportStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmergencyReport
        fields = [
            'status',
            'agency'
        ]

