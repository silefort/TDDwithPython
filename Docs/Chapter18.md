# Chapter 18 - User Authentication, Spiking, and De-Spiking

## Passwordless Auth

The concept is: just use email to verify someone’s identity. If you’re going to have a “forgot my password” feature, then you’re trusting email anyway, so why not just go the whole hog? Whenever someone wants to log in, we generate a unique URL for them to use, email it to them, and they then click through that to get into the site.
