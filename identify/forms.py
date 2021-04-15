import os.path

from django import forms
from django.conf import settings as django_settings
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.core.serializers import get_serializer_formats
from django.utils.translation import gettext_lazy as _

from .models import PokemonSpecies


class MultiFileInput(forms.FileInput):
    def render(self, name, value, attrs=None, **kwargs):
        attrs = attrs or {}
        attrs['multiple'] = 'multiple'
        return super().render(name, None, attrs=attrs, **kwargs)

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        if name in files:
            return [files.get(name)]
        return []


class ImportForm(forms.ModelForm):
    widgets = MultiFileInput

    class Meta:
        model = PokemonSpecies
        fields = '__all__'
