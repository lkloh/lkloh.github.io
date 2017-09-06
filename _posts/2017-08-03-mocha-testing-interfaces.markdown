---
layout: post
title:  "Different ways to write unit tests in Mocha"
date:   2017-08-03 01:57:45 -0700
---


Continuing from the [previous post](https://lkloh.github.io/2017/08/02/unit-testing-mocha.html) on unit testing in Mocha:
there are several types of [Mocha interfaces](https://mochajs.org/#interfaces)
to chose from.

## BDD (Behavior-driven development)

Apparently this is the recommended one,
because it lets you specify the desired behavior
and not implementation details,
as there may be many different solutions to arrive at the same desired behavior.
Here's the previous example on unit testing a function to determine if
a given year is a leap year in 
[BDD style](https://github.com/lkloh/javascriptPlayground/blob/master/mochaTestExample_aug2_2017/test_bdd.js).

Oh and since `describe` and `context` are aliases for each other,
if you use several layers of nesting,
it is considered good style to use `describe` for the outermost layer
and `context` for the inner one to seperate things more clearly.
Contrast [using `describe` for everything](https://github.com/lkloh/javascriptPlayground/blob/master/mochaTestExample_aug2_2017/test_good.js) that is not a test,
and [using both keywords](https://github.com/lkloh/javascriptPlayground/blob/master/mochaTestExample_aug2_2017/test_bdd.js) in nesting different sets of tests.

## TDD (Test-driven development)

General idea is to write the tests for expected behavior, 
then write the function that makes the tests pass.
Supposedly not as good as BDD because you
may be tempted to just get the tests to pass and be happy.
Doesn't force you to optimize for conciseness and design
as much as BDD does.

## Others

Haven't really used the others yet, but you can read about them 
[here](https://mochajs.org/#exports).
Seems like they would be fine for either BDD or TDD,
you can chose one or another based on syntax/compilation preferences.
