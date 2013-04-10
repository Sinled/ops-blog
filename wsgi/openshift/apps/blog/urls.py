from django.conf.urls import patterns, url


urlpatterns = patterns('openshift.apps.blog.views',
    url(r'^$', 'blog', name='blog'),
    url(r'^blog_post/(?P<post_id>\d+)/$', 'blog_post', name='blog_post'),
)
