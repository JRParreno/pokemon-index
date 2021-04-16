from django.db import models
from django.contrib.auth.models import User


class PokemonTypes(models.Model):
    class Meta:
        verbose_name_plural = "Pokemon Types"

    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class PokemonSpecies(models.Model):
    class Meta:
        verbose_name_plural = "Pokemon Species"

    name = models.CharField(max_length=255, null=False, blank=False)
    evolution_level = models.PositiveSmallIntegerField(blank=True, null=True)
    next_evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True)
    pokemon_types = models.ManyToManyField(PokemonTypes)

    def show_types(self):
        return "\n".join([poke_type.name for poke_type in self.pokemon_types.all()])

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    class Meta:
        verbose_name_plural = "Pokemons"

    nickname = models.CharField(max_length=255)
    species = models.ForeignKey(PokemonSpecies, on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(default=1, blank=True, null=True)
    trainer = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname
