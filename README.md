# WIP

This is a work in progress.

# Overview

This example shows how to create a secure, private RESTful API using [Django][django], [Tastypie][tastypie], and the [xAuth][xAuth] variant of [OAuth 1.0a](http://oauth.net/core/1.0a/), which can be deployed to [Heroku](http://www.heroku.com/).

The API has two resources, `Users` and `Tasks`, which are like simple TODO items.

### Motivation

I set out to create a simple REST backend for a mobile client. This API should also private, meaning that only clients I designate could access it. Finally, I wanted it to be easy to deploy or "Heroku-compatible".

I did a lot of research, and came to the conclusion that OAuth was the way to go for authentication and authorization. However, the full three-legged OAuth workflow seemed needlessly overcompliated. Then I recalled Twitter's xAuth, which allows 

xAuth is also used by [Instapaper's Full API](http://www.instapaper.com/api/full)

### Ingredients

1. [Django][django] --
2. [Tastypie][tastypie] -- 
3. [xAuth][xAuth] via my fork of [django-oauth-plus][django-oauth-plus]  -- 

# Quick Start

This app is already running at [http://django-api-example.herokuapp.com](http://django-api-example.herokuapp.com/). It includes an example user with read-only access. A few simple steps to query the API follow.

1. Install [`oauth-proxy`](https://github.com/mojodna/oauth-proxy). `oauth-proxy` makes is easy to use OAuth with `curl`.

1. Run the [`example/client.py script`](https://github.com/amrox/django-api-example/blob/master/example/client.py). It should generate an OAuth access token and secret:

```
$ python client.py
{'oauth_token_secret': 'WBGYYUjasZ2LFsQF', 'oauth_token': 'dac6e92dc42e42e685e39728cf6e523f'}
GET http://django-api-example.herokuapp.com/api/v1/ -> {"tasks": {"list_endpoint": "/api/v1/tasks/", "schema": "/api/v1/tasks/schema/"}, "users": {"list_endpoint": "/api/v1/users/", "schema": "/api/v1/users/schema/"}}
```

1. Start `oauth-proxy` with the oauth_token and oauth_token_secret from the output of `client.py`:

```
$ oauth-proxy --consumer-key=testconsumer --consumer-secret=secret --token=dac6e92dc42e42e685e39728cf6e523f --token-secret=WBGYYUjasZ2LFsQF
```
 
1. Get some data via `curl`:

```
$ curl -i -x localhost:8001 http://django-api-example.herokuapp.com/api/v1/tasks/
```


# Step-by-step


1. Edit [`example/client.py script`](https://github.com/amrox/django-api-example/blob/master/example/client.py), changing `consumer_key`, `consumer_secret` and `access_token_url` to the appropriate values. Run `example\client.py` to generate an access token and secret.

1. Start `oauth-proxy` with your consumer and access otken information

1. Post some data

```
curl -i -x localhost:8001 -X POST --data '{"text":"buy milk"}' -H "Content-Type: application/json" http://your-app.herokuapp.com/api/v1/tasks/
```

# Deployment



## Heroku

Create a new app.

	$ heroku create:app <app name>	

Add a `DEPLOY_CONFIG`  variable to distinguish between local and production environments.

	$ heroku config:add DEPLOY_CONFIG=production

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
