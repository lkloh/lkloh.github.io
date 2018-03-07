---
type: post
title: "Resolving JavaScript Promises"
date: 2018-03-07
---

```js
var Promise = require('promise');

function inOrder() {
  return new Promise((resolve, reject) => {
      console.log('foo');
      resolve();
    }).then(() => {
      console.log(`bar ${4 * 3454645}`);
    }).then(() => {
      console.log('buzz');
    });
}

inOrder();
```

Will print
```
foo
bar 13818580
buzz
```

while

```js
var Promise = require('promise');

function inOrder() {
  return new Promise((resolve, reject) => {
      console.log('foo');
    }).then(() => {
      console.log(`bar ${4 * 3454645}`);
    }).then(() => {
      console.log('buzz');
    });
}

inOrder();
```

will print
```foo
```

This is because `then` is only triggered after `resolve` is called.


