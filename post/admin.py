from django.contrib import admin
from .models import Post, ContentType, Comment
# Register your models here.


admin.site.register(Post)
admin.site.register(ContentType)
admin.site.register(Comment)
