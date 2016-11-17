Directory Layout

    example/
        Just a top-level directory to hold your Django project.
        The name of this doesn't matter.

        manage.py
            Python script provided by Django for doing various things with your
            Django project, like running the development server.

        example/     
            This is where project-wide Python code goes.
            Its name is important: it is the name of the whole project.

            __init__.py
                This empty file makes this directory a Python package.

            settings.py
                This file is critical to Django.
                It is where global configuration options are placed.

            urls.py
                This file is critical to Django.
                It defines all the URLs for the site, and maps them to bits
                of code called "views" which are run to process HTTP requests
                and generate HTTP responses.
                This project-wide `urls.py` should really just include URLs
                from any installed Django apps, to keep things tidy.

            wsgi.py
                This file is used to deploy your Django project on a WSGI
                server. WSGI is the traditional way to serve Python web apps.

        home/
            This directory is an example of a Django app that is included in
            the same repo with a Django project.
            This particular example app just shows the index or "home" page.

            __init__.py
                This empty file makes this directory a Python package.

            urls.py
                This is where you should put all the URLs for the home app,
                instead of in the top-level `urls.py`.

            admin.py
                This is where you can customize Django's builtin admin
                application, which is a quick and dirty way of working with
                the database tables your Django project knows about.
    
            apps.py

            migrations/
                In addition to the customary __init__.py, each file here
                describes a "migration" which automates changes to database
                tables, enabling upgrades between versions of the project.
            
            models.py
                This is the conventional place where a Django app will put
                definitions of "Django models" which define database tables
                together with Python code for working on those tables.

            tests.py
                This is a conventional place to put a few "unit tests" for
                this Django app. A unit test is just a bit of code which 
                tries out one piece (or "unit") of code, checks its behavior,
                and complains if the behavior is wrong.
        
            views.py
                This is a conventional place to put a few "views" for this
                Django app. In Django, a view is a function or class which
                runs to process an HTTP request and make an HTTP response.

                


Reproducing this Example Project
--------------------------------

First, a few commands (assume `vex` is installed to keep this simple)

    vex -m example
    pip install django
    django-admin startproject example
    ./manage.py migrate
    ./manage.py runserver
    ./manage.py startapp home
    git init
    git add .
    git commit -m "Django boilerplate"

Then you would start making code changes.

- Edit `example/settings.py` to add `"home"` to the `INSTALLED_APPS` list.

- Add an include() line to `example/urls.py` to bring in all the URLs from the
  `home` app.

- Add any views you need to `home/views.py`.

- Add routes which map to your views in `home/urls.py`. (These are included
  from `exchange/urls.py`.)

- Add any templates your views need to TODO

- Add any model definitions your views needed in `home/models.py`.
  Then run `./manage.py makemigrations home` to create migration files for it.

- Edit `example/settings.py` to specify a real database configuration.


Blah
----

- Run `./manage.py migrate` to run the migrations against your database.

- `./manage.py createsuperuser`
