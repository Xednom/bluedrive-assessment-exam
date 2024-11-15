from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = [
        "email",
    ]

    @property
    def user_full_name(self):
        return f"{self.first_name} {self.last_name}"
