from django.db import models
from emergency_response_system.utils.base_model import BaseModel
from emergency_response_system.agencies.models import (
    Agency
)
from emergency_response_system.utils.constants import(
    EmergencyReportStatus
)
class EmergencyReport(BaseModel):
    
    EMERGENCY_REPORT_CHOICES = [
        (EmergencyReportStatus.UNRESOLVED, "Unresolved"),
        (EmergencyReportStatus.IN_PROGRESS, "In progress"),
        (EmergencyReportStatus.RESOLVED, "Resolved")

    ]

    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=200, null=False, blank=False)
    longitude = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=10, default=EMERGENCY_REPORT_CHOICES[0][0], choices=EMERGENCY_REPORT_CHOICES)

    