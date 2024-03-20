from .base import *


REST_FRAMEWORK = {

    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler"
}


LOCAL_APPS = [
    "emergency_response_system.accounts",
    "emergency_response_system.agencies",
    "emergency_response_system.reports"
]


THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "drf_standardized_errors",
]

INSTALLED_APPS += LOCAL_APPS + THIRD_PARTY_APPS

AUTH_USER_MODEL = 'accounts.CustomUser'

