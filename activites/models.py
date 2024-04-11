from django.db import models
from django.contrib.auth import get_user_model
from contents.models import Episode
from profiles.models import Channel
from shared.models import BaseModel


User = get_user_model()


class Subscription(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="subscriptions"
    )
    channel = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="subscribers"
    )


class Comment(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comments"
    )
    body = models.CharField(max_length=1000)
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="episode_comments"
    )
    parent_comment = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="comments",
        null=True,
    )


class EpisodeLike(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liked_episodes"
    )
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="episode_likes"
    )


class CommentLike(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="liked_comments"
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="episode_likes"
    )


class PlayList(BaseModel):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="playlists")


class PlayListItem(BaseModel):
    playlist = models.ForeignKey(
        PlayList, on_delete=models.CASCADE, related_name="items"
    )
    episode = models.ForeignKey(
        Episode, on_delete=models.CASCADE, related_name="playlists"
    )
