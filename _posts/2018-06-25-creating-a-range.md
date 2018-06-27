---
type: post
title: "Making an array of 1,2,3..."
date: 2018-06-25
---

## Python

Python 2
```py
xrange(5) # [0, 1, 2, 3, 4]
```

Python 3
```py
range(5) # [0, 1, 2, 3, 4]
```

## JavaScript

Either
```js
Array.from(Array(5).keys()); # [0, 1, 2, 3, 4]
```

or
```js
[...Array(5).keys()]; # [0, 1, 2, 3, 4]
```


