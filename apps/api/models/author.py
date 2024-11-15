from django.db import models

from apps.core.models import CoreModel


class Author(CoreModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    class Meta:
        indexes = [
            models.Index(fields=["name"], name="name_idx"),
            models.Index(fields=["email"], name="email_idx"),
        ]

    def __str__(self):
        return f"{self.name}"