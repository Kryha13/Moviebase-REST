from faker import Faker
from random import randint
from movielist.models import Movie
from showtimes.models import Cinema, Screening
from django.core.management.base import BaseCommand


def cinemas():
    faker = Faker("pl_PL")
    movie_count = Movie.objects.all().count()
    for _ in range(3):
        cinema = Cinema.objects.create(name=faker.company(), city=faker.city())
        for _ in range(4):
            movie = Movie.objects.get(pk=randint(1, movie_count))
            Screening.objects.create(cinema=cinema, movie=movie, date=faker.date_time())


class Command(BaseCommand):
    def handle(self, *args, **options):
        cinemas()