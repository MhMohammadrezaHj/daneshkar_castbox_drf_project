from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import django_filters.rest_framework

from profiles.models import Channel


from ..contents.permissions import IsChannelOwnerPermission
from ..contents.serializers import ChannelSerializer, CreateChannelSerializer


# class ChannelsApiView(viewsets.ModelViewSet):
#     serializer_class = ChannelSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
#     permission_classes = [IsAuthenticated]
#     queryset = Channel.objects.all()

#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             return CreateChannelSerializer
#         return ChannelSerializer

#     @action(detail=False, methods=["GET", "POST"], permission_classes=[IsAuthenticated])
#     def me(self, request):
#         user_id = request.user.id
#         user_channels = Channel.objects.filter(user_id=user_id)
#         print(user_channels)
#         if not user_channels.exists():
#             return Response(
#                 {
#                     "Error": "You don't have any channels. You can create one if you want."
#                 }
#             )
#         if request.method == "GET":
#             serializer = ChannelSerializer(user_channels, many=True)
#             return Response(serializer.data)
#         elif request.method == "POST":
#             serializer = CreateChannelSerializer(
#                 data=request.data, context={"request": request}
#             )
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response(serializer.data)
