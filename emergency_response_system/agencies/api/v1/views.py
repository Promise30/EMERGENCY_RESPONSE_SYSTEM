from rest_framework import permissions, generics



class CreateAgencyAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    # serializer_class = 

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)