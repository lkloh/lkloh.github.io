---
type: post
title: "Some or all"
date: 2018-09-29
---

Write
```js
function hasDefinedValue(myDict) {
  Object.values(myDict).some(val => val);
}
```

instead of
```js
function hasDefinedValue(myDict) {
  let defined = false;
  for (const key in myDict) {
    if (myDict[key]) {
      defined = true;
      break;
    }
  }
  return defined;
}
```

