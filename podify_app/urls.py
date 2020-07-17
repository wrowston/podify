from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('creator', views.CreatorView)
router.register('episode', views.EpisodeView)
router.register('podcast', views.PodcastView)


urlpatterns = [
    path('', include(router.urls))
]
