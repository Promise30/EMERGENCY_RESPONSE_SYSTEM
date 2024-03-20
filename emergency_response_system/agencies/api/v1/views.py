from rest_framework import permissions, generics
from emergency_response_system.agencies.api.v1.serializers import (
    ServiceSerializer,
    AgencySerializer
)

class ServiceAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class AgencyAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AgencySerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
# class 