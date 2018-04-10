---
type: post
title: "Array.fill(<itemContent>, startPos(optional), endPos(optional))"
date: 2018-04-05
---

[Array.fill](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/fill)
lets you declare an array and initialize it.

Examples:
```js
const random = [3,7,9,2,67,45,78,6];
const evenRandom = Array.fill(random.filter(n => n % 2 === 0));
```



