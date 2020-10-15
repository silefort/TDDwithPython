# Chapter 11 - Automating Deployment with Fabric

The usual setup is to have a file called fabfile.py, which will contain one or more func‐ tions that can later be invoked from a command-line tool called fab

    $ fab function_name:host=SERVER_ADDRESS

mkdir -p is a useful flavour of mkdir, which is better in two ways: it can create directories several levels deep, and it only creates them if necessary. So, mkdir - p /tmp/foo/bar will create the directory bar but also its parent directory foo if it needs to. It also won’t complain if bar already exists

Many commands start with a cd in order to set the current working directory. Fabric doesn’t have any state, so it doesn’t remember what directory you’re in from one run to the next

## Git Tag the Release

    $ git tag LIVE
    $ export TAG=$(date +DEPLOYED-%F/%H%M) # this generates a timestamp 
    $ echo $TAG # should show "DEPLOYED-" and then the timestamp
    $ git tag $TAG
    $ git push origin LIVE $TAG # pushes the tags up

    $ git log --graph --oneline --decorate


## Automated Deployments
###Fabric 
lets you run commands on servers from inside Python scripts. This is a great tool for automating server admin tasks.

### Idempotency
If your deployment script is deploying to existing servers, you need to design them so that they work against a fresh installation and against a server that’s already configured.

### Keep config files under source control
Make sure your only copy of a config file isn’t on the server! They are critical to your application, and should be under version control like anything else.

### Automating provisioning
Ultimately, everything should be automated, and that includes spinning up brand new servers and ensuring they have all the right software installed. This will involve interacting with the API of your hosting provider.

### Configuration management tools
Fabric is very flexible, but its logic is still based on scripting. More advanced tools take a more “declarative” approach, and can make your life even easier. Ansible and Vagrant are two worth checking out (see Appendix C), but there are many more (Chef, Puppet, Salt, Juju...).
