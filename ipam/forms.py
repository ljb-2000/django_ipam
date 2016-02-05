from django import forms

from .models import SuperBlock
from .models import Subnet

class NewSuperNet(forms.ModelForm):
    address_space = forms.CharField(label='address_space')
    region = forms.CharField(label='region', required=False)

    class Meta:
        model = SuperBlock
        fields = ('address_space', 'region')


class NewSubNet(forms.ModelForm):
    address_space = forms.CharField(label='address_space')
    vrf = forms.CharField(label='vrf', required=False)
    route_target = forms.CharField(label='route_target', required=False)
    vlan_id = forms.CharField(label='vlan_id', required=False)
    environment = forms.CharField(label='environment', required=False)
    region = forms.CharField(label='region', required=False)
    customer_name = forms.CharField(label='customer_name', required=False)
    super_block = forms.ModelChoiceField(queryset=SuperBlock.objects.all(), to_field_name=id)

    class Meta:
        model = Subnet
        fields = ('address_space',
                  'vrf',
                  'route_target',
                  'vlan_id',
                  'environment',
                  'region',
                  'customer_name',
                  'super_block')
