---
layout: post
title:  "Generic libraries that check whether a value is truthy are useless"
date:   2017-08-01
---

Python's [operator library](https://docs.python.org/2/library/operator.html)
is useful when you want to pass in regular arithmetic operators
as an argument to another function.
I recently had to use it.

In the process, I discovered there's a handy function called as
`operator.truth(obj)` which takes in an object 
and returns `True` if the object is `True`, and `False` otherwise.
Meaning that `operator.truth(None) = False`, which is handy.

It would be handy if we could use it to 
verify that a variable which is supposed to hold an integers
is actually doing so, and isn't something like `1/0`, for instance.

Unfortunately, we have:
```python
import operator

not_an_integer = float('nan')
operator.truth(not_an_integer) = True
```

So not so helpful. There's lots of libraries to check whether
something is truthy lying around, but their edge cases differ in subtle ways
and you end up needing to implement it again.

One place where this could come in useful is when
we have a variable `x` to handle where `x` could be `None`, or
a valid value, such as a non-empty string.
Unfortunately, we could just as easily check whether `x is None` or not.
It's just easier this way.

I tried coding up [an example](https://github.com/lkloh/playground-for-python/blob/master/operator_library.py) using `operator.truth` to check for null values,
and it didn't work.
I still needed a specific case where I exlicitly checked 
whether a value was `None` or a `boolean`.

This example is simple:
create a dictionary with some fields describing a person,
and pass it into a function to transform all non-null fields of the dictionary into a string.
We use booleans to represent the gender of the person:
`True` for male and `False` for female,
I couldn't use `operator.truth` to test whether the value of the person's
gender was recorded, or it would cause problems as
`operator.truth(None) = False` and `operator.truth(False) = False`.
So if the gender is `False`,
then we want to transform the new dictionary's value to `female`,
but this would not get processed.

Of course, this could be solved with refactoring in the example provided,
but if I refactored everything I didn't like, I'll never get anything done.


