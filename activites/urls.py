from django.contrib import admin
from django.urls import path, include
from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("subscriptions", views.SubscribeViewSet, basename="subscriptions")
router.register("playlists", views.PlayListViewSet, basename="playlists")

playlists_router = routers.NestedDefaultRouter(router, "playlists", lookup="playlist")
playlists_router.register("items", views.PlayListItemViewSet, basename="playlist-items")

urlpatterns = router.urls + playlists_router.urls
