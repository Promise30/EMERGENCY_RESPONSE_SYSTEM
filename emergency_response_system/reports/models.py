from django.db import models
from emergency_response_system.utils.base_model import BaseModel
from emergency_response_system.agencies.models import (
    Agency
)


class EmergencyReportStatus(models.TextChoices):
    UNRESOLVED = 'UNRESOLVED', 'Unresolved'
    IN_PROGRESS = 'IN_PROGRESS', 'In progress'
    RESOLVED = 'RESOLVED', 'Resolved'


class EmergencyReport(BaseModel):

    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=200, null=False, blank=False)
    longitude = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=EmergencyReportStatus.choices, default=EmergencyReportStatus.UNRESOLVED)

