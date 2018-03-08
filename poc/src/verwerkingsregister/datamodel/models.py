from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _
from djchoices import DjangoChoices, ChoiceItem


class Organisatie(models.Model):
    naam = models.CharField(max_length=255)
    adres = models.TextField(blank=True)

    class Meta:
        verbose_name = _('organisatie')
        verbose_name_plural = _('organisaties')

    def __str__(self):
        return self.naam


class Doel(models.Model):
    naam = models.CharField(max_length=255)
    omschrijving = models.TextField(blank=True)

    class Meta:
        verbose_name = _('doel')
        verbose_name_plural = _('doelen')

    def __str__(self):
        return self.naam


class Grondslag(models.Model):
    omschrijving = models.TextField(blank=True)

    class Meta:
        verbose_name = _('grondslag')
        verbose_name_plural = _('grondslagen')

    def __str__(self):
        return '{}...'.format(self.omschrijving[0:50])


class Proces(models.Model):
    naam = models.CharField(max_length=300)
    verwerkings_verantwoordelijke = models.CharField(max_length=100)

    organisatie = models.ForeignKey(Organisatie, related_name='voert_uit', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('proces')
        verbose_name_plural = _('processen')

    def __str__(self):
        return self.naam


class ProcesStap(models.Model):
    naam = models.CharField(max_length=255)
    bewaartermijn = models.PositiveSmallIntegerField()

    proces = models.ForeignKey(Proces, related_name='bestaat_uit', on_delete=models.CASCADE)
    realiseert = models.ForeignKey(Doel, verbose_name=_('realiseert (doel)'), on_delete=models.CASCADE)
    gebaseerd_op = models.ManyToManyField(Grondslag, verbose_name=_('gebaseerd op (grondslag)'))

    class Meta:
        verbose_name = _('proces stap')
        verbose_name_plural = _('proces stappen')

    def __str__(self):
        return self.naam


class PrivacyClassificatie(DjangoChoices):
    open_data = ChoiceItem(label=_('Open data'))
    valt_onder_avg = ChoiceItem(label=_('Valt onder AVG'))
    overig = ChoiceItem(label=_('Overig'))


class DataObject(models.Model):
    naam = models.CharField(max_length=255)
    privacy_classificatie = models.CharField(max_length=100, choices=PrivacyClassificatie.choices, default=PrivacyClassificatie.overig)

    bronhouder = models.ForeignKey(Organisatie, verbose_name=_('bronhouder (organisatie)'), related_name='is_bronhouder_van', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('data object')
        verbose_name_plural = _('data objecten')

    def __str__(self):
        return self.naam


class DataElement(models.Model):
    naam = models.CharField(max_length=255)

    # TODO: Johan prefers this field on the ProcesStap, rather than on the DateElement side. This is too much work for now.
    process_stap = models.ManyToManyField(ProcesStap, related_name='mag_bewerken', blank=True)
    data_object = models.ForeignKey(DataObject, related_name='omvat', on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('data element')
        verbose_name_plural = _('data elementen')

    def __str__(self):
        return self.naam


class Applicatie(models.Model):
    naam = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('applicatie')
        verbose_name_plural = _('applicaties')

    def __str__(self):
        return self.naam


class RolName(DjangoChoices):
    gegevensontvanger = ChoiceItem(label=_('Gegevensontvanger'))
    gegevensaanbieder = ChoiceItem(label=_('Gegevensaanbieder'))
    gegevensverwerker = ChoiceItem(label=_('Gegevensverwerker'))
    eventontvanger = ChoiceItem(label=_('Eventontvanger'))
    eventaanbieder = ChoiceItem(label=_('Eventaanbieder'))
    eventverwerker = ChoiceItem(label=_('Eventverwerker'))


class Rol(models.Model):
    naam = models.CharField(max_length=255, choices=RolName.choices)

    wordt_vervuld_door_organisatie = models.ForeignKey(Organisatie, verbose_name=_('wordt vervuld door (organisatie)'), blank=True, null=True, on_delete=models.CASCADE)
    wordt_vervuld_door_applicatie = models.ForeignKey(Applicatie, verbose_name=_('wordt vervuld door (applicatie)'), blank=True, null=True, on_delete=models.CASCADE)
    heeft_betrekking_op = models.ForeignKey(ProcesStap, verbose_name=_('heeft betreking op (proces stap)'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('rol')
        verbose_name_plural = _('rollen')

    def __str__(self):
        return self.naam

    def clean(self):
        if self.wordt_vervuld_door_applicatie and self.wordt_vervuld_door_organisatie:
            raise ValidationError(_('Een rol moet vervuld worden door een applicatie of organisatie.'))

    @property
    def wordt_vervuld_door(self):
        return self.wordt_vervuld_door_applicatie or self.wordt_vervuld_door_organisatie


class Medewerker(models.Model):
    naam = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('medewerker')
        verbose_name_plural = _('medewerkers')

    def __str__(self):
        return self.naam


class MedewerkerRol(models.Model):
    naam = models.CharField(max_length=255)

    gedefinieerd_voor = models.ForeignKey(Applicatie, verbose_name=_('gedefinieerd voor (applicatie)'), on_delete=models.CASCADE)
    wordt_vervuld_door = models.ForeignKey(Medewerker, verbose_name=_('wordt vervuld door (medewerker)'), on_delete=models.CASCADE)
    is_geautoriseerd_voor = models.ForeignKey(DataObject, verbose_name=_('is geautoriseerd voor (data object)'), on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('medewerker rol')
        verbose_name_plural = _('medewerker rollen')

    def __str__(self):
        return self.naam


class Rule(ProcesStap):
    class Meta:
        proxy = True
        verbose_name = _('Regel')
        verbose_name_plural = _('Regels')

    @property
    def proces_stap(self):
        return self.naam