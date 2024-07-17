from rest_framework import serializers
from .models import User, PredefinedN




class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'institution']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

class CustomUserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', "last_name",'institution','country', 'pred_name']



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['about', 'country', 'institution', 'gender', 'graduation_year', 'pred_name']


    """def update(self, instance, validated_data):
        instance.about = validated_data.get('about', instance.about)
        instance.country = validated_data.get('country', instance.country)
        instance.institution = validated_data.get('institution', instance.institution)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.graduation_year = validated_data.get('graduation_year', instance.graduation_year)
        instance.save()
        return instance
"""


class PredefinedNSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredefinedN
        fields = ['id', 'name', 'used']