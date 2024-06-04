
from django.urls import path, include
from .views import *

urlpatterns = [
    path('oauth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('register/', RegistrationAPIView.as_view(), name='registration_api'),
    
]




