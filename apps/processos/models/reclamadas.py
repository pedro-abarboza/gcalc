from django.db import models


class Reclamadas(models.Model):

    nome = models.CharField("Nome", max_length=100)

    class Meta:
        verbose_name = "Reclamada"
        verbose_name_plural = "Reclamadas"

    def __str__(self):
        return self.nome