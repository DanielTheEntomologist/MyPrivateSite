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
    thumbnail = models.ImageField(null=True, blank=True)
    advertisement = models.CharField(
        max_length=200, default=None, blank=True, null=True
    )
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
    thumbnail = models.ImageField(null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True
    )
    featured = models.BooleanField()
    display_order = models.IntegerField(default=99)

    def __str__(self):
        return self.title


class CurriculumVitae(models.Model):
    name = models.CharField(max_length=50)
    pdf_file = models.FileField(upload_to="cv/")

    def __str__(self):
        return self.name


from website.storage import MyStorage


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(storage=MyStorage())
    mobile_thumbnail = models.ImageField(null=True, blank=True, storage=MyStorage())
    hosted_url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    skills = models.ManyToManyField("Skill")

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class SkillProfile(models.Model):
    profile_name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    skills = models.ManyToManyField(Skill)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    rating = models.IntegerField()

    def __str__(self):
        return f"{self.user.username} - {','.join(skill.name for skill in self.skills.all())}"
