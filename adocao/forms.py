from django import forms
from .models import Adocao
from animais.models import Animal


class AdocaoForm(forms.ModelForm):
    class Meta:
        model = Adocao
        fields = '__all__'
