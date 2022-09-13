from rest_framework import routers
from . import views

# app_name = "api"

router = routers.SimpleRouter(trailing_slash=True)

router.register(r'sobreviventes', views.SobreviventeViewSet,
                basename='sobreviventes')
 
router.register(r'itens', views.ItensViewSet,
                basename='itens')

                
router.register(r'inventario', views.InventarioViewSet,
                basename='inventario')

router.register(r'sinalizar', views.SinalizarViewSet,
                basename='sinalizar')

# router.register(r'negociar', views.NegociarViewSet,
#                 basename='negociar')
 
urlpatterns = []
urlpatterns += router.urls