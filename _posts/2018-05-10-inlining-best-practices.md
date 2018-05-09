---
type: post
title: "Inlining tricks in ES6"
date: 2018-05-09
---

## Verbose

```js
if (arrB) {
  arrA = arrA.concat(arrB);
} else {
  arrA = arrB;
}
```

## Concise

```js
arrA = [...arrA, ...(arrB || [])];
```

