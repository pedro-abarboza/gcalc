from django.db import models
    

class Reclamantes(models.Model):

    nome = models.CharField("Nome", max_length=100)

    class Meta:
        verbose_name = "Reclamante"
        verbose_name_plural = "Reclamantes"

    def __str__(self):
        return self.nome