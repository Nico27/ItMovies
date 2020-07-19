from rest_framework import serializers
from .models import Movie, Person


class MovieSerializer(serializers.ModelSerializer):
    director = serializers.SerializerMethodField()
    casting = serializers.SerializerMethodField()
    producer = serializers.SerializerMethodField()
    release_year = serializers.SerializerMethodField()

    def get_director(self, instance):
        return instance.directors.values()

    def get_casting(self, instance):
        return instance.actors.values()

    def get_producer(self, instance):
        return instance.producers.values()

    def get_release_year(self, instance):
        '''int2roman'''
        num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                   (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        roman = ''
        year = instance.release_year

        while year > 0:
            for i, r in num_map:
                while year >= i:
                    roman += r
                    year -= i

        return roman

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_year', 'casting', 'director', 'producer']

class PersonSerializer(serializers.ModelSerializer):
    movie_as_actor = MovieSerializer(many=True, write_only=True)
    movie_as_director = MovieSerializer(many=True)
    movie_as_producer = MovieSerializer(many=True)

    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'alias', 'movie_as_actor',
                  'movie_as_director', 'movie_as_producer']
