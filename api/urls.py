from rest_framework import routers
from . import views

app_name = "api"

router = routers.SimpleRouter(trailing_slash=True)

router.register(r'sobreviventes', views.SobreviventeViewSet,
                basename='sobreviventes')
 
router.register(r'itens', views.ItensViewSet,
                basename='itens')
 
urlpatterns = []
urlpatterns += router.urls