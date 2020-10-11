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

* [Chapter 1 - Getting Django Set Up Using a Functional Test](Docs/Chapter1.md)
* [Chapter 2 - Extending our Functional Test Using the unittest Module](Docs/Chapter2.md)
* [Chapter 3 - Testing a Simple Home Page with Unit Tests](Docs/Chapter3.md)
* [Chapter 4 - What Are We Doing with All These Tests? (And, Refactoring)](Docs/Chapter4.md)
* [Chapter 5 - Saving User Input: Testing the Database](Docs/Chapter5.md)
* [Chapter 6 - Improving Functional Tests: Ensuring Isolation and Removing Voodoo Sleeps](Docs/Chapter6.md)
* [Chapter 7 - Working Incrementally](Docs/Chapter7.md)

# Part II - Web Development Sine Qua Nons

* [Chapter 8 - Prettification: Layout and Styling, and What to Test About It](Docs/Chapter8.md)
