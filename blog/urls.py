from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^products/$', views.products, name='products'),
    url(r'^services/$', views.services, name='services'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^vegetables/$', views.vegetables, name='vegetables'),
    url(r'^fruits/$', views.fruits, name='fruits'),
    url(r'^post/new/$', views.post_new, name='post_new'),
]