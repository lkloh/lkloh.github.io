---
layout: post
title:  "What is random enough?"
date:   2017-10-03
---

The [random library](https://docs.python.org/2/library/random.html) generates
pseudorandom numbers based on the basic function 
[random()](https://docs.python.org/2/library/random.html#random.random).
It uses the Mersenne Twister to generate random numbers,
which well enough for most uses cases, 
but NOT for security purposes as it is deterministic.

If you need something cryptographically secure,
you're supposed to use `os.urandom()` or `SystemRandom`,
which relies the OS to generate random numbers.
How "random" this is depends on the specific OS you are using.

