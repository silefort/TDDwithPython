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
