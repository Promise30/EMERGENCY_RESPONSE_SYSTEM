from rest_framework import generics, permissions
from emergency_response_system.accounts.api.v1.serializers import (
    RegistrationSerializer,
    SignInSerializer,
)
from rest_framework.response import Response

class RegistrationAPIView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    



class SignInAPIVIew(generics.GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = (permissions.AllowAny,)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            
            return Response(serializer.data)
        

