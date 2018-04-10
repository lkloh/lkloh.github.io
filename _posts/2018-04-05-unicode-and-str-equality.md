---
type: post
title: "Unicode and string equality in Python"
date: 2018-04-05
---

Someone was wondering what the result of 
```py
# Python 2
'string' == u'string'
```
would be. Its `True`. 

If the string content matches unicode content, they should be considered equal.

In JavaScript, source code is treated as UTF-16 code units,
so you shouldn't even run into this confusion.

In fact, the root cause of the confusion was a completely different matter altogether.

Oh well, when Jan 1, 2020 rolls around and everyone cuts over to Python 3
for security reasons by then, no one will get confused, obviously.
In theory, if everyone makes the enormous effort needed to migrate to Python 3.



