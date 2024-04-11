from django.db import models
from django.conf import settings

from shared.models import BaseModel

from django.contrib.auth import get_user_model

User = get_user_model()


# class Customer(BaseModel):
#     user = models.OneToOneField(User, on_delete=models.PROTECT)

#     def __str__(self):
#         return self.get_user_display_name()

#     def get_user_display_name(self):
#         if self.user.first_name or self.user.last_name:
#             return f"{self.user.first_name} {self.user.last_name}"
#         return self.user.username


class ChannelManager(models.Manager):
    def does_user_own_any_channels(self, user_id):
        return Channel.objects.filter(user_id=user_id).exists()


class Channel(BaseModel):
    cover = models.ImageField(upload_to="uploads/channels/cover/", blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=30, unique=True)

    objects = ChannelManager()

    def __str__(self):
        return self.get_user_display_name()

    def get_user_display_name(self):
        if self.user.first_name or self.user.last_name:
            return f"{self.user.first_name} {self.user.last_name}"
        return self.user.username


class ChannelLink(BaseModel):
    LINK_TYPE = (
        ("instagram", "Instagram"),
        ("linkedin", "LinkedIn"),
        ("youtube", "Youtube"),
        ("twitter", "Twitter"),
        ("facebook", "Facebook"),
        ("tiktok", "TikTok"),
        ("website", "Website"),
    )

    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name="links")
    type = models.CharField(choices=LINK_TYPE, max_length=100)
    address = models.URLField(max_length=1000)
