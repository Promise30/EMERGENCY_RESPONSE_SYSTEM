from rest_framework import permissions, generics
from emergency_response_system.agencies.api.v1.serializers import (
    ServiceSerializer,
    AgencySerializer
)
from rest_framework.response import Response

class ServiceAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = ServiceSerializer

    def post(self, request, *args, **kwargs):
       response = Response({"message": "Report submitted successfully"})
       response.set_cookie(key='visitor_id', value='your_visitor_id_value', max_age=3600)  # Example cookie settings
       return super().post(request, *args, **kwargs)

class AgencyAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AgencySerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)