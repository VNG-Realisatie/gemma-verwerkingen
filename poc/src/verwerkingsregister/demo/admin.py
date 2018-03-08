from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .models import (Persoon, VergunningsAanvraag)


@admin.register(Persoon)
class PersoonAdmin(admin.ModelAdmin):
    list_display = ('achternaam', 'voornaam')


@admin.register(VergunningsAanvraag)
class VergunningsAanvraagAdmin(admin.ModelAdmin):
    list_display = ('zaaktype', 'zaakstatus', 'aanvrager')
