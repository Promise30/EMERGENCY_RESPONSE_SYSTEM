from django.urls import path
from emergency_response_system.reports.api.v1.views import (
    EmergencyReportAPIView,
    ChangeEmergencyReportStatusAPIView,
    AgencyEmergencyReportAPIView
)

app_name  = 'reports'

urlpatterns = [
    path('report/', EmergencyReportAPIView.as_view(), name= 'reports'),
    path('change-report-status/<str:report_id>/', ChangeEmergencyReportStatusAPIView.as_view(), name='change_report_status'),
    path('agency-reports/<str:agency_name>/', AgencyEmergencyReportAPIView.as_view(), name='agency-reports/')
]