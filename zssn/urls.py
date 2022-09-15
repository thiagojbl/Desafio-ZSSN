from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
# from rest_framework import permissions
from rest_framework.documentation import include_docs_urls

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
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('doc', include_docs_urls(
    #     title='Documentation',
    #     authentication_classes=[],
    #     permission_classes=[])
    # ),
    
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
