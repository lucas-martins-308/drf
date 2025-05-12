from django.db import models

class Transacoes(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=12)
    tipo = models.BooleanField(verbose_name='Tipo Transação', help_text='0. Entrada | 1. Saída')
    categoria = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    data_transacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.valor)
    
    # QUERYSET
    