from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField(default=1900)
    casting = models.CharField(max_length=255, blank=True)
    director = models.CharField(max_length=255, blank=True)
    producer = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, blank=True, null=True)
    movie_as_actor = models.ManyToManyField(Movie, related_name="actors", blank=True)
    movie_as_director = models.ManyToManyField(Movie, related_name="directors", blank=True)
    movie_as_producer = models.ManyToManyField(Movie, related_name="producers", blank=True)

    def __str__(self):
        return self.first_name
