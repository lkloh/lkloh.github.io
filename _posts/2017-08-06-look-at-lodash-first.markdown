---
layout: post
title:  "Look at Lodash first"
date:   2017-08-05 01:57:45 -0700
---

Once I had to refactor a JavaScript function
some people were using.
Someone else had already wrote it,
and we wanted the code to do something like:

```
valIsDefined(``) = True;
valIsDefined(0) = True;
valIsDefined(42) = True;
valIsDefined(NaN) = False;
valIsDefined(null) = False;
valIsDefined(undefined) = False;
```

Problem was, the code didn't really need to be writte in the first place.
What should probably have been done was to go look for something like that in 
[Lodash](https://lodash.com/),
which is a well-known JavaScript library that implements
lots of commonly used functions,
such as checking if an object is defined,
or whether a number falls within a certain range, etc.

We could likely have used (https://www.npmjs.com/package/lodash.isundefined)
with a little negative,
instead of writing a brand new function.

Since JavaScript is so popular,
some multilingual people decided to translate it to 
[Python](https://github.com/dgilland/pydash) as well.
There's probably an analogy for most of the popular languages,
look it up before writing your own function to perform a popular action.


