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
    thumbnail = models.ImageField()
    advertisement = models.CharField(max_length=200,default=None,blank=True,null=True)
    
    def __str__(self):
        return self.title
    
    @classmethod
    def get_default_pk(cls):
        category, created = cls.objects.get_or_create(
            title='Other', 
            defaults=dict(
            sub_title = "Miscellanous ideas",
            slug = "misc",
            thumbnail = None,
            advertisement = None
            )
        )
        return category.pk

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=Category.get_default_pk())
    featured = models.BooleanField()
    display_order = models.IntegerField(default=99)

    def __str__(self):
        return self.title



