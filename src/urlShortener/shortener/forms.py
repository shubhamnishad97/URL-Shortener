from django import forms
from .validators import valid_URL

class SubmitUrl(forms.Form):
    url = forms.CharField(label="Submit URL",validators=[valid_URL])