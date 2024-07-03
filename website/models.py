from django.db import models

from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=25)
    sub_title = models.CharField(max_length=25)
    slug = models.SlugField()
    thumbnail = models.ImageField(null=True,blank=True)
    advertisement = models.CharField(max_length=200,default=None,blank=True,null=True)
    visible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
    featured = models.BooleanField()
    display_order = models.IntegerField(default=99)

    def __str__(self):
        return self.title



