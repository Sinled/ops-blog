from django.shortcuts import render
from blog_project.apps.blog.models import Blog


def news(request):
    blog_post_list = Blog.objects.all().order_by('-id')[:3]
    favorite_post_list = Blog.objects.filter(post_type__post_type='favorites').order_by('-id')[:3]
    popular_post_list = Blog.objects.filter(post_type__post_type='popular').order_by('-id')[:3]
    return render(request, "news.html", {"blog_list": blog_post_list,
                                         "blog_popular_post_list": popular_post_list,
                                         "blog_favorite_post_list": favorite_post_list})


def contacts(request):
    return render(request, "contacts.html")
