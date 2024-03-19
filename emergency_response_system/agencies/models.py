from django.db import models
from emergency_response_system.utils.base_model import(
    BaseModel
)
from django.contrib.auth import get_user_model

User = get_user_model()

class Service(BaseModel):
    service_type = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=250, blank=False, null=False)


class Agency(BaseModel):
    service = models.ForeignKey(Service, on_delete=models.CAs)
    agency_name = models.CharField(max_length=200, unique=True, blank=False, null=False)
    contact_person = models.ForeignKey(User, on_delete=models.PROTECT, related_name="to_be_contacted")
