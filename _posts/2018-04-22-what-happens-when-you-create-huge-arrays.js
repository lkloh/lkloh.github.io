---
type: post
title: "What happens when you push too often in a JavaScript array?"
date: 2018-04-22
---

Stack Overflow!

```js
function causesOverflow() {
  const arr = [];
  const large = new Array(200000).fill(1);
  arr.push(...large);
  return arr;
}

noOverflow();
causesOverflow();
```

Output is 
```
RangeError: Maximum call stack size exceeded
```

Seems that beyond a certain point, there is no more space to double `arr` 
and stack overflow happens.

Instead, tell the system to set asside that much space from the beginning,
and preallocate the size of your gigantic array:
```js
function noOverflow() {
  const arr = [];
  for (let i = 0; i < 200000; i++) {
    arr.push(i);
  }
  return arr;
}

noOverflow();
```

Only applies for HUGE amounts of data of course, 
but many production systems actually need to care about this.


