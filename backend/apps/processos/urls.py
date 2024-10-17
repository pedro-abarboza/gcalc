from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('reclamadas', ReclamadaViewSet)
router.register('reclamantes', ReclamanteViewSet)
router.register('processos', ProcessosViewSet)
router.register('andamentos', AndamentosViewSet)

urlpatterns = router.urls