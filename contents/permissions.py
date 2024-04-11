from rest_framework.permissions import BasePermission
from rest_framework import permissions

from activites.models import Comment, CommentLike
from contents.models import Episode
from profiles.models import Channel


class IsChannelOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        channel = Channel.objects.get(username=view.kwargs["username"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if channel.user.id == request.user.id:
            return True
        return False


class IsEpisodeOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        channel = Channel.objects.get(username=view.kwargs["channel_username"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if channel.user.id == request.user.id:
            return True
        return False


class IsCommentOwnerOrReadyOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        comment = Comment.objects.get(pk=view.kwargs["pk"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if comment.user.id == request.user.id:
            return True
        return False


class IsCommentLikeOwnerOrReadyOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        comment_like = CommentLike.objects.get(pk=view.kwargs["pk"])
        if request.method in permissions.SAFE_METHODS:
            return True
        if comment_like.user.id == request.user.id:
            return True
        return False


# class IsChannelOwnerOrReadOnlyPermission(BasePermission):
#     # TODO: refactor the code of this class
#     message = "You must be the owner of Channel to perform this action"

#     def has_object_permission(self, request, view, obj):
#         if not request.user.is_authenticated:
#             return False
#         print("enter has_object_permission")
#         user = self.get_user_for_obj(obj)
#         print(f"user: {user.username}")

#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # if user is staff can do anything
#         elif request.user.is_staff:
#             print("has_object_permission true: staff")
#             return True
#         # if a user wants to create a channel it is ok if it is authenticated
#         elif view.action == "create":
#             print("has_object_permission true: create")
#             # if type(obj) is Channel:
#             return request.user.is_authenticated
#             # if type(obj) is Episode:
#             #     return (request.user.is_authenticated) and (request.user.id == user.id)
#         # if the user owns a channel he can do anything
#         elif user.id == request.user.id:
#             print("has_object_permission true: owner")
#             return True
#         # otherwise it is not allowed
#         else:
#             print("has_object_permission false")
#             return False

#     def get_user_for_obj(self, obj):
#         assert type(obj) is Channel
#         return obj.user
#         # elif type(obj) is Episode:
#         #     return obj.channel.user


# class HasEpisodePermissionOrReadOnlyPermission(BasePermission):
#     # TODO: refactor the code of this class
#     message = "You must be the owner of Channel to perform this action"

#     def has_object_permission(self, request, view, obj):
#         if not request.user.is_authenticated:
#             return False
#         print("enter has_object_permission")
#         user = self.get_user_for_obj(obj)
#         print(f"user: {user.username}")

#         if request.method in permissions.SAFE_METHODS:
#             return True
#         # if user is staff can do anything
#         elif request.user.is_staff:
#             print("has_object_permission true: staff")
#             return True
#         # if a user wants to publish an episode it is ok if it is authenticated and the owner of channel
#         elif view.action == "create":
#             print("has_object_permission true: create")
#             print("$$$$$", request.user.id, user.id)
#             print((request.user.is_authenticated) and (request.user.id == user.id))
#             return (request.user.is_authenticated) and (request.user.id == user.id)
#         # if the user owns a channel he can do anything
#         elif user.id == request.user.id:
#             print("has_object_permission true: owner")
#             return True
#         # otherwise it is not allowed
#         else:
#             print("has_object_permission false")
#             return False

#     def get_user_for_obj(self, obj):
#         assert type(obj) is Episode
#         # if type(obj) is Channel:
#         #     return obj.user
#         return obj.channel.user


# class IsChannelOwnerOrReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         # return request.user.is_staff or (request.method in permissions.SAFE_METHODS)
#         # return Channel.objects.filter(user=request.user).exists()
#         return (
#             # GET, HEAD, OPTIONS are allowed for anyone
#             (request.method in permissions.SAFE_METHODS)
#             # POST is allowed only for authenticated users
#             or (request.method == "POST" and request.user.is_authenticated)
#             # PUT is only allowed for the users that own the channel
#             or (
#                 request.method == "PUT"
#                 and Channel.objects.does_user_own_any_channels(user_id=request.user.id)
#             )
#             or (
#                 request.method == "DELETE"
#                 and Channel.objects.does_user_own_any_channels(user_id=request.user.id)
#             )
#         )
