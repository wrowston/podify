from rest_framework import serializers
from .models import Creator, Episode, Podcast

# associations


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = "__all__"


class PodcastSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Podcast
        fields = "__all__"


class CreatorSerializer(serializers.ModelSerializer):
    podcasts = PodcastSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Creator
        fields = "__all__"
