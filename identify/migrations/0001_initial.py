# Generated by Django 3.2 on 2021-04-14 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PokemonSpecies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('evolution_level', models.IntegerField()),
                ('next_evolution', models.CharField(max_length=255)),
                ('show_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identify.pokemontypes')),
            ],
        ),
        migrations.CreateModel(
            name='Pokemons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('level', models.IntegerField()),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='identify.pokemonspecies')),
                ('trainer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
