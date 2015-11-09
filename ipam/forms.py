from django import forms

from .models import SuperBlock

class NewSuperNet(forms.ModelForm):
    address_space = forms.CharField(label='address_space')
    region = forms.CharField(label='region', required=False)

    class Meta:
        model = SuperBlock
        fields = ('address_space', 'region',)
