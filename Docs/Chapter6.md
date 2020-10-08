# Chapter 6 - Improving Functional Tests: Ensuring Isolation and Removing Voodoo Sleeps

## Ensuring Test Isolation in Functional Tests

Since Django 1.4 though, there’s a new class called LiveServerTestCase which can do this work for you. It will automatically create a test database (just like in a unit test run), and start up a development server for the functional tests to run against

## Testing "Best Practices" Applied in this Chapter

### Ensuring test isolation and managing global state
Different tests shouldn’t affect one another. This means we need to reset any permanent state at the end of each test. Django’s test runner helps us do this by creating a test database, which it wipes clean in between each test.

### Avoid “voodoo” sleeps
Whenever we need to wait for something to load, it’s always tempting to throw in a quick-and-dirty time.sleep. But the problem is that the length of time we wait is always a bit of a shot in the dark, either too short and vulnerable to spurious failures, or too long and it’ll slow down our test runs. Prefer a retry loop that polls our app and moves on as soon as possible.

### Don’t rely on Selenium’s implicit waits
Selenium does theoretically do some “implicit” waits, but the implementation varies between browsers, and at the time of writing was highly unreliable in the Selenium 3 Firefox driver. “Explicit is better than implict”, as the Zen of Python says, so prefer explicit waits.
