from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=False)
    username = models.CharField(unique=True, max_length=255, db_index=True)
    # is_active = models.BooleanField(null=False)
    # is_staff = models

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']