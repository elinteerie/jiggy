# serializers.py
from rest_framework import serializers
from .models import Student, University

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'phone_number', 'university_or_college', 'expected_graduation_year', 'jiggy_coin_balance', 'referral_code']
        read_only_fields = ['jiggy_coin_balance', 'referral_code']


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['id', 'name', 'short_name']


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
