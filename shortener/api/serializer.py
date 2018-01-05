from rest_framework import serializers
from shortener.models import shortenedUrl


class URLSerializer(serializers.ModelSerializer):
	class Meta:
		model = shortenedUrl
		fields = [
			'pk',
			'url',
			'short',
			'updated',
			'created',
			'active',
			'count',
		]
		read_only_fields = ['count','short']

	

	def validate_url(self,value):
		qs =  shortenedUrl.objects.filter(url__iexact=value)
		if qs.exists():
			for e in qs:
				raise serializers.ValidationError("Shortened URL already exists. "+"url:"+e.url+"  shortcode:"+e.short)

		return value	
