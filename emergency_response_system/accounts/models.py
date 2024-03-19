from django.db import models
from emergency_response_system.utils.base_model import (
    BaseModel
)

class CustomUser(BaseModel):
    email = models.EmailField(max_length=70, blank=False, null=False, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
