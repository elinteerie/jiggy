from django.shortcuts import render
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .email_template import *


class RegistrationAPIView(generics.CreateAPIView):
    """
    Handles user registration through a POST request.
    Upon successful registration, a welcome email is sent to the user.

    Example:
        To register a new user, make a POST request to the 'accounts/register/' endpoint with the required data.

        eg:
        {
            "email": "",
            "password": ""
            "institution": ""
        }
    """

    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = self.perform_create(serializer)

        # Customize the response data
        response_data = {
            'user_id': user.id,
            'email': user.email,
            'message': 'User registered successfully'
        }

        headers = self.get_success_headers(serializer.data)
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        """
        Save the user instance and send a welcome email.
        """
        user = serializer.save()
        send_welcome_email(user.email)

        # Generate and assign an OTP secret to the user
        otp_token = OTP.generate_otp(user)
        send_otp_email(user.email, otp_token)

        return user






class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserViewSerializer

    def get_object(self):
        return self.request.user
        
    