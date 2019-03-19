from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    send_mode = models.BooleanField(default=False)

