from django.contrib import admin
from .models import AMessages, Annon, AnonChat


admin.site.register(Annon)
admin.site.register(AMessages)
admin.site.register(AnonChat)