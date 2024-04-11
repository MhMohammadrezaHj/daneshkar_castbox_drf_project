from rest_framework import serializers
from django.contrib.auth import get_user_model

from logs.models import SeenChannel, SeenEpisode

User = get_user_model()


class SeenEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeenEpisode
        fields = ["id", "user", "datetime_created"]


class SeenChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeenChannel
        fields = ["id", "user", "datetime_created"]
