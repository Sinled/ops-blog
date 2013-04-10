from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    url(r'^$', 'openshift.views.news', name='news'),
    url(r'^contacts/$', 'openshift.views.contacts', name='contacts'),

    url(r'^blog/', include('openshift.apps.blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
