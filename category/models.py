from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone


class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
    def __set__(self):
        return self.name
class Page(models.Model):
    CHAR_MAX_LENGTH = 128
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=CHAR_MAX_LENGTH, unique=True)
    rate = models.CharField(max_length=20, default="0")
    intro = models.CharField(max_length=CHAR_MAX_LENGTH)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Page, self).save(*args, **kwargs)
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wonder = models.ForeignKey(Page, on_delete=models.CASCADE)
    rate = models.CharField(max_length=20, default="0")
    comment = models.CharField(max_length=512)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.user+self.wonder
