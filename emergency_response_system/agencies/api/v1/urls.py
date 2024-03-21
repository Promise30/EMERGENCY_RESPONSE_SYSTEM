from django.urls import path
from emergency_response_system.agencies.api.v1.views import (
    AgencyAPIView,
    ServiceAPIView
)


urlpatterns = [
    path('service/', ServiceAPIView.as_view(), name='service'),
    path('add-agency/', AgencyAPIView.as_view(), name="agency")
]