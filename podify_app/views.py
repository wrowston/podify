from .serializers import CreatorSerializer, EpisodeSerializer, PodcastSerializer
from .models import Creator, Episode, Podcast
from rest_framework import viewsets

# Create your views here.


class CreatorView(viewsets.ModelViewSet):
    # the data we're looking at
    queryset = Creator.objects.all()
    # how we will see the data
    serializer_class = CreatorSerializer


class EpisodeView(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class PodcastView(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
