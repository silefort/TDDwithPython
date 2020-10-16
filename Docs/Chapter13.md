# Chapter 13 - Validation at the Database Layer

## Model-Layer Validation

In a web app, there are two places you can do validation: on the client side (using JavaScript or HTML5 properties, as we’ll see later), and on the server side. The server side is “safer” because someone can always bypass the client side, whether it’s mali‐ ciously or due to some bug.

Similarly on the server side, in Django, there are two levels at which you can do vali‐ dation. One is at the model level, and the other is higher up at the forms level. I like to use the lower level whenever possible, partially because I’m a bit too fond of databases and database integrity rules, and partially because, again, it’s safer—you can some‐ times forget which form you use to validate input, but you’re always going to use the same database.

## Surfacing Model Validation Errors in the View
