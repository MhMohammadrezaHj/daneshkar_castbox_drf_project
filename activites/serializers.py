from django.shortcuts import get_object_or_404
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.response import Response

from activites.models import (
    Comment,
    CommentLike,
    EpisodeLike,
    PlayList,
    PlayListItem,
    Subscription,
)
from contents.models import Episode
from profiles.models import Channel
from accounts.serializers import UserSerializer

User = get_user_model()


class SubscriptionSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    channel_username = serializers.CharField(max_length=30, source="channel.username")

    class Meta:
        model = Subscription
        fields = ["id", "user", "datetime_created", "channel_username"]

    def create(self, validated_data):
        user_id = self.context["request"].user.id
        channel_username = validated_data.pop("channel")["username"]
        channel = get_object_or_404(Channel, username=channel_username)
        try:
            return Subscription.objects.get(channel_id=channel.id, user_id=user_id)
        except Subscription.DoesNotExist:
            print("create new subscription")
            return Subscription.objects.create(
                channel_id=channel.id,
                user_id=user_id,
                **validated_data,
            )


class PlayListItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayListItem
        fields = ["id", "episode"]

    def create(self, validated_data):
        request = self.context["request"]
        user_id = request.user.id
        playlist_id = self.context["playlist_id"]
        playlist = get_object_or_404(PlayList, user_id=user_id, id=playlist_id)
        return PlayListItem.objects.create(
            playlist_id=playlist.id,
            **validated_data,
        )


class PlayListSerializer(serializers.ModelSerializer):
    items = PlayListItemSerializer(many=True)

    class Meta:
        model = PlayList
        fields = ["id", "name", "items"]

    def create(self, validated_data):
        request = self.context["request"]
        user_id = request.user.id
        return PlayList.objects.create(user_id=user_id, **validated_data)

    # def create(self, validated_data):
    #     # get the channel that the user wants to subscribe
    #     channel_username = validated_data.pop("channel")["username"]
    #     channel = get_object_or_404(Channel, username=channel_username)
    #     # check if it is already subscribed
    #     request = self.context["request"]
    #     user_id = request.user.id
    #     already_subscriptions = Subscription.objects.get(
    #         user_id=user_id,
    #         channel_id=channel.id,
    #     )

    #     if already_subscriptions:
    #         return already_subscriptions

    #     return Subscription.objects.create(
    #         user_id=user_id,
    #         channel_id=channel.id,
    #         **validated_data,
    #     )
