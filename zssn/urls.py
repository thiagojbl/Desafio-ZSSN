from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="API-ZSSN",
      default_version='v1',
      description="Rede Social de Sobrevivência Zumbi",
      terms_of_service="",
      contact=openapi.Contact(email="xxx@xxx.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),  
    path('', include_docs_urls(
        title='Documentation',
        authentication_classes=[],
        permission_classes=[])
    ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

