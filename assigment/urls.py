from django.conf.urls import patterns, include, url
from django.contrib import admin
from histogram import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assigment.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^histogram/(?P<filename>.*)/$',views.hcount)
)
