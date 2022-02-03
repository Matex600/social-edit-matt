from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=300, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    post_image = CloudinaryField('image', default='proxy-image')
    date_created = models.DateTimeField(auto_now_add=True)
    section = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='blog_upvote', blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def number_of_likes(self):
        return self.likes.count()

class Comment(models.Model):
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
