from django.contrib import admin
from .models import PokemonTypes, PokemonSpecies, Pokemon
from django.contrib.admin import widgets
admin.site.site_header = 'Pokemon Admin'


class PokemonSpeciesAdmin(admin.ModelAdmin):
    list_display = ('name', 'show_types', 'evolution_level', 'next_evolution')
    list_per_page = 5  # No of records per page

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget'] = widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )

        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class PokemonTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_per_page = 5  # No of records per page


class PokemonsAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'species', 'level', 'trainer')
    list_per_page = 5  # No of records per page


admin.site.register(PokemonTypes, PokemonTypesAdmin)
admin.site.register(PokemonSpecies, PokemonSpeciesAdmin)
admin.site.register(Pokemon, PokemonsAdmin)
