from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog, Category

# Create your views here.

def index(request):
    categories = Category.objects.all()
    posts_list = Blog.objects.all()
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context = {'categories': categories,
               'posts': posts,
               'range': range(posts.number+1, posts.paginator.num_pages)[:5]}
    return render(request, 'blog/index.html', context)

def view_post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/view_post.html', {'post': blog})

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts_list = Blog.objects.filter(category=category)[:]
    paginator = Paginator(posts_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    context = {'category': category,
               'posts': posts,
               'range': range(posts.number+1, posts.paginator.num_pages)[:5]}
    return render(request, 'blog/view_category.html', context)
