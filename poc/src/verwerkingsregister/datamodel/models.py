from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Organisatie(models.Model):
    identificatie = models.CharField(max_length=12)
    naam = models.CharField(max_length=255)
    adres = models.TextField(blank=True)


class Doel(models.Model):
    naam = models.CharField(max_length=255)
    omschrijving = models.TextField(blank=True)


class Grondslag(models.Model):
    identificatie = models.CharField(max_length=12)
    omschrijving = models.TextField(blank=True)


class Proces(models.Model):
    identificatie = models.CharField(max_length=12)
    naam = models.CharField(max_length=300)
    verwerkings_verantwoordelijke = models.CharField(max_length=100)

    organisatie = models.ForeignKey(Organisatie, related_name='voert_uit', on_delete=models.CASCADE)


class ProcesStap(models.Model):
    identificatie = models.CharField(max_length=12)
    naam = models.CharField(max_length=255)
    bewaartermijn = models.PositiveSmallIntegerField()

    proces = models.ForeignKey(Proces, related_name='bestaat_uit', on_delete=models.CASCADE)
    realiseert = models.ForeignKey(Doel, on_delete=models.CASCADE)
    gebaseerd_op = models.ManyToManyField(Grondslag)


class DataObject(models.Model):
    naam = models.CharField(max_length=255)

    organisatie = models.ForeignKey(Organisatie, related_name='is_bronhouder_van', on_delete=models.CASCADE)


class DataElement(models.Model):
    naam = models.CharField(max_length=255)

    process_stap = models.ForeignKey(ProcesStap, related_name='mag_bewerken', on_delete=models.CASCADE)
    data_object = models.ForeignKey(DataObject, related_name='omvat', on_delete=models.CASCADE)


class Applicatie(models.Model):
    identificatie = models.CharField(max_length=12)
    naam = models.CharField(max_length=255)


class Rol(models.Model):
    naam = models.CharField(max_length=255)

    wordt_vervuld_door_organisatie = models.ForeignKey(Organisatie, null=True, on_delete=models.CASCADE)
    wordt_vervuld_door_applicatie = models.ForeignKey(Applicatie, null=True, on_delete=models.CASCADE)
    heeft_betrekking_op = models.ForeignKey(ProcesStap, on_delete=models.CASCADE)

    def clean(self):
        if self.wordt_vervuld_door_applicatie and self.wordt_vervuld_door_applicatie:
            raise ValidationError(_('Een rol moet vervuld worden door een applicatie, organisatie, of beide.'))


class Medewerker(models.Model):
    identificatie = models.CharField(max_length=12)
    naam = models.CharField(max_length=255)


class MedewerkerRol(models.Model):
    naam = models.CharField(max_length=255)

    gedefinieerd_door = models.ForeignKey(Applicatie, on_delete=models.CASCADE)
    wordt_vervuld_door = models.ForeignKey(Medewerker, on_delete=models.CASCADE)
    is_geautoriseerd_voor = models.ForeignKey(DataObject, on_delete=models.CASCADE)
