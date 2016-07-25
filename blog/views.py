from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def home(request):
    return render(request, 'blog/home.html', {})

def products(request):
    return render(request, 'blog/products.html', {})

def services(request):
    return render(request, 'blog/services.html', {})


def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
	return render(request, 'blog/contact.html', {})

