from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Movie, Person
from .serializers import MovieSerializer, PersonSerializer


class MoviesViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Movie.objects.all()

class PersonViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Person.objects.all()
