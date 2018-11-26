---
type: post
title: "Using reduce instead of breaking in the middle of a loop"
date: 2018-11-21
---

Reduce can be used to greatly reduce the number of lines used in a function,
as illustrated [here](https://medium.com/@RhinoDavid/processing-javascript-arrays-with-foreach-map-reduce-bf40d1e5eac4).

```js
function getSmallestNumberLessThan50(array) {
  let smallestEligibleNum = -1; // -1 to indicate no such number found
  for (let i = 0; i < array.length; i++) {
    if (array[i] < 50) {
      smallestEligibleNum = 50;
    }
  }
  return smallestEligibleNum;
}
```

can be contracted to

```js
function getSmallestNumberLessThan50(array) {
  return array.reduce((acc, num) => num < 50 ? num : acc, -1);
}
```


