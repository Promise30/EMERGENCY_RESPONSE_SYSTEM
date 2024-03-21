from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]
        
    
    def validate(self, attrs):
        return super().validate(attrs)
    
    @transaction.atomic
    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'agency',
            'first_name',
            'last_name',
        ]
class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs) :
        """
        This is for validating the values provided by user to login
        """
        user = User.objects.filter(email=attrs["email"]).first()

        error = {}
        if (user and user.check_password(attrs["password"])) and (user.is_active == True):
            return user

        else:
            error["credential_error"] = "Please recheck the credentials provided."
            raise serializers.ValidationError(error)
    
    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {"refresh": str(refresh), 
                "access_token": str(refresh.access_token),
                "user": UserSerializer(instance).data
                }