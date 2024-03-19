from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'image',
            'username',
            'email',
            'password',
            'date_of_birth'
        ]
        
    
    def validate(self, attrs):
        return super().validate(attrs)
    


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