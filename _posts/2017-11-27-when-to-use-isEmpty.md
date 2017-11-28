---
layout: post
title:  "When to use isEmpty"
date:   2017-11-27
---

How often do you actually need to use stuff from lodash now, with ES6 out?

Probably not very often, since much of the stuff can be done with native ES6 functions.

`_.isEmpty(x)` could check whether `x` was an object with key-value pairs.
For example, we had
```
_.isEmpty(NaN) = true
_.isEmpty(null) = true
_.isEmpty(undefined) = true
_.isEmpty(0) = true
_.isEmpty(1) = true
_.isEmpty('') = true

_.isEmpty('tree') = false
_.isEmpty([1,2,3]) = false
_.isEmpty({a:1, b:2}) = false
_.isEmpty({a:undefined, b:undefined}) = false
```

But mostly, you'll find that just checking for whether
`x` is defined or `x.length` is defined should be enough for your use case.

If `x` could be a dict/undefined, checking for `x ? 'defined' : 'not defined` would give what you want.

If `x` is a string/array, checking for `x.length ? 'not empty' : 'empty'` also does the trick.

Better to use the above methods if possible, as it is more clear and concise.

Unless `x` could be either an array or a dict, then you need `_.isEmpty`.
Then you have a really badly written function that tries to be too many things, that produced `x`. 

