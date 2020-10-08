# Chapter 5 - Saving user Input: Testing the Database

We want to take the to-do item input from the user and send it to the server, so that we can save it somehow and display it back to her later

the point of TDD is to allow you to do one thing at a time, when you need to

Django’s CSRF protection involves placing a little auto-generated token into each generated form, to be able to identify POST requests as having come from the origi‐ nal site. So far our template has been pure HTML, and in this step we make the first use of Django’s template magic. To add the CSRF token we use a template tag, which has the curly-bracket/percent syntax, {% ... %}—famous for being the world’s most annoying two-key touch-typing combination

## Red/Green/Refactor and Triangulation
The unit-test/code cycle is sometimes taught as Red, Green, Refactor: • Start by writing a unit test which fails (Red).

• Write the simplest possible code to get it to pass (Green), even if that means cheating.
• Refactor to get to better code that makes more sense.

So what do we do during the Refactor stage? What justifies moving from an implementation where we “cheat” to one we’re happy with?

One methodology is eliminate duplication: if your test uses a magic constant (like the “1:” in front of our list item), and your application code also uses it, that counts as duplication, so it justifies refactoring. Removing the magic constant from the applica‐ tion code usually means you have to stop cheating.

I find that leaves things a little too vague, so I usually like to use a second technique, which is called triangulation: if your tests let you get away with writing “cheating” code that you’re not happy with, like returning a magic constant, write another test that forces you to write some better code. That’s what we’re doing when we extend the FT to check that we get a “2:” when inputting a second list item.

## The Django ORM and Our First Model

An Object-Relational Mapper (ORM) is a layer of abstraction for data stored in a data‐ base with tables, rows, and columns. It lets us work with databases using familiar object-oriented metaphors which work well with code. Classes map to database tables, attributes map to columns, and an individual instance of the class represents a row of data in the database.

Django comes with an excellent ORM, and writing a unit test that uses it is actually an excellent way of learning it, since it exercises code by specifying how we want it to work

In Django, the ORM’s job is to model the database, but there’s a second system that’s in charge of actually building the database called migrations. Its job is to give you the ability to add and remove tables and columns, based on changes you make to your models.py files

One way to think of it is as a version control system for your database

    $ python manage.py makemigrations # help us to build our first database migration

## Creating our production Database with migrate

Django creates a special test database for unit tests; it’s one of the magical things that Django’s TestCase does

To set up our “real” database, we need to create it. SQLite databases are just a file on disk, and you’ll see in settings.py that Django, by default, will just put it in a file called db.sqlite3 in the base project directory

ngo everything it needs to create the database, first via models.py and then when we created the migrations file. To actually apply it to creating a real data‐ base, we use another Django Swiss Army knife manage.py command, migrate:

    $ python manage.py migrate

Clean our Database:

    $ rm db.sqlite3
    $ python manage.py migrate --noinput

## Usefull TDD Concepts:

### Regression
When new code breaks some aspect of the application which used to work.

### Unexpected failure
When a test fails in a way we weren’t expecting. This either means that we’ve made a mistake in our tests, or that the tests have helped us find a regression, and we need to fix something in our code.

### Red/Green/Refactor
Another way of describing the TDD process. Write a test and see it fail (Red), write some code to get it to pass (Green), then Refactor to improve the implementation.

### Triangulation
Adding a test case with a new specific example for some existing code, to justify generalising the implementation (which may be a “cheat” until that point).

### Three strikes and refactor
A rule of thumb for when to remove duplication from code. When two pieces of code look very similar, it often pays to wait until you see a third use case, so that you’re more sure about what part of the code really is the common, re-usable part to refactor out.

### The scratchpad to-do list
A place to write down things that occur to us as we’re coding, so that we can fin‐ ish up what we’re doing and come back to them later.
