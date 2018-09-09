---
type: post
title: "Terminating if...elseIf constructs with an else clause
date: 2018-09-08
---

Summarized from [here](https://stackoverflow.com/questions/35053371/what-is-the-benefit-of-terminating-if-else-if-constructs-with-an-else-clause).

Given this bit of code,
```py
if x == True:
  return `The user exists`
elif x == False:
  return `The user does not exist`
```

one would think that we should just change it to
```py
if x == True:
  return `The user exists`
else:
  return `The user does not exist`
```

and it would always return some sort of string.

But in certain scenarios, it would be better to write

```py
if x == True:
  return `The user exists`
elif x == False:
  return `The user does not exist`
else:
  raise Exception('The variable x (%r) should be a boolean, but something went wrong.' % x)
```

in order to

1. Communicate that the author has considered the case when neither 
  `x == True` nor `x == False` are true.
2. Handle unlikely scenarios in mission critical software,
  to catch the case in which `x` has been corrupted and is not a boolean variable.
  `'string' == True` and `'string' == False` both return `false`, after all.


