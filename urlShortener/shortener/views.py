from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest,HttpResponse
from .models import shortenedUrl

# Create your views here.

def redirectView(request, shortcode=None ,*args ,**kwargs ):
    try:
        obj = shortenedUrl.objects.get(short=shortcode)
        return HttpResponseRedirect(obj.url)

    except:
        return HttpResponse("URL Does not exist")
