from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r'^$',views.HomeView.as_view(),name='home'),
    url(r'^(?P<shortcode>[\w-]+)/',views.redirectView,name='redirect'),
]