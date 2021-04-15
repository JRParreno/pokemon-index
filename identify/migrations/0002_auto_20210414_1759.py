# Generated by Django 3.2 on 2021-04-14 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identify', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemons',
            options={'verbose_name_plural': 'Pokemons'},
        ),
        migrations.AlterModelOptions(
            name='pokemonspecies',
            options={'verbose_name_plural': 'Pokemon Species'},
        ),
        migrations.AlterModelOptions(
            name='pokemontypes',
            options={'verbose_name_plural': 'Pokemon Types'},
        ),
        migrations.AlterField(
            model_name='pokemonspecies',
            name='next_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='identify.pokemonspecies'),
        ),
    ]