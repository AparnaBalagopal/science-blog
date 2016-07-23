from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
    
]