from django.db import models
from accounts.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class ContentType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Create your models here.
class Post(models.Model):
    #DEFAULT_CONTENT_TYPE_ID = 1
    content = models.TextField()
    headline = models.CharField(max_length=300)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    upvotes = models.ManyToManyField(User, related_name='upvoted_posts', blank=True)
    downvotes = models.ManyToManyField(User, related_name='downvoted_posts', blank=True)
    comments = models.TextField(blank=True)  # If comments are to be stored as text
    boosted = models.BooleanField(default=False)
    privacy = models.BooleanField(default=False)
    share_count = models.PositiveIntegerField(default=0)

    @property
    def upvote_count(self):
        return self.upvotes.count()

    @property
    def downvote_count(self):
        return self.downvotes.count()
    
    @property
    def share(self):
        self.share_count += 1
        self.save()

    def __str__(self):
        return f"{self.content_type}: {self.content[:20]} by {self.user.email}"
    


@receiver(post_save, sender=Post)
def post_save_handler(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "posts",
            {
                "type": "post_created",
                "post": {
                    "id": instance.id,
                    "content": instance.content,
                    "content_type": instance.content_type,
                    "time_created": instance.time_created.isoformat(),
                    "user": {
                        "id": instance.user.id,
                        "email": instance.user.email,
                        "institution": instance.user.institution.short_name,
                        "pred_name": instance.user.pred_name
                    },
                    "upvote_count": instance.upvote_count,
                    "downvote_count": instance.downvote_count,
                    "share_count": instance.share_count,
                    "boosted": instance.boosted,
                }
            }
        )