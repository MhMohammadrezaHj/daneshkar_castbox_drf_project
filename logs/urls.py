from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("seen-episodes", views.SeenEpisodeViewSet, basename="seen-episodes")
router.register("seen-channels", views.SeenChannelViewSet, basename="seen-channels")


urlpatterns = router.urls
