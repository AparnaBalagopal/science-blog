from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^products/$', views.products, name='products'),
    url(r'^crops/$', views.crops, name='crops'),
    url(r'^images/$', views.images, name='images'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^vegetables/$', views.vegetables, name='vegetables'),
    url(r'^fruits/$', views.fruits, name='fruits'),
    url(r'^spices/$', views.spices, name='spices'),
    url(r'^tubers/$', views.tubers, name='tubers'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]