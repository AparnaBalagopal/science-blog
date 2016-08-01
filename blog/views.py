from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from django.utils import timezone


def home(request):
    return render(request, 'blog/home.html', {})

def products(request):
    return render(request, 'blog/products.html', {})

def images(request):
    return render(request, 'blog/images.html', {})


def about(request):
    return render(request, 'blog/about.html', {})

def contact(request):
	return render(request, 'blog/contact.html', {})

def vegetables(request):
	return render(request, 'blog/vegetables.html', {})

def fruits(request):
	return render(request, 'blog/fruits.html', {})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog/home.html', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
