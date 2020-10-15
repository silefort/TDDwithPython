# Chapter 12 - Splitting Our Tests into Multiple Files, and a Generic Wait Helper

## Skipping a Test

Use `@skip` before the test function

Whenever you submit a form with Keys.ENTER or click something that is going to cause a page to load, you probably want an explicit wait for your next assertion

## Tips on Organising Tests and Refactoring

### Use a tests folder
Just as you use multiple files to hold your application code, you should split your tests out into multiple files.
• For functional tests, group them into tests for a particular feature or user story.
• For unit tests, use a folder called tests, with a __init__.py.
• You probably want a separate test file for each tested source code file. For Django, that’s typically test_models.py, test_views.py, and test_forms.py.
• Have at least a placeholder test for every function and class.

### Don’t forget the “Refactor” in “Red, Green, Refactor”
The whole point of having tests is to allow you to refactor your code! Use them, and make your code (including your tests) as clean as you can.
Don’t refactor against failing tests
• In general!
• But the FT you’re currently working on doesn’t count.
• You can occasionally put a skip on a test which is testing something you haven’t written yet.
• More commonly, make a note of the refactor you want to do, finish what you’re working on, and do the refactor a little later, when you’re back to a working state.
• Don’t forget to remove any skips before you commit your code! You should always review your diffs line by line to catch things like this.

### Try a generic wait_for helper
Having specific helper methods that do explicit waits is great, and it helps to make your tests readable. But you’ll also often need an ad-hoc one-line assertion or Selenium interaction that you’ll want to add a wait to. self.wait_for does the job well for me, but you might find a slightly different pattern works for you.
