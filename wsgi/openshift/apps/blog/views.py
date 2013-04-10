from django.shortcuts import render, get_object_or_404
from blog_project.apps.blog.models import Blog


def blog_post(request, post_id):
    # try:
        # blog_post_item = Blog.objects.get(id=post_id)
    # except blog_post_item.DoesNotExist:
        # raise Http404
    blog_post_item = get_object_or_404(Blog, id=post_id)
    print blog_post_item
    return render(request, "blog_post.html", {"blog_item": blog_post_item})


def blog(request):
    blog_post_list = Blog.objects.all()
    return render(request, "blog.html", {"blog_list": blog_post_list})
