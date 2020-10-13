# Chapter 9 - Testing Deployment Using a Staging Site 

## As Always, Start with a Test

Let’s adapt our functional tests slightly so that it can be run against a staging site.

    $ STAGING_SERVER=superlists-staging.ottg.eu python manage.py test functional_tests
