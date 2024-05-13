from django.contrib import admin
from home.models import User, UserVideo, Video

# Register your models here.
admin.site.register(User)
admin.site.register(Video)
admin.site.register(UserVideo)