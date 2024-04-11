from django.db import models

from profiles.models import Channel
from shared.models import BaseModel


class Episode(BaseModel):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="episodes"
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    audio = models.FileField(upload_to="uploads/episodes/audio/")
    cover = models.ImageField(upload_to="uploads/episodes/cover/", blank=True)
