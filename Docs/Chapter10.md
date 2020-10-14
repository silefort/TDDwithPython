# Chapter 10 - Getting to a Production-Ready Deployment

What’s wrong with our hacky deployment? Well, we can’t use the Django dev server for production; it’s not designed for “real-life” loads. We’ll use something called Guni‐ corn instead to run our Django code, and we’ll get Nginx to serve our static files

Our settings.py currently has DEBUG=True, and that’s strongly recommended against for production (you don’t want users staring at debug tracebacks of your code when your site errors, for example). We’ll also need to set ALLOWED_HOSTS for security

We want our site to start up automatically whenever the server reboots. For that we’ll write a Systemd config file

Finally, hardcoding port 8000 won’t let us run multiple sites on this server, so we’ll switch to using “unix sockets” to communicate between nginx and Django.

## Switching to Gunicorn

    $ ../virtualenv/bin/pip install gunicorn
    $ ../virtualenv/bin/gunicorn superlists.wsgi:application

The Django dev server will serve static files magically for you, Gunicorn doesn’t. Now is the time to tell Nginx to do it instead.

## Switching to Using Unix Sockets

When we want to serve both staging and live, we can’t have both servers trying to use port 8000. We could decide to allocate different ports, but that’s a bit arbitrary, and it would be dangerously easy to get it wrong and start the staging server on the live port, or vice versa.
A better solution is to use Unix domain sockets—they’re like files on disk, but can be used by Nginx and Gunicorn to talk to each other. We’ll put our sockets in /tmp.

### Nginx file:

    location / {
      proxy_set_header Host $host;
      proxy_pass http://unix:/tmp/superlists-staging.ottg.eu.socket;
    }

### Instal Gunicorn:

    $ ../virtualenv/bin/gunicorn --bind \
    unix:/tmp/superlists-staging.ottg.eu.socket superlists.wsgi:application

### Create a systemd service ( `/etc/systemd/system/gunicorn-superlists-staging.ottg.eu.service` )

		[Unit]
		Description=Gunicorn server for superlists-staging.ottg.eu

		[Service]
		Restart=on-failure
		User=elspeth
		WorkingDirectory=/home/elspeth/sites/superlists-staging.ottg.eu/source
		ExecStart=/home/elspeth/sites/superlists-staging.ottg.eu/virtualenv/bin/gunicorn \
		--bind unix:/tmp/superlists-staging.ottg.eu.socket \ superlists.wsgi:application

		[Install]
		WantedBy=multi-user.target
