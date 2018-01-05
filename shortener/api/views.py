from rest_framework import generics
from shortener.models import shortenedUrl
from .serializer import URLSerializer

class URLRetrieveView(generics.RetrieveAPIView):
	pass
	lookup_field = 'short'
	serializer_class = URLSerializer
	queryset = shortenedUrl.objects.all()


class URLCreateView(generics.CreateAPIView):
	pass
	lookup_field = 'short'
	serializer_class = URLSerializer
	queryset = shortenedUrl.objects.all()