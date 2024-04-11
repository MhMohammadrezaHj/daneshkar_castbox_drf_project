from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("channels", views.ChannelsViewSet, basename="channel")

episodes_router = routers.NestedDefaultRouter(router, "channels", lookup="channel")
episodes_router.register("episodes", views.EpisodesViewSet, basename="channel-episodes")

comments_router = routers.NestedDefaultRouter(
    episodes_router,
    "episodes",
    lookup="episode",
)
comments_router.register("comments", views.CommentViewSet, basename="episode-comments")

comments_likes_router = routers.NestedDefaultRouter(
    comments_router,
    "comments",
    lookup="comment",
)
comments_likes_router.register(
    "likes", views.CommentLikeViewSet, basename="episode-comment-likes"
)


urlpatterns = (
    router.urls
    + episodes_router.urls
    + comments_router.urls
    + comments_likes_router.urls
)
