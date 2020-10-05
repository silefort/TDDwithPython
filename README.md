# TDDwithPython

This Repo is my workplace to follow the book "Test-Driven Development with Python" by harry J.W. Percival

Code examples can be found here: https://github.com/hjwp/book-example/

## Requirements:

    $ brew install geckodriver 
    $ pip install --user virtualenvwrapper
    $ echo 'PATH=~/.local/bin:$PATH' >> ~/.custom_bash
    $ echo 'source virtualenvwrapper.sh' >> ~/.custom_bash

## Create a virtualenv

    $ mkvirtualenv --python=python3.8 superlists

## Activate your virtualenv

    $ workon superlists

## Check if your virtualenv is active

    (superlists) $ which python

## Deactivate your virtualenv

    (superlists) $ deactivate

## Install Django & Selenium

    (superlists) $ pip install "django<1.12" "selenium<4"

# Part I - The Basics of TDD & Django

[Chapter 1 - Getting Django Set Up Using a Functional Test](Docs/Chapter1.md)
