# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#    address = models.TextField(blank=True, null=True)

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, 
        verbose_name=_("user"), 
        on_delete=models.CASCADE
    )
    address = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
