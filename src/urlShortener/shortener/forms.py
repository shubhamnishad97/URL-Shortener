from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# provides url validation
def valid_URL(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL")
    return value


class SubmitUrl(forms.Form):
    url = forms.CharField(label="Submit URL",validators=[valid_URL])