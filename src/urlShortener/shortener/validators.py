from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


# provides url validation
def valid_URL(value):
    url_validator = URLValidator()
    noHTTP = False
    totalInvalid = False
    try:
        url_validator(value)
    except:
        noHTTP=True
        newURL="http://"+value
        try:
            url_validator(newURL)
        except:
            totalInvalid=True
    if noHTTP==True and totalInvalid==True:
         raise ValidationError("Invalid URL, try again!")

    return value

