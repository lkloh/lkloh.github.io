---
layout: post
title:  "Median of a long running stream"
date:   2017-07-02
---

"What is the best way find the approximate median of a huge stream of numbers,
so large that they can't all fit into memory at the same time?"

The smart way to do this when the stream can fit into memory, is to
use a max heap and a min heap. 
That would give an efficient answer in `O(n log n)` time and `O(n)` space.
But now there's not enough space.

The answer to this needs you to remember that computers have a maximum 
number of digits they can represent.
Lets say 4 bytes to a number, meaning that numbers must fit within 32 bits. 
So the integers can only range from -2^31 to 2^31-1,
a.k.a. -2 147 483 648 to 2 147 483 647.
So that's a maximum of `2^32` possible digits.
Given that 2^10 = 1024 ~ 1000 = 1kb, therefore (2^10) * (2^10) * (2^10) * 4
would only be 4000kb, a.k.a. 4MB, which would fit into memory.

So the right way to do things is to keep track of the number of times
every possible integer in the stream was seen,
and also the number of integers seen so far.
Then when someone queries for the median, it would be fairly easy to 
compute the median in a reasonable amount of time.









