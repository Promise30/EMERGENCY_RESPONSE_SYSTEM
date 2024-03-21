from django.urls import path
from emergency_response_system.accounts.api.v1.views import(
    RegistrationAPIView,
    SignInAPIVIew,
)


urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name='registration'),
    path('sign-in/', SignInAPIVIew.as_view(), name="sign_in")
]