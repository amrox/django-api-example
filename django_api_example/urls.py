from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_api_example.views.home', name='home'),
    # url(r'^django_api_example/', include('django_api_example.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
