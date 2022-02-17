from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    """
    User model 
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_bio = models.TextField()

    def __str__(self):
        return f"{self.user}"

