from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# provides url validation
def valid_URL(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL, try again!, maybe http is missing")
        
    return value

