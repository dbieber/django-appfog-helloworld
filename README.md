# django-appfog-helloworld

You'll have your Django webapp up and running live on the internet with AppFog in a matter of minutes.

### Here's what you have to do.

1. [Start a project on AppFog.](#setting-up-appfog)
2. [Clone this repository.](#cloning-this-repository)
3. [Push to AppFog.](#pushing-to-appfog)

### Here's what comes with this repo.

It's a Django project that works out of the box (just download it and `python manage.py runserver`. If you have Django installed, it'll work!). It's already setup to serve static files. It's all ready to use MySQL or sqlite3. It ships with Bootstrap and jQuery. Django's admin app is enabled and ready to go. It has templates for 404 and 500 errors so you can quickly see how to get error handling working. And it has one app, named app_name, that demonstrates the core functionality of Django: models, views, templating, forms, and working with Django's admin app.

My hope is that it will work well both as start code and as reference code for how to get Django working quickly.

###### This template is great for quick and dirty websites. It's perfect for a hackathon or for prototyping an idea with friends. And it's a great template for getting started with [Django](https://www.djangoproject.com/), [Bootstrap](http://twitter.github.com/bootstrap/), and [jQuery](http://jquery.com/). But it's not production quality in two key respects, security and scalability. Keep that in mind as you start building.

##### Let's dive deeper into these three steps.

#### Setting up AppFog

Register for an account at [AppFog.com](http://appfog.com).

Create a new "Django Python" app. Host it on AWS. And give it a name. I called mine "helloworld-django". Let's say you call yours `name_of_app`.

 You'll want to set up the `af` command line utility to make deploying your site easier later. On Mac or Unix this is as simple as `gem install af`. Windows instructions are simple too, and are available in the "Update Source Code" tab of your app on AppFog.

(Optional) Make sure you have a MySQL database service provisioned. To do this, log in to AppFog, choose your app, and choose the "Services" tab. You can either bind an existing MySQL database service to your app or create a new one. If you don't have a MySQL database provisioned, the app we deploy in a moment will use sqlite3 as a fallback.

#### Cloning this repository

`git clone https://github.com/dbieber/django-appfog-helloworld.git`

The webapp is already all ready to be pushed to AppFog.

Before you go and push this website live, there are a few things you should do, all marked with `TODO` in the source code you just downloaded. These are the most important:

1. Set your `SECRET_KEY` in `settings.py`
3. Set up the `ADMINS` variable in `settings.py`
2. Set default admin account credentials in `views.py`
4. Always be aware of whether `DEBUG = True` or `DEBUG = False` in `settings.py`. This changes how errors are handled and you definitely want `DEBUG` set to false when your site is public.

Now you're ready to go live!

#### Pushing to AppFog

Be sure to either run `python manage.py collectstatic` or place all your static files your `static` directory before pushing.

Log in to AppFog with the command `af login`. (Find instructions for setting up the command line tool in the "Update Source Code" tab of your app on [AppFog.com](http://appfog.com).

From inside the `django-appfog-helloworld` directory (which, by the way, you are free to rename) run `af update name_of_app`.

That's it. Your site is live! You're already collecting email address of beta-testers. Huzzah!

### Testing Locally

To test locally, you'll need to [install Django](https://docs.djangoproject.com/en/dev/topics/install/).

To test your app locally, navigate to the `django-appfog-helloworld` directory containing `manage.py`:

`python manage.py runserver` runs your app locally. View it at `localhost:8000`.
`python manage.py syncdb` sets up your local database by default in a file called `dev.db`.
`python manage.py collectstatic` copies all your static files into your static files directory.
`python manage.py help` for more.
