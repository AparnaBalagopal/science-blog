from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


def home(request):
    return render(request, 'blog/home.html', {})

def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
	return render(request, 'blog/contact.html', {})

