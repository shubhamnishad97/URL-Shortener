from django.db import models
import random
import string

def code_generator(size=10,chars=string.ascii_lowercase+string.digits+string.ascii_uppercase):
    new_code = ''
    for i in range(size):
         new_code += random.choice(chars)

    return new_code

def create_shortcode(instance,size=10):
    new_code = code_generator(size=size)
    data = instance.__class__
    qs_exists = data.objects.filter(short=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code

# Create your models here.
class shortenedUrl(models.Model):
    url = models.CharField(max_length=300)
    short =models.CharField(max_length=15,unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args,**kwargs):
        if self.short is None or self.short=='':
            self.short = create_shortcode(self)
        super(shortenedUrl,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.url)