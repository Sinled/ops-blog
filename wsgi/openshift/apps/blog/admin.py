from django.contrib import admin
from openshift.apps.blog.models import Blog
from openshift.apps.blog.models import PostType
from openshift.apps.blog.models import SiteUsers

admin.site.register(Blog)
admin.site.register(PostType)
admin.site.register(SiteUsers)
