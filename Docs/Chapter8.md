# Chapter 8 - Prettification: Layout and Styling, and What to Test About It

In this chapter, we’ll cover some of the basics of styling, including integrating an HTML/CSS framework called Boot‐ strap. We’ll learn how static files work in Django, and what we need to do about test‐ ing them.

Most people will tell you you shouldn’t test aesthetics, and they’re right. It’s a bit like testing a constant, in that tests usually wouldn’t add any value.

## Prettification: Using a CSS Framework

## Django Template Inheritance

We can make the two tem‐ plates inherit from a common “superclass” template

## Static Files in Django
Django, and indeed any web server, needs to know two things to deal with static files:
1. How to tell when a URL request is for a static file, as opposed to for some HTML that’s going to be served via a view function
2. Where to find the static file the user wants

## Using Bootstrap Components to Improve the Look of the Site

### Jumbotron!

  $ python manage.py collectstatic

## Recap: On Testing Design and Layout
* The short answer is: you shouldn’t write tests for design and layout per se. It’s too much like testing a constant, and the tests you write are often brittle.
* With that said, the implementation of design and layout involves something quite tricky: CSS and static files. As a result, it is valuable to have some kind of minimal “smoke test” which checks that your static files and CSS are working. As we’ll see in the next chapter, it can help pick up problems when you deploy your code to production.
* Similarly, if a particular piece of styling required a lot of client-side JavaScript code to get it to work (dynamic resizing is one I’ve spent a bit of time on), you’ll definitely want some tests for that.
* Try to write the minimal tests that will give you confidence that your design and lay‐ out is working, without testing what it actually is. Aim to leave yourself in a position where you can freely make changes to the design and layout, without having to go back and adjust tests all the time.
