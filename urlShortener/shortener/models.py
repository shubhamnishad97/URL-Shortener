from django.db import models

# Create your models here.
class shortenedUrl(models.Model):
    url = models.CharField(max_length=300)
    short =models.CharField(max_length=15,unique=True)

    def __str__(self):
        return str(self.url)