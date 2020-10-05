# Chapter 2 - Extending our Functional test Using the unittest Module

Functional Test == Acceptance Test == End-to-End Test = Black Box Test

When creating a new FT, we can write the comments first, to capture the key points of the User Story. Being human-readable, you could even share them with nonprogrammers, as a way of discussing the require‐ ments and features of your app

Tests are organised into classes which inherit from unittest.TestCase
Any method whose name starts with test is a test method, and will be run by the test runner
Nice descriptive names for our test methods are a good idea too.
setUp and tearDown are special methods which get run before and after each test
tearDown will run even if there’s an error during the test itself ( The only exception is if you have an exception inside setUp, then tearDown doesn’t run.)
self.fail just fails no matter what, producing the error message given. I’m using it as a reminder to finish the test
Finally, we have the if __name__ == '__main__' clause (if you’ve not seen it before, that’s how a Python script checks if it’s been executed from the command line, rather than just imported by another script)

## Useful TDD Concepts

User Story: A description of how the application will work from the point of view of the user. Used to structure a functional test.
Expected Failure: When a test fails in the way that we expected it to.
