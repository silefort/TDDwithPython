# Chapter 13 - Validation at the Database Layer

## Model-Layer Validation

In a web app, there are two places you can do validation: on the client side (using JavaScript or HTML5 properties, as we’ll see later), and on the server side. The server side is “safer” because someone can always bypass the client side, whether it’s mali‐ ciously or due to some bug.

Similarly on the server side, in Django, there are two levels at which you can do vali‐ dation. One is at the model level, and the other is higher up at the forms level. I like to use the lower level whenever possible, partially because I’m a bit too fond of databases and database integrity rules, and partially because, again, it’s safer—you can some‐ times forget which form you use to validate input, but you’re always going to use the same database.

## Surfacing Model Validation Errors in the View

## On Database-Layer Validation

I always like to push my validation logic down as low as possible.

### Validation at the database layer is the ultimate guarantee of data integrity
It can ensure that, no matter how complex your code at the layers above gets, you have guarantees at the lowest level that your data is valid and consistent.

### But it comes at the expense of flexibility
This benefit doesn’t come for free! It’s now impossible, even temporarily, to have inconsistent data. Sometimes you might have a good reason for temporarily stor‐ ing data that breaks the rules rather than storing nothing at all. Perhaps you’re importing data from an external source in several stages, for example.

### And it’s not designed for user-friendliness
Trying to store invalid data will cause a nasty IntegrityError to come back from your database, and possibly the user will see a confusing 500 error page. As we’ll see in later chapters, forms-layer validation is designed with the user in mind, anticipating the kinds of helpful error messages we want to send them.
