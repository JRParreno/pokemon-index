from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib import admin
from .models import PokemonTypes, PokemonSpecies, Pokemons
from .forms import ImportForm
from django.contrib.admin import widgets
admin.site.site_header = 'Pokemon Admin'


class PokemonSpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_types', 'evolution_level', 'next_evolution')

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )

        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class PokemonTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(PokemonTypes, PokemonTypesAdmin)
admin.site.register(PokemonSpecies, PokemonSpeciesAdmin)
admin.site.register(Pokemons)
