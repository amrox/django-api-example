# WIP

This is a work in progress.

# Overview

This example shows how to create a secure, private RESTful API using [Django](https://www.djangoproject.com/), [tastypie](https://github.com/toastdriven/django-tastypie), and the [xAuth](https://dev.twitter.com/docs/oauth/xauth) variant of [OAuth 1.0a](http://oauth.net/core/1.0a/), which can be deployed to [Heroku](http://www.heroku.com/).

The API has two resources, `Users` and `Tasks`, which are like simple TODO items.

### Motivation

I wanted to create a simple REST backend for a mobile client. This API should also private, meaning that only clients I designate could access it. Finally, I wanted it to be easy to deploy or "Heroku-compatible".

I did a lot of research, and came to the conclusion that OAuth was the way to go for authentication and authorization. However, the full three-legged OAuth workflow seemed needlessly overcompliated. Then I recalled Twitter's xAuth, which allows 

# Quick Start

This app is already running at [http://django-api-example.herokuapp.com](http://django-api-example.herokuapp.com/). To work 

1. 



# Step-by-step


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
