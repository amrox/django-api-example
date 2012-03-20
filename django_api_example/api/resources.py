from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authentication import OAuthAuthentication
from tastypie.authorization import DjangoAuthorization

from django.contrib.auth.models import User
from tasks.models import Task

class UserResource(ModelResource):
    tasks = fields.ToManyField('api.resources.TaskResource', 'task_set', related_name='user')

    class Meta:
        queryset = User.objects.all()
        resource_name = 'users'
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']
        authentication = OAuthAuthentication()
        authorization = DjangoAuthorization()

    #def apply_authorization_limits(self, request, object_list):
    #    return object_list.filter(self=request.user)

class TaskResource(ModelResource):
    user = fields.ToOneField(UserResource, 'user', full=False)

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'tasks'
        authentication = OAuthAuthentication()
        authorization = DjangoAuthorization()

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)

