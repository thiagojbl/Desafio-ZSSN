from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
 
    path('', include_docs_urls(
        title='Documentation',
        authentication_classes=[],
        permission_classes=[])
    ),
]

