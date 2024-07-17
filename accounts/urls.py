
from django.urls import path, include
from .views import *

urlpatterns = [
    path('oauth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('register/', RegistrationAPIView.as_view(), name='registration_api'),
    path('user_detail/', UserDetailsView.as_view(),name='user_details'),
    path('update_user/', UpdateUserView.as_view(), name="update_user_info"),
    path('generate_name/', AssignPredefinedNameView.as_view(), name='assign_name'),
    
]




