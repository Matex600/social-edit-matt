from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class UserProfile(models.Model):
    """
    User profile model displaying showing fields
    when user goes to their user profile.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    user_bio = models.TextField()
    user_image = CloudinaryField('image', null=True, blank=True)
    github_url = models.CharField(max_length=225, null=True, blank=True)
    linkedin_url = models.CharField(max_length=225, null=True, blank=True)
    facebook_url = models.CharField(max_length=225, null=True, blank=True)
    twitter_url = models.CharField(max_length=225, null=True, blank=True)
    instagram_url = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse('home')
