# Chapter 7 - Working Incremently

The agile philosophy is that you learn more from solving problems in practice than in theory, especially when you confront your application with real users as soon as possible

we try to put a minimum viable application out there early, and let the design evolve gradually based on feedback from real-world usage.

So, let’s think about our minimum viable lists app, and what kind of design we’ll need to deliver it:
• We want each user to be able to store their own list—at least one, for now.
• A list is made up of several items, whose primary attribute is a bit of descriptive text.
• We need to save lists from one visit to the next. For now, we can give each user a unique URL for their list. Later on we may want some way of automatically rec‐ ognising users and showing them their lists.

To deliver the “for now” items, it sounds like we’re going to store lists and their items in a database. Each list will have a unique URL, and each list item will be a bit of descriptive text, associated with a particular list.

## YAGNI!

“YAGNI” (pronounced yag-knee), which stands for “You ain’t gonna need it!”

## REST (ish)

We have an idea of the data structure we want—the Model part of Model-View- Controller (MVC). What about the View and Controller parts? How should the user interact with Lists and their Items using a web browser?

REST suggests that we have a URL structure that matches our data structure, in this case lists and list items. Each list can have its own URL:
/lists/<list identifier>/

To create a brand new list, we’ll have a special URL that accepts POST requests:
/lists/new

To add a new item to an existing list, we’ll have a separate URL, to which we can send POST requests:
/lists/<list identifier>/add_item

## Implementing the New Design Incrementally Using TDD

At the top level, we’re going to use a combination of adding new functionality (by adding a new FT and writing new application code), and refactoring our application

At the unit test level, we’ll be adding new tests or modifying existing ones to test for the changes we want, and we’ll be able to similarly use the unit tests we don’t touch to help make sure we don’t break anything in the process.

## Iterating Towards the New Design

We don’t need to implement our new, shiny design in a single big bang. Let’s make small changes that take us from a working state to a working state, with our design guiding us gently at each stage.

## Taking a First, Self-Contained Step: One New URL

Deleting migrations is dangerous. We do need to do it now and again, because we don’t always get our models code right on the first go. But if you delete a migration that’s already been applied to a database somewhere, Django will be confused about what state it’s in, and how to apply future migrations. You should only do it when you’re sure the migration hasn’t been used. A good rule of thumb is that you should never delete or modify a migration that’s already been committed to your VCS.
