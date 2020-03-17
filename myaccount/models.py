from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# UserProfile, model for website users


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes
    logInDate = models.DateField(null=True)
    personalURL = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
