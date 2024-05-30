# views.py
from rest_framework import generics
from .models import Student, University
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import StudentSerializer, UniversitySerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        referral_code = self.request.query_params.get('referral_code')
        print(referral_code)
        if referral_code:
            try:
                referrer = Student.objects.get(referral_code=referral_code)
                referrer.jiggy_coin_balance += 1
                referrer.save()
            except Student.DoesNotExist:
                pass  # If referral code does not exist, just pass without raising an error
        
        student = serializer.save()
        student.generate_referral_id()


    def get(self, request, *args, **kwargs):
        universities = University.objects.all()
        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
