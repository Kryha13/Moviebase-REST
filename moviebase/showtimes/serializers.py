from rest_framework import serializers
from showtimes.models import Cinema, Screening
from movielist.models import Movie, Person


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.SlugRelatedField(many=True, slug_field='title', queryset=Movie.objects.all())

    class Meta:
        model = Cinema
        fields = ('name', 'city', 'movies')

