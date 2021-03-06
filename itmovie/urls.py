from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="ItMovie API",
      default_version='v1',
      description="UI API documentation",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="nicoalvarez.27@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
        name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),   
    url(r'^api/', include('rest_framework.urls')),
    url(r'^', include('movies.urls')),
]
