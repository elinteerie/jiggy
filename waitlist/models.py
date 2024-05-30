# models.py
from django.db import models
import uuid


class University(models.Model):
    name = models.CharField(max_length=290)
    short_name= models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.short_name

class Student(models.Model):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    university_or_college = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university_of_student')
    expected_graduation_year = models.IntegerField()
    jiggy_coin_balance = models.IntegerField(default=0)
    referral_code = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.email

    def generate_referral_id(self):
        if not self.referral_code:
            self.referral_code = str(uuid.uuid4())[:5]  # Generate a unique referral ID
            self.save()

    def increase_balance(self):
        self.JIggy_coin_balance += 2
        self.save()

class Referral(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='referrals')
    referred_client = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='referred_by')
    referred_bonus = models.IntegerField(default=50)


    def __str__(self):
        return f"{self.referred_client} referred by {self.user.email}"