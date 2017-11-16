---
layout: post
title:  "When to ship with bugs"
date:   2017-11-13
---

This post explains when to [ship buggy code](http://elliot.land/post/why-most-unit-testing-is-waste).

# No bugs allowed

Mission Critical stuff (e.g. if you write software to deploy rockets for NASA)

# Ok to have bugs

Web applications, even those with lots of users.
Facebook apparently does ship with bugs,
because they chose to ship quickly over making something perfect.
After all, this may fail sometimes on a really old/corrupted CPU:

```py
def add(a, b):
	return a + b
```

But writing a simple test to make sure it works is probably enough,
no need to stress test it extensively.
Or you'll spend all your time testing and no time writing stuff,
and make no money because you product stagnated in the meantime.
