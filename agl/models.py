from django.db import models
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Annon(models.Model):
    annon_user = models.OneToOneField(User, on_delete=models.CASCADE)
    annon_username = models.CharField(max_length=40)
    


    def __str__(self) -> str:
        return self.annon_username




class AMessages(models.Model):
    annon_user = models.ForeignKey(Annon, on_delete=models.CASCADE)
    content = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_created']
    
    

    def __str__(self) -> str:
        return self.content
    
def generate_short_uuid():
    return str(uuid.uuid4()).replace('-', '')[:10]

class AnonChat(models.Model):
    annon_user = models.ForeignKey(Annon, on_delete=models.CASCADE)
    chat = models.CharField(default=generate_short_uuid, editable=False, unique=True, max_length=10)
    message = models.ManyToManyField(AMessages, related_name='anon_mess', blank=True)
    pass_code = models.CharField(max_length=6, unique=True)
    group = models.BooleanField(default=False)
    joiners = models.ManyToManyField(Annon, related_name='ch_messagengers', blank=True)
    
    

    def __str__(self):
        return str(self.chat)
    

    def save(self, *args, **kwargs):
        if not self.pass_code:
            self.pass_code = str(uuid.uuid4()).replace('-', '')[:6]
        super().save(*args, **kwargs)
    




