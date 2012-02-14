#from django import http

# adapted from http://djangosnippets.org/snippets/2472/

class CloudMiddleware(object):
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_PROTO' in request.META:
            if request.META['HTTP_X_FORWARDED_PROTO'] == 'https':
                request.is_secure = lambda: True
        return None



