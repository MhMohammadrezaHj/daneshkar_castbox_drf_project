from rest_framework import serializers
from django.contrib.auth import get_user_model

from activites.models import Comment, CommentLike, EpisodeLike
from contents.models import Episode
from profiles.models import Channel
from accounts.serializers import UserSerializer

User = get_user_model()


class ChannelOwnerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class ChannelSerializer(serializers.ModelSerializer):
    user = ChannelOwnerUserSerializer()

    class Meta:
        model = Channel
        fields = [
            "id",
            "cover",
            "user",
            "name",
            "username",
        ]


class UpdateChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "cover",
            "name",
        ]


class CreateChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            "cover",
            "name",
            "username",
        ]

    def create(self, validated_data):
        request = self.context["request"]
        user_id = request.user.id
        return Channel.objects.create(user_id=user_id, **validated_data)


class EpisodeSerializer(serializers.ModelSerializer):
    cover = serializers.SerializerMethodField()
    audio = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = ["id", "title", "audio", "cover", "description", "datetime_created"]

    def create(self, validated_data):
        channel_username = self.context["channel_username"]
        return Episode.objects.create(
            channel_id=Channel.objects.get(username=channel_username).id,
            **validated_data,
        )

    def get_cover(self, episode):
        request = self.context.get("request")
        try:
            return str(request.build_absolute_uri(episode.cover.url))
        except:
            return ""

    def get_audio(self, episode):
        request = self.context.get("request")
        try:
            return str(request.build_absolute_uri(episode.audio.url))
        except:
            return ""


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ["id", "user", "body", "datetime_created"]

    def create(self, validated_data):
        episode_id = self.context["episode_id"]
        request = self.context["request"]
        user_id = request.user.id
        return Comment.objects.create(
            episode_id=episode_id,
            user_id=user_id,
            **validated_data,
        )


class CommentLikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CommentLike
        fields = ["id", "user"]

    def create(self, validated_data):
        comment_id = self.context["comment_id"]
        request = self.context["request"]
        user_id = request.user.id
        return CommentLike.objects.create(
            comment_id=comment_id,
            user_id=user_id,
            **validated_data,
        )
