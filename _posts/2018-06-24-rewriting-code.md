---
type: post
title: "Rewriting a codebase"
date: 2018-06-24
---

[Joel thinks that you should almost never rewrite a codebase](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/).
Even if the implementation looks like a mess with conditional `if`s for edge cases everywhere.
It's been tested in the wild.

The rewrite is untested, and you probably won't be able to incorporate all the tiny bug fixes
that made you want to rewrite the old codebase,
because there probably aren't tests for all of them.

By throwing the old code away, you're undoing years of collected bug fixes and programming work,
and also wasting money by rewriting code that already exists.

I try to read this when I have to make changes to a codebase dating to 2012.

