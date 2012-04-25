"""
The MIT License

Copyright (c) 2012 Andy Mroczkowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Example consumer. This is not recommended for production.
Instead, you'll want to create your own subclass of OAuthClient
or find one that works with your web framework.
"""

import oauth2 as oauth
import urllib
import urlparse

#############################################################################
# Get Access Token with xAuth
#############################################################################

# Basic Configuration.
# You'll probably need to change these.
consumer_key = 'consumer'
consumer_secret = 'secret'
host = 'django-api-example.herokuapp.com'
#host = 'localhost:8000'
username = 'test'
password = 'test'

access_token_url = 'http://%s/oauth/access_token/' % (host)

consumer = oauth.Consumer(consumer_key, consumer_secret)
client = oauth.Client(consumer)

# Set xAuth parameters
params = dict()
params['x_auth_username'] = username
params['x_auth_password'] = password
params['x_auth_mode'] = 'client_auth'

resp, token = client.request(access_token_url, method="POST",body=urllib.urlencode(params))

if resp.status / 100 != 2:
    print resp
    print token
    exit(1)
else:
    access_token = dict(urlparse.parse_qsl(token))
    print access_token

# Parse access token
token = oauth.Token(access_token['oauth_token'], access_token['oauth_token_secret'])

# and create a new client with that token
client = oauth.Client(consumer, token)

#############################################################################
# Access a protected URL using OAuth access token
#############################################################################


# Basic Configuration.
# You'll need to change these.
protected_url = 'http://%s/api/v1/tasks/' % (host)
protected_url_method = 'GET'

resp, content = client.request(protected_url, protected_url_method)
if resp.status / 100 != 2:
    print resp
print '%s %s ->\n %s' % (protected_url_method, protected_url, content)

