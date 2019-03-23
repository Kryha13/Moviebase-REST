from django.db import models
from movielist.models import Person, Movie

# Create your models here.


class Cinema(models.Model):
    name = models.TextField(max_length=100)
    city = models.TextField(max_length=100)
    movies = models.ManyToManyField(Movie, through='Screening')


class Screening(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    date = models.DateTimeField()


