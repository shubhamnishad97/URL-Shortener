from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest,HttpResponse
from django.views import View
from .forms import SubmitUrl

from .models import shortenedUrl

# Create your views here.

def redirectView(request, shortcode=None ,*args ,**kwargs ):
    try:
        obj = shortenedUrl.objects.get(short=shortcode)
        return HttpResponseRedirect(obj.url)

    except:
        return HttpResponse("URL Does not exist")


class HomeView(View):
    def get(self,request,*args,**kwargs):
        form=SubmitUrl()
        context={
            "title":"Submit URL",
            "form": form
        }
        return render(request,'home.html',context)


    def post(self,request,*args,**kwargs):
        form = SubmitUrl(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

        context = {
            "title": "Submit URL",
            "form": form
        }
        return render(request, 'home.html',context)