from django.urls import path
from .views import StudentCreateView, LoginView

urlpatterns = [
    path('student/', StudentCreateView.as_view(), name='student-create'),
    path('login/', LoginView.as_view(), name='login'),
]
