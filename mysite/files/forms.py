from django import forms

from .models import Fls


class FlsForm(forms.ModelForm):
    class Meta:
        model = Fls
        fields = ('file',)



