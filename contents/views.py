from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet
import django_filters

from activites.models import Comment, CommentLike, EpisodeLike, Subscription
from activites.serializers import SubscriptionSerializer
from contents.models import Episode
from contents.permissions import (
    IsChannelOwnerOrReadOnly,
    IsCommentLikeOwnerOrReadyOnly,
    IsCommentOwnerOrReadyOnly,
    IsEpisodeOwnerOrReadOnly,
)
from profiles.models import Channel

from .serializers import (
    ChannelSerializer,
    CommentSerializer,
    CreateChannelSerializer,
    EpisodeSerializer,
    CommentLikeSerializer,
    UpdateChannelSerializer,
)


class ChannelsViewSet(viewsets.ModelViewSet):
    serializer_class = ChannelSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    queryset = Channel.objects.all()
    lookup_field = "username"
    http_method_names = ["get", "post", "delete", "patch"]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateChannelSerializer
        if self.request.method == "PUT":
            return UpdateChannelSerializer
        return ChannelSerializer

    def get_permissions(self):
        # http safe methods: GET, OPTIONS, HEAD
        # list, retrieve, create, destroy, update, partial_update
        if self.request.method in permissions.SAFE_METHODS:
            return []
        if self.action in ["list", "retrieve"]:
            return []
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["destroy", "partial_update"]:
            return [IsChannelOwnerOrReadOnly()]
        return [IsChannelOwnerOrReadOnly()]

    @action(detail=True, methods=["GET", "PUT"], permission_classes=[IsAdminUser])
    def subscribers(self, request, username):
        channel = get_object_or_404(Channel, username=username)
        subscribers = Subscription.objects.filter(channel_id=channel.id)
        serializer = SubscriptionSerializer(subscribers, many=True)
        return Response(serializer.data)


class EpisodesViewSet(viewsets.ModelViewSet):
    serializer_class = EpisodeSerializer
    http_method_names = ["get", "post", "delete", "patch"]
    # permission_classes = [IsEpisodeOwnerOrReadOnly]

    def get_queryset(self):
        channel_username = self.kwargs["channel_username"]
        return Episode.objects.filter(
            channel=Channel.objects.get(username=channel_username)
        ).all()

    def get_permissions(self):
        # http safe methods: GET, OPTIONS, HEAD
        # list, retrieve, create, destroy, update, partial_update
        if self.request.method in permissions.SAFE_METHODS:
            return []
        if self.action in ["list", "retrieve"]:
            return []
        if self.action in ["create"]:
            return [(permissions.IsAdminUser | IsEpisodeOwnerOrReadOnly)()]
        if self.action in ["destroy", "partial_update"]:
            return [IsChannelOwnerOrReadOnly()]
        return [IsChannelOwnerOrReadOnly()]

    def get_serializer_context(self):
        return {
            "request": self.request,
            "channel_username": self.kwargs["channel_username"],
        }


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "delete", "patch"]

    def get_queryset(self):
        episode_id = self.kwargs["episode_pk"]
        return Comment.objects.filter(episode_id=episode_id)

    def get_serializer_context(self):
        return {
            "episode_id": self.kwargs["episode_pk"],
            "request": self.request,
        }

    def get_permissions(self):
        # http safe methods: GET, OPTIONS, HEAD
        # list, retrieve, create, destroy, update, partial_update
        if self.request.method in permissions.SAFE_METHODS:
            return []
        if self.action in ["list", "retrieve"]:
            return []
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["destroy", "partial_update", "update"]:
            return [IsCommentOwnerOrReadyOnly()]
        return [IsCommentOwnerOrReadyOnly()]


class CommentLikeViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = CommentLikeSerializer
    # get, post, put, delete, patch
    http_method_names = ["get", "post", "delete"]

    def get_queryset(self):
        comment_id = self.kwargs["comment_pk"]
        return CommentLike.objects.filter(comment_id=comment_id)

    def get_serializer_context(self):
        return {
            "comment_id": self.kwargs["comment_pk"],
            "request": self.request,
        }

    def create(self, request, *args, **kwargs):
        user_id = self.request.user.id
        comment_id = self.kwargs["comment_pk"]

        already_liked_this_comment_by_user = CommentLike.objects.filter(
            comment_id=comment_id,
            user_id=user_id,
        )

        if already_liked_this_comment_by_user.exists():
            # already_liked_this_comment_by_user.delete()
            return Response({"Message": "Already liked."})
            # return Response({"Message": "Successfully deleted your like."})
        else:
            return super().create(request, *args, **kwargs)

    def get_permissions(self):
        # list, retrieve, create, destroy, update, partial_update
        if self.request.method in permissions.SAFE_METHODS:
            return []
        if self.action in ["list", "retrieve"]:
            return []
        if self.action == "create":
            return [IsAuthenticated()]
        if self.action == "destroy":
            return [IsCommentLikeOwnerOrReadyOnly()]

        return [IsCommentLikeOwnerOrReadyOnly()]
