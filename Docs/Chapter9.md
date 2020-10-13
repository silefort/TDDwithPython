# Chapter 9 - Testing Deployment Using a Staging Site 

## As Always, Start with a Test

Let’s adapt our functional tests slightly so that it can be run against a staging site.

    $ STAGING_SERVER=superlists-staging.ottg.eu python manage.py test functional_tests

Don’t use export to set the STAGING_SERVER environment vari‐ able; otherwise, all your subsequent test runs in that terminal will be against staging (and that can be very confusing if you’re not expecting it). Setting it explicitly inline each time you run the FTs is best.

We can separate out “deployment” into two tasks:
• Provisioning a new server to be able to host the code
• Deploying a new version of the code to an existing server

One rule of thumb for distinguishing provisioning from deploy‐ ment is that you tend to need root permissions for the former, but you don’t for the latter
