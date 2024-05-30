from django.urls import path
from .views import StudentCreateView

urlpatterns = [
    path('student/', StudentCreateView.as_view(), name='student-create'),
]
