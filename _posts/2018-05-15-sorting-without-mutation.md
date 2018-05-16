---
type: post
title: "Sorting a JavaScript array without mutation"
date: 2018-05-15
---

This mutates the array:
```js
const arr = [5, 1, 4, 2, 3];
arr.sort((a, b) => a <= b);
console.log(arr); // prints [1, 2, 3, 4, 5];
```

To avoid mutating the array, copy it.
```js
const arr = [5, 1, 4, 2, 3];
const sortedArr = arr.sort((a, b) => a <= b);
console.log(sortedArr); // prints [1, 2, 3, 4, 5];
console.log(arr); // prints [5, 1, 4, 2, 3];
```

