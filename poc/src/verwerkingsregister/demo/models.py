from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from djchoices import DjangoChoices, ChoiceItem


class ZaakType(DjangoChoices):
    # Similar to Proces
    bouwvergunningsaanvraag = ChoiceItem(label=_('Bouwvergunningsaanvraag'))


class ZaakStatus(DjangoChoices):
    # Similar to ProcesStap
    nieuw = ChoiceItem(label=_('Nieuw'))
    in_behandeling = ChoiceItem(label=_('In behandeling'))
    afgewezen = ChoiceItem(label=_('Afgewezen'))
    toegewezen = ChoiceItem(label=_('Toegewezen'))


class Persoon(models.Model):
    achternaam = models.CharField(max_length=200)
    voornaam = models.CharField(max_length=200, blank=True)
    adres = models.TextField(blank=True)

    class Meta:
        verbose_name = _('persoon')
        verbose_name_plural = _('personen')

    def __str__(self):
        return '{}, {}'.format(self.achternaam, self.voornaam)


class VergunningsAanvraag(models.Model):
    aanvrager = models.ForeignKey(Persoon, on_delete=models.CASCADE)
    zaaktype = models.CharField(max_length=50, choices=ZaakType.choices)
    zaakstatus = models.CharField(max_length=50, choices=ZaakStatus.choices, default=ZaakStatus.nieuw)

    lokatie_plaats = models.CharField(max_length=100)
    lokatie_postcode = models.CharField(max_length=7)
    lokatie_huisnummer = models.CharField(max_length=10)
    lokatie_huisnummer_toevoeging = models.CharField(max_length=20, blank=True)

    onderwerp = models.CharField(max_length=200)
    toelichting = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('vergunningsaanvraag')
        verbose_name_plural = _('vergunningsaanvragen')
        ordering = ['-created']

    def get_lokatie_display(self):
        return '{} {} {}, {}'.format(
            self.lokatie_postcode,
            self.lokatie_huisnummer,
            self.lokatie_huisnummer_toevoeging,
            self.lokatie_plaats,
        )

    def save(self, *args, **kwargs):
        if self.pk and self.zaakstatus in [ZaakStatus.toegewezen, ZaakStatus.afgewezen]:
            self.completed = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)