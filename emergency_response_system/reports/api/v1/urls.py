from django.urls import path
from emergency_response_system.reports.api.v1.views import (
    EmergencyReportAPIView
)

app_name  = 'reports'

urlpatterns = [
    path('reports/', EmergencyReportAPIView.as_view(), name= 'reports')
]