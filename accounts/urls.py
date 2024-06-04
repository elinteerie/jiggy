
from django.urls import path, include

urlpatterns = [
    path('oauth/', include('drf_social_oauth2.urls', namespace='drf')),
    
]




