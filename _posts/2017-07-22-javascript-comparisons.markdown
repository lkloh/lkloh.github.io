---
layout: post
title:  "Javascript: Use === and !=="
date:   2017-07-22 11:05:37 -0700
---

Javascript has three ways to 
[establish equality](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness),
two of which are well known:

## A == B

The best known, because it is used in lost of other languages.
Doesn't work well for JavaScript because it
converts A and B to a common type, then compares them.
Meaning that these are all true:
```js
0 == `0`
0 == 0
null == undefined
```

Since NaN represents the solution to an ill-behaved math problem (e.g. 1/0),
thus `NaN === NaN` returns false.

## A === B

Compares objects A and B for strict equality.
Meaning for `true` to be emitted, the objects must be of the same type,
and also be the same. Thus these are false:
```js
`0` === 0
null === undefined
```

and only this is true:
```js
0 === 0
```

It's considered good practice to use `===` equality, because:
1. Easier to predict the result of `A === B`
2. No type conversion is made, so faster evaluation


## Object.is(A, B)

Almost the same behavior as `A === B`, except that `Object.is(NaN, NaN)` is true.

Generally use `A === B` instead of `Object.is(A, B)` as it the syntax that other
people would recognize and expect. 

The only time you should use `Object.is` is if you want to mimic the way `Object.defineProperty()`
works for some reason, or when you want `Object.is(-0, +0)` to be false.










