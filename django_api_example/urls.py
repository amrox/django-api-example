from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from api.resources import UserResource, TaskResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(TaskResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_api_example.views.home', name='home'),
    # url(r'^django_api_example/', include('django_api_example.foo.urls')),

    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^oauth/', include('oauth_provider.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
