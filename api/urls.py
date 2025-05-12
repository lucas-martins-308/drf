from rest_framework.routers import DefaultRouter
from .views import TransacoesViewSet

router = DefaultRouter()
router.register('transacoes', TransacoesViewSet)
