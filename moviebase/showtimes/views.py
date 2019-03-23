from django.shortcuts import render
from django.views import generic

from showtimes.models import Cinema, Screening
from showtimes.serializers import ScreeningSerializer, CinemaSerializer
from rest_framework import generics, filters


# Create your views here.

class CinemaListView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer


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


