from rest_framework import serializers
from movies.models import MovieData


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None,
        use_url=True,
    )

    class Meta:
        model = MovieData
        fields = ['id', 'name', 'duration', 'rating', 'genre', 'image']