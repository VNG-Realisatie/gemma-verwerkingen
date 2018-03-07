from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from .models import (Applicatie, DataElement, DataObject, Doel, Grondslag,
                     Medewerker, MedewerkerRol, Organisatie, Proces,
                     ProcesStap, Rol, Rule)


@admin.register(Organisatie)
class OrganisatieAdmin(admin.ModelAdmin):
    list_display = ('naam', )


@admin.register(Doel)
class DoelAdmin(admin.ModelAdmin):
    list_display = ('naam', )


@admin.register(Grondslag)
class GrondslagAdmin(admin.ModelAdmin):
    list_display = ('get_omschrijving_display', )

    def get_omschrijving_display(self, obj):
        return '{}...'.format(obj.omschrijving[0:100])


@admin.register(Proces)
class ProcesAdmin(admin.ModelAdmin):
    list_display = ('naam', 'verwerkings_verantwoordelijke', )
    list_filter = ('organisatie', )


@admin.register(ProcesStap)
class ProcesStapAdmin(admin.ModelAdmin):
    list_display = ('pk', 'naam', 'bewaartermijn', 'proces', 'realiseert', 'get_gebaseerd_op_display', )
    list_filter = ('proces__organisatie', )

    def get_gebaseerd_op_display(self, obj):
        return '<br>'.join([str(o) for o in obj.gebaseerd_op.all()])
    get_gebaseerd_op_display.allow_tags = True
    get_gebaseerd_op_display.short_description = _('gebaseerd op')


class DataElementInline(admin.TabularInline):
    model = DataElement
    extra = 0
    # filter_horizontal = ('process_stap', )


@admin.register(DataObject)
class DataObjectAdmin(admin.ModelAdmin):
    list_display = ('naam', 'privacy_classificatie')
    list_filter = ('bronhouder', )
    inlines = (DataElementInline, )


@admin.register(Applicatie)
class ApplicatieAdmin(admin.ModelAdmin):
    list_display = ('naam', )


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('naam', 'wordt_vervuld_door_organisatie', 'wordt_vervuld_door_applicatie', 'heeft_betrekking_op', )
    list_filter = ('heeft_betrekking_op', )


@admin.register(Medewerker)
class MedewerkerAdmin(admin.ModelAdmin):
    list_display = ('naam', )


@admin.register(MedewerkerRol)
class MedewerkerRolAdmin(admin.ModelAdmin):
    list_display = ('naam', 'gedefinieerd_voor', 'wordt_vervuld_door', 'is_geautoriseerd_voor', )


@admin.register(Rule)
class OverviewAdmin(ProcesStapAdmin):
    list_display = (
        'pk', 'proces', 'proces_stap', 'get_organisaties_display',
        'get_data_objecten_display',
    )

    def get_data_objecten_display(self, obj):
        # TODO: A structure is build based on names which is very error prone but serves our purpose for now.
        data_objecten = {}
        for data_element in obj.mag_bewerken.all():
            data_object = str(data_element.data_object)
            if data_object not in data_objecten:
                data_objecten[data_object] = []
            data_objecten[data_object].append(str(data_element))
        return mark_safe('<br>'.join(['{}: <ul><li>{}</li></ul>'.format(k, '</li><li>'.join(v)) for k, v in data_objecten.items()]))
    get_data_objecten_display.allow_tags = True
    # TODO: Fix this name in data model.
    get_data_objecten_display.short_description = _('mag verwerken')

    def get_organisaties_display(self, obj):
        return mark_safe('<br>'.join(
            ['{} ({})'.format(str(rol.wordt_vervuld_door), rol.naam) for rol in obj.rol_set.all()]
        ))
    get_organisaties_display.allow_tags = True
    get_organisaties_display.short_description = _('organisaties')