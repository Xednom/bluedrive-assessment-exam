from django.db import models

from apps.core.models import CoreModel


class Post(CoreModel):
    DRAFT = "draft"
    PUBLISHED = "published"
    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("author", on_delete=models.CASCADE)
    status = models.CharField(max_length=250, choices=STATUS_CHOICES)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["author"], name="author_idx"),
            models.Index(fields=["status"], name="status_idx"),
        ]
