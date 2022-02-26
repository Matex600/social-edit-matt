"""
Importing models from django
User from Auth
Cloudinary model
Reverse Url.
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Category(models.Model):
    """
    Class representing categories model.
    """
    name = models.CharField(max_length=255)

    class Meta:
        """
        Change categorys to categories using class meta.
        """
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        """
        This fixes an error which the button on add categories
        is not taking user back as expected.
        """
        return reverse('home')


class Post(models.Model):
    """
    A class to represent the model for posts in the blog
    details and the functionality that will be present when
    creating post.
    """
    title = models.CharField(max_length=260)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    category = models.ForeignKey(
        Category, related_name='blog_posts', on_delete=models.CASCADE)
    blog_snippet = models.CharField(max_length=255)
    post_image = CloudinaryField('image', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='blog_upvote', blank=True)

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        """
        This fixes an error which the button on add blog post
        is not taking user back as expected.
        """
        return reverse('home')

    def number_of_likes(self):
        """
        Method returns total number of likes on post.
        """
        return self.likes.count()


class Comment(models.Model):
    """
    Class representing comment model
    that have to be approved by an admin.
    """
    post = models.ForeignKey(Post, related_name='comments',
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField('approved', default=False)

    class Meta:
        """
        Shows order of comments.
        """
        ordering = ['-date_created']

    def __str__(self):
        return f"Comment {self.content} by {self.name}"
