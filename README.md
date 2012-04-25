# Overview

This example shows how to create a secure, private RESTful API using [Django][django], [Tastypie][tastypie], and the [xAuth][xAuth] variant of [OAuth 1.0a](http://oauth.net/core/1.0a/), which can be deployed to [Heroku][heroku].

The API has two resources, `Users` and `Tasks` which are like simple TODO items.

### Motivation

I wanted to create a simple REST backend for a mobile client. I also wanted this API to be private, meaning that only clients I designate could access it. Finally, I wanted it to be easy to deploy or "Heroku-compatible".

I did a lot of research, and came to the conclusion that OAuth was the way to go for authentication and authorization. However, the full three-legged OAuth workflow seemed needlessly overcompliated. Then I recalled Twitter's [xAuth][xAuth]<sup>*</sup>, which allows client to obtain an access token and secret with a user name and password. This seemed like a much better fit for a mobile app.

---

\* xAuth is also used by [Instapaper's Full API](http://www.instapaper.com/api/full).

### Ingredients

1. [Tastypie][tastypie] (and [Django][django]) -- I feel like Tastypie gets REST right, and I like Django so this was an easy starting point. Also, Tastypie supports OAuth via the django-oauth-plus app (but not xAuth!).
1. [xAuth][xAuth] via my fork of [django-oauth-plus][django-oauth-plus] -- django-oauth-plus does not support xAuth, so I added support for it myself. Some inspiration was drawn from [django-piston-xauth](https://github.com/kennethreitz/django-piston-xauth).
1. [Heroku](http://www.heroku.com/) -- Heroku is the easiest way to deploy a Django app that I've found. It has some drawbacks, but it can't be beat for getting something up and running quickly.

# Demo

This app is already running at [http://django-api-example.herokuapp.com](http://django-api-example.herokuapp.com/). It includes an example user with read-only access. A few simple steps to query the API follow.

1. Install [`oauth-proxy`](https://github.com/mojodna/oauth-proxy). `oauth-proxy` makes is easy to use OAuth with `curl`.

1. Run the [`example/client.py script`](https://github.com/amrox/django-api-example/blob/master/example/client.py). It should generate an OAuth access token and secret:

	$ python client.py
	{'oauth_token_secret': 'WBGYYUjasZ2LFsQF', 'oauth_token': 'dac6e92dc42e42e685e39728cf6e523f'}
	GET http://django-api-example.herokuapp.com/api/v1/ -> {"tasks": {"list_endpoint": "/api/v1/tasks/", "schema": "/api/v1/tasks/schema/"}, "users": {"list_endpoint": "/api/v1/users/", "schema": "/api/v1/users/schema/"}}

1. Start `oauth-proxy` with the oauth_token and oauth_token_secret from the output of `client.py`:

	$ oauth-proxy --consumer-key=testconsumer --consumer-secret=secret --token=dac6e92dc42e42e685e39728cf6e523f --token-secret=WBGYYUjasZ2LFsQF
 
1. Get some data via `curl`:

	$ curl -i -x localhost:8001 http://django-api-example.herokuapp.com/api/v1/tasks/


# Deploy your own

1. Create a virtualenv and install requirments

	$ mkvirtualenv django-api-example
	$ pip install -r requirements.txt

1. Create a new app and add the remote.

	$ heroku apps:create <app name>	--stack=cedar
	
	$ git remote add heroku git@heroku.com:<app name>.git

1. Add a `DEPLOY_CONFIG`  variable to distinguish between local and production environments.

	$ heroku config:add DEPLOY_CONFIG=production
	
1. Push

	$ git push heroku master
		
1. Set up the database.

	$ heroku run django_api_example/manage.py syncdb

1. Set up initial data with the included test fixture. This creates two users, `admin` and `test`. The passwords are the same as the username. This is obviously absurdly insecure should be changed in production. The test fixture also creates a consumer with key `consumer` and secret `secret`. Again these should be changed. Finally it creates an `all` resource (a django-oauth-plus requirement) and sets up a `Basic` group that has read/write priveledges to `Tasks`.

	$ heroku run  django_api_example/manage.py loaddata django_api_example/fixtures/test_data.json

1. Edit [`example/client.py script`](https://github.com/amrox/django-api-example/blob/master/example/client.py), changing `consumer_key`, `consumer_secret` and `access_token_url` to the appropriate values. Run `example/client.py` to generate an access token and secret.

1. Start `oauth-proxy` with your consumer and access token information

	$ oauth-proxy --consumer-key=consumer --consumer-secret=secret --token=<access token> --token-secret=<access token secret>

1. Post some data

	curl -i -x localhost:8001 -X POST --data '{"text":"buy milk"}' -H "Content-Type: application/json" http://your-app.herokuapp.com/api/v1/tasks/

1. Verify it was created

	curl -i -x localhost:8001 http://django-api-example1.herokuapp.com/api/v1/tasks/




# License

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

[django]: https://www.djangoproject.com/ "Django"
[tastypie]: http://tastypieapi.org/ "Tastypie"
[xauth]: https://dev.twitter.com/docs/oauth/xauth "xAuth"
[django-oauth-plus]: https://bitbucket.org/amrox/django-oauth-plus "django-oauth-plus"
[heroku]: http://www.heroku.com/
