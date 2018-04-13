---
type: post
title: "JSON vs SimpleJson in Python"
date: 2018-04-12
---

SimpleJson behaves more intuitively, by transforming a string type to string,
and unicode type to unicode,
while Json always transforms string/unicode to unicode,
which can lead to all sorts of nasty [bugs](https://code.google.com/archive/p/simplejson/issues/40).

## JSON

```py
import json

type(json.loads(u'"foo"')) # returns <type 'unicode'>
type(json.loads('"foo"'))  # returns <type 'unicode'>
```

## SimpleJson

```py
import simplejson

type(simplejson.loads('"foo"'))  # returns <type 'str'>
type(simplejson.loads(u'"foo"')) # returns <type 'unicode'>
```




