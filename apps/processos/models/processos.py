from django.db import models
from apps.processos.models import Reclamadas, Reclamantes
    
    
class Processos(models.Model):

    n_processo = models.CharField("N.Processo", max_length=26)
    reclamada = models.ForeignKey(Reclamadas, verbose_name="Reclamada", on_delete=models.PROTECT)
    reclamante = models.ForeignKey(Reclamantes, verbose_name="Reclamante", on_delete=models.PROTECT)
    dt_ajuizamento = models.DateField(
        "D.Ajuizamento", auto_now=False, auto_now_add=False
    )
    formato = models.CharField("Formato", max_length=50, null=True, blank=True)
    dt_ult_atualizacao = models.DateField(
        "Ultima Atualização", auto_now=False, auto_now_add=False, null=True, blank=True
    )
    dt_ult_verificacao = models.DateField(
        "Ultima Verificação", auto_now=False, auto_now_add=False, null=True, blank=True
    )

    class Meta:
        verbose_name = "Processo"
        verbose_name_plural = "Processos"

    def __str__(self):
        return self.n_processo