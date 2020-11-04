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

## Install Django, Selenium and other tools

    (superlists) $ pip install "django<1.12" "selenium<4"
    (superlists) $ pip install litecli

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
* [Chapter 9 - Testing Deployment Using a Staging Site](Docs/Chapter9.md)
* [Chapter 10 - Getting to a Production-Ready Deployment](Docs/Chapter10.md)
* [Chapter 11 - Automating Deployment with Fabric](Docs/Chapter11.md)
* [Chapter 12 - Splitting Our Tests into Multiple Files, and a Generic Wait Helper](Docs/Chapter12.md)
* [Chapter 13 - Validation at the Database Layer](Docs/Chapter13.md)
* [Chapter 14 - A Simple Form](Docs/Chapter14.md)
* [Chapter 15 - More Advanced Forms](Docs/Chapter15.md)
* [Chapter 16 - Dipping Our Toes, Very Tentatively, into JavaScript](Docs/Chapter16.md)
* [Chapter 17 - Deploying Our New Code](Docs/Chapter17.md)

# Part III - More Advanced Topics in Testing

* [Chapter 18 - User Authentication, Spiking, and De-Spiking](Docs/Chapter18.md)
* [Chapter 19 - Using Mocks to Test External Dependencies or Reduce Duplication](Docs/Chapter19.md)
* [Chapter 20 - Test Fixtures and a Decorator for Explicit Waits](Docs/Chapter20.md)
* [Chapter 21 - Server-Side Debugging](Docs/Chapter21.md)
* [Chapter 22 - Finishing “My Lists”: Outside-In TDD](Docs/Chapter22.md)
