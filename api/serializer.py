from .models import Transacoes
from rest_framework import serializers

class TransacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacoes
        fields = ['id', 'valor', 'tipo']