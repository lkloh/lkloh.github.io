---
type: post
title: "Pure functions vs Functions with Side Effects'
date: 2018-04-01
---

Modified from [here](https://softwareengineering.stackexchange.com/questions/40297/what-is-a-side-effect?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa).

## Idempotent functions - what's that

Making multiple identical requests to a function has the same effect as making one request.

Examples
* f(f(x)) = f(x)
* addZero(addZero(num)) = addZero(num)

Important in REST - if a request fails,
keep retrying until it succeeds. 

## What is a "side effect" in software engineering?

Modification of some state somewhere.

Examples:
* Changing the value of a variable
* Disabling a button

## Pure functions

No side effects (a.k.a. leave the state unchanged).

Output is determined only by the input,
which is why it is a good practice to write only pure functions for ease of testing.

A pure function must be idempotent.

## Idempotent vs Pure function

An idempotent function can cause idempotent side effects.
For example, given a function `delete(x)` that
only deletes `x` if it exists in the state,
calling `delete` has the side effect of removing `x` from the state. 



