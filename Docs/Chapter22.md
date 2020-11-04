# Chapter 22 - Finishing “My Lists”: Outside-In TDD

## The Alternative: “Inside-Out”

The alternative to “outside-in” is to work “inside-out”, which is the way most people intuitively work before they encounter TDD. After coming up with a design, the nat‐ ural inclination is sometimes to implement it starting with the innermost, lowest- level components first.

It feels comfortable because it means you’re never working on a bit of code that is dependent on something that hasn’t yet been implemented. Each bit of work on the inside is a solid foundation on which to build the next layer out.

But working inside-out like this also has some weaknesses.

## Why Prefer “Outside-In”?

One problem that can result is to build inner components that are more general or more capable than we actually need, which is a waste of time, and an added source of complexity for your project

Another common problem is that you create inner com‐ ponents with an API which is convenient for their own internal design, but which later turns out to be inappropriate for the calls your outer layers would like to make... worse still, you might end up with inner components which, you later realise, don’t actually solve the problem that your outer layers need solved.

In contrast, working outside-in allows you to use each layer to imagine the most con‐ venient API you could want from the layer beneath it. Let’s see it in action.
