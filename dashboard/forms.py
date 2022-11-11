from django import forms
from django.utils.translation import gettext_lazy as _
from landing.models import OldageHome


class AddOldageHomeForm(forms.ModelForm):
    class Meta:
        model = OldageHome
        fields = ['name', 'logo', 'phone', 'email', 'address', 'description', 'license_no', 'webaddress']
        labels = {
            'webaddress': _('Web Address'),
        }