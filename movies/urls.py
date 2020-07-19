from django.conf.urls import url, include
from rest_framework import routers
from .views import MoviesViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(r'movies', MoviesViewSet, basename='movies')
router.register(r'persons', PersonViewSet, basename='persons')

urlpatterns = [
    url(r'^', include(router.urls)),
]
