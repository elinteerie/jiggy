from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import AbstractUser
from waitlist.models import University
import random
import secrets
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)




class User(AbstractUser):
    username = None  # Remove the username field
    email = models.EmailField(unique=True)
    about = models.TextField(blank=True)
    #avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    country = models.CharField(max_length=100, blank=True)
    institution = models.ForeignKey(University, on_delete=models.CASCADE, related_name='user_uni', null=True)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    graduation_year = models.IntegerField(blank=True, null=True)


    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email





class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)

    def is_valid(self):
        # Check if the OTP is still valid (lasts for 10 minutes)
        return timezone.now() - self.created_at < timezone.timedelta(minutes=10)
    
    @classmethod
    def generate_otp(cls, user):
        # Generate a secure random 6-digit OTP
        otp_code = ''.join(secrets.choice("0123456789") for _ in range(4))

        # Create and save the OTP instance
        otp = cls(user=user, code=otp_code)
        otp.save()

        return otp
    

class GeneratedNames(models.Model):
    name = models.CharField(max_length=254, null=True, blank=True)
    used = models.BooleanField(default=False)
