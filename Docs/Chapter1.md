# Chapter 1 - Getting Django Set Up Using a Functional Test

The Testing Goat is the unofficial mascot of TDD in the Python testing community
In TDD the first step is always the same: write a test

## Write your first test ( in `functionnal_tests.py` )

## Getting Django Up & Running

    $ django-admin.py startproject superlists

That will create a folder called superlists, and a set of files and subfolders inside it

* `superlists/superlists` folder is for stuff that applies to the whole project - like `settings.py`
* `manage.py` is Django's Swiss Army knife, and one of the things it can do is run a development server

## Run a development server

    $ cd superlists
    $ python manage.py runserver
