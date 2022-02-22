from django.contrib import admin
from .models import UserProfile

# For getting the userprofile in admin
admin.site.register(UserProfile)
