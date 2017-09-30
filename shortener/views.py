from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpRequest,HttpResponse
from django.views import View
from .forms import SubmitUrl
from .models import shortenedUrl

# Create your views here.

def redirectView(request, shortcode=None ,*args ,**kwargs ):
    try:
        obj = shortenedUrl.objects.get(short=shortcode)
        obj.count+=1
        obj.save()
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
        context = {
            "title": "Submit URL",
            "form": form
        }
        if form.is_valid():
            current_url=form.cleaned_data.get('url')
            obj, created = shortenedUrl.objects.get_or_create(url=current_url)
            context={
                'title':'URL Shortened!',
                'object':obj,
                'created':created
            }
            if created:
                messages.add_message(request, messages.SUCCESS, 'Shortened URL created')
            else:
                messages.add_message(request, messages.INFO, 'Shortened URL already exists')


        return render(request, 'home.html',context)