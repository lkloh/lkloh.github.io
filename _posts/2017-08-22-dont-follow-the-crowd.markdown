---
layout: post
title:  "Don't follow the crowd"
date:   2017-08-22 11:05:37 -0700
---

Obviously, you should not copy code for a homework assignment. 
You will get [caught](https://theory.stanford.edu/~aiken/moss/).

How about when developing a software product?
Then you're allowed to use anything you found on Stack Overflow/ elsewhere,
as long as you can get it to work.

But this article goes into mode detail about why [copying code](https://medium.freecodecamp.org/the-benefits-of-typing-instead-of-copying-54ed734ad849) you don't fully understand is bad.
Copying code leads to unexpected side effects if you don't know what it does.
Or the style doesn't fit in with the rest of the code base you copied it to.
Same for blindly following the way code for a similar functionality is written,
even if it was written by another team member. 
If you don't fully understand it,
you can't write effective unit tests for it.

As an example, suppose you have this test you want to copy:

```js
def test_multiply_by_seven(n):
	assert multiply_by_seven(n) == (7 * n)

def test_add_seven(n):
	assert add_seve(n) == (n + 7)
```

and we refactored them to

```js
def test_multiply_by_seven(n):
	assert_equal(multiply_by_seven(n), 7 * n)

def test_add_seven(n):
	assert_equal(add_seven(n), n + 7)

def assert_equal(actual, expected):
	actual == expected
```

And the tests still pass!

Problem with this now, is that the `assert` statement isn't being called at all.
Easy to gloss over because `assert_equal` looks so much like `assert`,
and all the unit tests passed.

We actually need

```js
def assert_equal(actual, expected):
	assert actual == expected
```

Lesson learnt: Get a test to fail first when doing any writing/refactoring,
then get it to pass. This is the best way to making sure the tests
can actually catch errors when they happen.







