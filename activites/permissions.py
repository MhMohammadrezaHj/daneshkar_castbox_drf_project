from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission
from rest_framework import permissions

from activites.models import PlayList, PlayListItem, Subscription


class IsSubscriptionOwner(BasePermission):
    def has_permission(self, request, view):
        subscription = get_object_or_404(Subscription, pk=view.kwargs["pk"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if subscription.user.id == request.user.id:
            return True
        return False


class IsPlayListOwner(BasePermission):
    def has_permission(self, request, view):
        playlist = get_object_or_404(PlayList, pk=view.kwargs["pk"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if playlist.user.id == request.user.id:
            return True
        return False


class IsPlayListItemOwner(BasePermission):
    def has_permission(self, request, view):
        playlist_item = get_object_or_404(PlayListItem, pk=view.kwargs["pk"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if playlist_item.playlist.user.id == request.user.id:
            return True
        return False
