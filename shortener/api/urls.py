from .views import URLRetrieveView,URLCreateView
from django.conf.urls import url,include


urlpatterns = [
    url(r'^$',URLCreateView.as_view(),name='retrieve'),
	url(r'^(?P<short>[\w-]+)/$',URLRetrieveView.as_view(),name='create'),    
]