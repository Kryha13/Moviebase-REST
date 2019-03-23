from django.shortcuts import render
from django.views import generic

from showtimes.models import Cinema, Screening
from movielist.models import Movie
from showtimes.serializers import ScreeningSerializer, CinemaSerializer
from rest_framework import generics, filters
from datetime import datetime


# Create your views here.

class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    # def get_queryset(self):
    #     return Cinema.objects.filter(screening__date__gte=datetime.now())


class CinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


class ScreeningListView(generics.ListCreateAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    filter_backends = (filters.SearchFilter,)  ###
    search_fields = ('movie__title', )  ###


class ScreeningView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer


