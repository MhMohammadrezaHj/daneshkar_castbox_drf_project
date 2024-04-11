from django.db import models
from django.contrib.auth import get_user_model
from contents.models import Episode
from profiles.models import Channel
from shared.models import BaseModel

User = get_user_model()


class SeenEpisode(BaseModel):
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="episode_watched"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_watched"
    )


class SeenChannel(BaseModel):
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="channel_seens"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_seens")
