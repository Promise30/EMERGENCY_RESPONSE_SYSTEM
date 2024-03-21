from django.db import models
from emergency_response_system.utils.base_model import (
    BaseModel
)


from django.contrib.auth.models import AbstractUser


class CustomUser(BaseModel, AbstractUser):
    
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True)
    agency = models.CharField(max_length=100, null=False, blank=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
