from django.contrib import admin

# Register your models here.

from .models import Person, Movie


admin.site.register(Person)
admin.site.register(Movie)