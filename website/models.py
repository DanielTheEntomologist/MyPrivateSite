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
    title = models.CharField(max_length=20)
    sub_title = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()
    
    def __str__(self):
        return self.title

# from django.core.files.storage import FileSystemStorage
# from django.conf import settings
# upload_storage = FileSystemStorage(location=settings.STATIC_ROOT, base_url='/staticfiles/images')
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # thumbnail = models.ImageField(upload_to='your_image_name', storage=upload_storage)
    # thumbnail = models.ImageField( storage=upload_storage)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()

    def __str__(self):
        return self.title



