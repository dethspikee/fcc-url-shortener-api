from django import forms
from django.core.exceptions import ValidationError
from .models import Url
class UrlForm(forms.Form):
    url = forms.CharField(label='URL to be shortened:' ,max_length=200)
    url.widget.attrs.update({
        'class': 'form-control',
        'id': 'inputPassword2'
    })

