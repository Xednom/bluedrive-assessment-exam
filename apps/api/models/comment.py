from django.db import models

from apps.core.models import CoreModel


class Comment(CoreModel):
    post = models.ForeignKey("post", on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["post"], name="post_idx")]
