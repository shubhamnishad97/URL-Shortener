from django.db import models
from django.conf import settings
import random
import string
from .validators import valid_URL
from django.core.urlresolvers import reverse

# thank stackoverflow for this
SIZE = getattr(settings,'SIZE',5)
MYURL = getattr(settings,'MYURL','http://127.0.0.1:8000')


def code_generator(size=SIZE,chars=string.ascii_letters+string.digits):
    new_code = ''
    for i in range(size):
         new_code += random.choice(chars)

    return new_code

def create_shortcode(instance,size=SIZE):
    new_code = code_generator(size=size)
    data = instance.__class__
    qs_exists = data.objects.filter(short=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code

class URLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs = super(URLManager, self).all(*args,**kwargs)
        qs.filter(active=True)
        return qs


# Create your models here.
class shortenedUrl(models.Model):
    url = models.CharField(max_length=300,validators=[valid_URL])
    short =models.CharField(max_length=SIZE,unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    count = models.IntegerField(default=0)

    objects=URLManager

    def save(self, *args,**kwargs):
        if self.short is None or self.short=='':
            self.short = create_shortcode(self)
        super(shortenedUrl,self).save(*args,**kwargs)

    def get_short_url(self):
        url_path = reverse("redirect",kwargs= {'shortcode':self.short})
        url_path = MYURL+url_path
        return url_path


    def __str__(self):
        return str(self.url)