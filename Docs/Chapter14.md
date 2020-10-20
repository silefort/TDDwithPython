# Chapter 14 - A Simple Form

## Tips

### Thin views

If you find yourself looking at complex views, and having to write a lot of tests for them, it’s time to start thinking about whether that logic could be moved else‐ where: possibly to a form, like we’ve done here.
Another possible place would be a custom method on the model class. And— once the complexity of the app demands it—out of Django-specific files and into your own classes and functions, that capture your core business logic.

### Each test should test one thing

The heuristic is to be suspicious if there’s more than one assertion in a test. Sometimes two assertions are closely related, so they belong together. But often your first draft of a test ends up testing multiple behaviours, and it’s worth rewriting it as several tests. Helper functions can keep them from getting too bloated.
