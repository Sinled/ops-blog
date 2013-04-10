from django.contrib import admin
from blog_project.apps.blog.models import Blog
from blog_project.apps.blog.models import PostType
from blog_project.apps.blog.models import SiteUsers

admin.site.register(Blog)
admin.site.register(PostType)
admin.site.register(SiteUsers)
