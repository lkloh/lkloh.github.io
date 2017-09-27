---
layout: post
title:  "Python object representation"
date:   2017-09-26
---

According to the [python datamodel](https://docs.python.org/2/reference/datamodel.html), 
all data in Python is an object/relation between objects. 
In particular, _an object’s identity never changes once it has been created._
The `id()` function returns an integer representing the identity of an object
(it's unique address in memory).
But the value of certain objects can change.

For example given a list `a = [7, 8, 9]`
```
 -----
|  7  | <---- a (list) at 4320001280
 -----
|  8  |
 -----
|  9  |
 -----
```
it is always stored at address 4320001280
and currently has values `a[0] = 7, a[1] = 8, a[2] = 9`,
but after assignment 
```py
a[0] = 5
```
the representation in memory looks like
```
 -----
|  5  | <---- a (list) at 4320001280
 -----
|  8  |
 -----
|  9  |
 -----
```
so the value of `a` changed, though it's identity is still 4320001280.

The value of list a could change because lists in python are mutable.
Thus if we do something like
```py
a = [7, 8, 9]
b = a
a[0] = 5
```
then the value of `a` will be `[5, 8, 9]`.

And when we print `b`, because `b` is pointing
to the representation of `a` in memory, 
then we get
```py
b = [5, 8, 9]
```
as well.
This can be illustrated by verifying that `id(a) = 4320001280 = id(b)`.

But integers are immutable objects in python, so after doing
```py
x = 7
y = x
```
We see that `id(x) = 140243129881624 = id(y)`.
By now if we reassign `x`, since `x` is an immutable integer,
it gets assigned to a new location in memory.
Thus
`x = 8`
and then `id(x) = 140243129881600`.
And still we have `y` pointing to the old object `x` was assigned to,
so we still have `id(y) = 140243129881624` and `y = 7`.





