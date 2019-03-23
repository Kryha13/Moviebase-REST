from rest_framework import serializers
from showtimes.models import Cinema, Screening
from movielist.models import Movie, Person
from datetime import datetime, timedelta


class CinemaSerializer(serializers.ModelSerializer):
    movies = serializers.SerializerMethodField()

    class Meta:
        model = Cinema
        fields = ('name', 'city', 'movies')

    def get_movies(self, cinema):

        movies = cinema.movies.filter(screening__date__lt=datetime.now() + timedelta(days=30),
                                      screening__date__gte=datetime.now())
        return [movie.title for movie in movies]


class ScreeningSerializer(serializers.ModelSerializer):
    cinema = serializers.SlugRelatedField(slug_field='name', queryset=Cinema.objects.all())
    movie = serializers.SlugRelatedField(slug_field='title', queryset=Movie.objects.all())

    class Meta:
        model = Screening
        fields = ('cinema', 'movie', 'date')


