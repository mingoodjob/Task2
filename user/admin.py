from django.contrib import admin
from user.models import UserModel, UserProfile

admin.site.register(UserModel)
admin.site.register(UserProfile)