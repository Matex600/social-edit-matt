"""
Importing models from django
User from Auth
Cloudinary model
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    """
    A class to represent the model for posts in the blog
    Detalis the functionality that will be present when
    Creating Post
    """
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='Meddit Blog!')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = CloudinaryField('image', default='proxy-image')
    date_created = models.DateTimeField(auto_now_add=True)
    section = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_upvote', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    class Meta:
        """
        Ordering of Objects from last to first
        """
        ordering = ['-date_created']

    def number_of_likes(self):
        """
        Method returns total number of likes on post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Class represnting comment model
    that have to be approved by an admin
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"
