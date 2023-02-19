from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class BlogCategory(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True)
    meta_title = models.CharField(max_length=100, help_text='Meta title contain 100 characters')
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField(max_length=4000)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title[:20]

    def get_absolute_url(self):
        return reverse('website:blog-details', args=[str(self.pk)])
