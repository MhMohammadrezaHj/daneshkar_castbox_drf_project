from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import mixins, GenericViewSet

from .permissions import IsPlayListItemOwner, IsPlayListOwner, IsSubscriptionOwner
from .models import PlayList, PlayListItem, Subscription
from .serializers import (
    PlayListItemSerializer,
    PlayListSerializer,
    SubscriptionSerializer,
)


class SubscribeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    http_method_names = ["get", "post", "delete"]

    def get_serializer_class(self):
        return SubscriptionSerializer

    def get_queryset(self):
        user_id = self.request.user.id
        return Subscription.objects.filter(user_id=user_id)

    def get_permissions(self):
        if self.action in ["retrieve", "destroy"]:
            return [(IsAuthenticated & IsSubscriptionOwner)()]
        return [IsAuthenticated()]


class PlayListViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        return PlayListSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    def get_queryset(self):
        user_id = self.request.user.id
        return PlayList.objects.filter(user_id=user_id)

    def get_permissions(self):
        if self.action in ["retrieve", "destroy", "partial_update"]:
            return [(IsAuthenticated & IsPlayListOwner)()]
        if self.action in ["list", "create"]:
            return [IsAuthenticated()]
        return [IsPlayListOwner()]


class PlayListItemViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    http_method_names = ["get", "post", "delete"]

    def get_serializer_class(self):
        return PlayListItemSerializer

    def get_serializer_context(self):
        print(self.kwargs)
        return {
            "request": self.request,
            "playlist_id": self.kwargs["playlist_pk"],
        }

    def get_queryset(self):
        user_id = self.request.user.id
        playlist_id = self.kwargs["playlist_pk"]
        return PlayListItem.objects.filter(
            playlist__user_id=user_id, playlist_id=playlist_id
        )

    def get_permissions(self):
        if self.action in ["list", "create"]:
            return [IsAuthenticated()]
        if self.action in ["retrieve", "destroy"]:
            return [(IsAuthenticated & IsPlayListItemOwner)()]
        return [IsPlayListItemOwner()]
