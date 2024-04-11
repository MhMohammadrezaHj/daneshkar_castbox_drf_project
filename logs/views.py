from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from logs.models import SeenEpisode
from logs.serializers import SeenEpisodeSerializer


class SeenEpisodeViewSet(mixins.ListModelMixin, GenericViewSet):
    serializer_class = SeenEpisodeSerializer
    permission_classes = [IsAdminUser]
    queryset = SeenEpisode.objects.all()

    @action(detail=False, methods=["GET"], permission_classes=[IsAuthenticated])
    def me(self, request):
        user_id = request.user.id
        seen_episodes = SeenEpisode.objects.filter(user_id=user_id)
        serializer = SeenEpisodeSerializer(seen_episodes, many=True)
        return Response(serializer.data)
