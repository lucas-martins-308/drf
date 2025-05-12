from .models import Transacoes
from .serializer import TransacoesSerializer
from rest_framework import viewsets

class TransacoesViewSet(viewsets.ModelViewSet):
    queryset = Transacoes.objects.all()
    serializer_class = TransacoesSerializer
