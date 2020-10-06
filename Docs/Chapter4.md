# Chapter 4 - What are we doing with all these tests ? ( And, Refactoring )

## Programming is like pulling a Bucket of water up from a Well

When the well isn’t too deep, and the bucket isn’t very full, it’s easy. And even lifting a full bucket is pretty easy at first. But after a while, you’re going to get tired. TDD is like having a ratchet that lets you save your progress, take a break, and make sure you never slip backwards
That way you don’t have to be smart all the time

One of the great things about TDD is that you never have to worry about forgetting what to do next—just rerun your tests and they will tell you what you need to work on

## Using Selenium to test User Interactions

## The "Don't test Constants" rule, and Templates to the Rescue

In general, one of the rules of unit testing is Don’t test constants, and testing HTML as text is a lot like testing a constant

Unit tests are really about testing logic, flow control, and configuration

## Refactoring to Use a Template

What we want to do now is make our view function return exactly the same HTML, but just using a different process

You need to register your app to Django adding it to the `settings.py` file under `INSTALLED_APPS` list
