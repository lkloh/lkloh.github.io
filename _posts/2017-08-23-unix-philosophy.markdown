---
layout: post
title:  "Unix Philosophy"
date:   2017-08-23
---

There's a long list [here](https://github.com/timoxley/best-practices)
on programming best practices.
The opening principle of that document is `never build large apps`.

The most important one in the entire document is probably:

```
write unit tests
``` 

If you don't remember the rest (there's a lot in that document!)
remember this one.
It encompasses all the others in one way or another.

It's corollary is `write testable code`,
meaning code should be written in testable, bite-size pieces.
It would be more robust as well if you've designed tests for all sorts of edge cases.

If the code can't be easily tested, then some refactoring is in order... so it is more testable

Your system should be designed defensively because you don't know how it would grow
before you built it...
meaning you need tests to throw all sorts of scenarios that could break something.

Try not the write classes unless necessary...
because its easier to test a pure function than a class.


