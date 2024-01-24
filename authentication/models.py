from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import AbstractUser


# for creation of custom users with their categories


class CustomUser(AbstractUser):
    USER_CATEGORIES = (
        ('analyst', 'Analyst'),
        ('controller', 'Controller'),
        ('manager', 'Manager'),
    )
    user_category = models.CharField(max_length=20, choices=USER_CATEGORIES)
