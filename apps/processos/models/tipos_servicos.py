from django.db import models
from apps.processos.models import Clientes

class TipoServicos(models.Model):

    descricao = models.CharField(verbose_name="Descrição", max_length=200,
                                 null=False, blank=False)
    
    cliente = models.ForeignKey(
        Clientes, on_delete=models.DO_NOTHING,
        verbose_name='Cliente',
        null=False, blank=False
    )

    valor = models.FloatField(verbose_name="Valor", null=True, blank=True)

    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipos de Serviço"

    def __str__(self):
        return self.descricao