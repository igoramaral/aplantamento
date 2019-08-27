from django.db import models
from django.utils import timezone

# Create your models here.

class Planta(models.Model):
    # nome, data de plantio, numero de colheitas, data da ultima colheita
    nome = models.CharField(max_length=50)
    dataPlantio = models.DateTimeField()
    numColheitas = models.PositiveIntegerField(default=0)
    dataUltimaColheita = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Planta"
        verbose_name_plural = "Plantas"

class Medicao(models.Model):
    # planta correspondente, umidade, luz, temperatura ambiente, data medição
    planta = models.ForeignKey('Planta', on_delete=models.CASCADE, null=True)
    umidade = models.BooleanField()
    temperatura = models.FloatField()
    luz = models.BooleanField()
    dataMedicao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        data = timezone.localtime(self.dataMedicao).strftime("%d/%m/%y %H:%M")
        return "Medição de " + data

    class Meta:
        verbose_name = "Medição"
        verbose_name_plural = "Medições"

class Rega(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, null=True)
    dataRega = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        data = timezone.localtime(self.dataRega).strftime("%d/%m/%y %H:%M")
        return "Rega de " + data