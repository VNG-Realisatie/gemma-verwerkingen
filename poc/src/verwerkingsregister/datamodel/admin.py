from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import (Applicatie, DataElement, DataObject, Doel, Grondslag,
                     Medewerker, MedewerkerRol, Organisatie, Proces,
                     ProcesStap, Rol)


@admin.register(Organisatie)
class OrganisatieAdmin(admin.ModelAdmin):
    list_display = ('identificatie', 'naam', )


@admin.register(Doel)
class DoelAdmin(admin.ModelAdmin):
    list_display = ('naam', )


@admin.register(Grondslag)
class GrondslagAdmin(admin.ModelAdmin):
    list_display = ('identificatie', 'get_omschrijving_display', )

    def get_omschrijving_display(self, obj):
        return '{}...'.format(obj.omschrijving[0:100])


@admin.register(Proces)
class ProcesAdmin(admin.ModelAdmin):
    list_display = ('identificatie', 'naam', 'verwerkings_verantwoordelijke', )
    list_filter = ('organisatie', )


@admin.register(ProcesStap)
class ProcesStapAdmin(admin.ModelAdmin):
    list_display = ('identificatie', 'naam', 'bewaartermijn', 'proces', 'realiseert', 'get_gebaseerd_op_display', )
    list_filter = ('proces__organisatie', )

    def get_gebaseerd_op_display(self, obj):
        return ', '.join(list(obj.gebaseerd_op.values_list('identificatie', flat=True)))


class DataElementInline(admin.TabularInline):
    model = DataElement


@admin.register(DataObject)
class DataObjectAdmin(admin.ModelAdmin):
    list_display = ('naam', )
    list_filter = ('organisatie', )
    inlines = (DataElementInline, )


@admin.register(Applicatie)
class ApplicatieAdmin(admin.ModelAdmin):
    list_display = ('identificatie', 'naam', )


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('naam', 'wordt_vervuld_door_organisatie', 'wordt_vervuld_door_applicatie', 'heeft_betrekking_op', )
    list_filter = ('heeft_betrekking_op', )


@admin.register(Medewerker)
class MedewerkerAdmin(admin.ModelAdmin):
    list_display = ('identificatie', 'naam', )


@admin.register(MedewerkerRol)
class MedewerkerRolAdmin(admin.ModelAdmin):
    list_display = ('naam', 'gedefinieerd_door', 'wordt_vervuld_door', 'is_geautoriseerd_voor', )
