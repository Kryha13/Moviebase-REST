from movielist.models import Movie
from movielist.serializers import MovieSerializer
from rest_framework import generics, filters


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.SearchFilter,)  ###
    search_fields = ('cinema__city',)  ###


class MovieView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
