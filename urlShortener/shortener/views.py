from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from .models import shortenedUrl

# Create your views here.

def redirectView(request, shortcode=None ,*args ,**kwargs ):
    try:
        obj = shortenedUrl.objects.get(short=shortcode)
        return HttpResponse("Hello {sc}".format(sc=obj.url))

    except:
        obj = shortenedUrl.objects.all().first()
        return HttpResponse("URL Does not exist")
