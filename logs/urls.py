from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("seen-episodes", views.SeenEpisodeViewSet, basename="seen-episodes")


urlpatterns = router.urls
