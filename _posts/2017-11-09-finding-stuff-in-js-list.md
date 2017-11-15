---
layout: post
title:  "Finding something in a JavaScript list"
date:   2017-11-09
---

## Yes

```js
var fruits = ['apple', 'orange', 'pear', 'avocado'];
var orangeExists = fruits.find('orange'); // true
```

## No

```js
var fruits = ['apple', 'orange', 'pear', 'avocado'];
var orangeExists = fruits.indexOf('orange') > -1; // true
```

