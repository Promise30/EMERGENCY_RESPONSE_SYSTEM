from rest_framework import generics, permissions
from emergency_response_system.reports.api.v1.serializers import (
    EmergencyReportSerializer,
    ChangeEmergencyReportStatusSerializer,
    AgencyEmergencySerializer
    
)
from emergency_response_system.agencies.models import Agency
from emergency_response_system.reports.models import (
    EmergencyReport
)


class EmergencyReportAPIView(generics.CreateAPIView):
    serializer_class = EmergencyReportSerializer
    permission_classes = [permissions.AllowAny,]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class AgencyEmergencyReportAPIView(generics.ListAPIView):
    serializer_class = AgencyEmergencySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        agency_id = Agency.objects.filter(agency_name=self.kwargs['agency_name']).first().id

        agency_reports_queryset = EmergencyReport.objects.filter(agency_id=agency_id).all()
        return agency_reports_queryset

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
class ChangeEmergencyReportStatusAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ChangeEmergencyReportStatusSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = EmergencyReport.objects.all()
    

    def get_object(self):
        report_obj = EmergencyReport.objects.filter(id=self.kwargs['report_id']).first()
        return report_obj
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)


