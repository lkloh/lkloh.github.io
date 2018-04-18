---
type: post
title: "JavaScript array: PUSH or CONCAT?"
date: 2018-04-18
---

To merge two arrays in JavaScript, you could do this:

## Merge using CONCAT

```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const merged = arr1.concat(arr2); // [1, 2, 3, 4, 5, 6]
```

Since `concat` creates a new array, that may cause a performance hit though.

## Merge using PUSH

```js
let arr1 = [1, 2, 3];
let arr2 = [4, 5, 6];
arr1.push(..arr2); // arr1 is now [1, 2, 3, 4, 5, 6]
```
PUSH appends to the end of the array that is being pushed to, so no 
need to create a new array in memory.

## Conclusion

Use PUSH when performance is important.
CONCAT is better for readability in general, and to 
avoid contaiminating previous data structures.


