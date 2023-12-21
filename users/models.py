from django.contrib.auth.models import AbstractUser
from django.db import models
from main.models import NULLABLE
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    phone = models.CharField(max_length=50, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='автар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []