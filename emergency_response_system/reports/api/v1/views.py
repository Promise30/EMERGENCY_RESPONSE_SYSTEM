from rest_framework import generics, permissions
from emergency_response_system.reports.api.v1.serializers import (
    EmergencyReportSerializer,
    ChangeEmergencyReportStatusSerializer,
    AgencyEmergencySerializer
    
)


class EmergencyReportAPIView(generics.CreateAPIView):
    serializer_class = EmergencyReportSerializer
    permission_classes = [permissions.AllowAny,]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AgencyEmergencyReportAPIView(generics.ListAPIView):

    serializer_class = AgencyEmergencySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ChangeEmergencyReportStatusAPIView(generics.UpdateAPIView):
    serializer_class = ChangeEmergencyReportStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


