# Chapter 11 - Automating Deployment with Fabric

The usual setup is to have a file called fabfile.py, which will contain one or more func‐ tions that can later be invoked from a command-line tool called fab

    $ fab function_name:host=SERVER_ADDRESS

mkdir -p is a useful flavour of mkdir, which is better in two ways: it can create directories several levels deep, and it only creates them if necessary. So, mkdir - p /tmp/foo/bar will create the directory bar but also its parent directory foo if it needs to. It also won’t complain if bar already exists

Many commands start with a cd in order to set the current working directory. Fabric doesn’t have any state, so it doesn’t remember what directory you’re in from one run to the next


