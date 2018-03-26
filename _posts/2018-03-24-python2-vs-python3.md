---
type: post 
title: "Python 2 vs Python 3"
date: 2018-03-24
---

Summarized from [here](http://blog.teamtreehouse.com/python-2-vs-python-3)

## Print is a function in Python 3

```py
# Python 2
print "Hello world"
```

vs

```py
# Python 3
print("Hello world")
```

## Unicode strings as default in Python 3

```py
# Python 2
print 'The \u2600 is hidden by \u2601 so bring an \u2602 just in case.'
```
returns: The \u2600 is hidden by \u2601 so bring an \u2602 just in case.

vs
```
# Python 3
print 'The \u2600 is hidden by \u2601 so bring an \u2602 just in case.'
```
which returns: The &#9728; is hidden by &#9729; so bring an &#9730; just in case.

This really helps as due to globalization,
as more people realize the not everyone speaks just English.

## Integer division
```py
# Python 2
5/2 # returns 2 which is rather counterintuitive
```
This was because Python did not want to take two integers and return a float.
But returning "2" after computing "5/2" was very counterintuitive to many people.

vs

```py
# Python 3
5/2 # returns 2.5 as expected
```

