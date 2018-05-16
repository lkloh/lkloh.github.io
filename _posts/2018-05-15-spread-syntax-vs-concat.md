---
type: post
title: "When to use spread syntax vs concat"
date: 2018-05-15
---

These seem to have the same effect:
```js
const arrA = [1, 2, 3];
const arrB = [4, 5];

console.log([...arrA, ...arrB]); // prints [1, 2, 3, 4, 5]
console.log(arrA.concat(arrB));  // prints [1, 2, 3, 4, 5]
```

According to [Stack Overflow](https://stackoverflow.com/questions/48865710/spread-operator-vs-array-concat)

## Use "concat" when merging arrays of UNKNOWN size

```js
arrayA.concat(arrayB);
```

"concat" tends to perform faster than spread syntax as it uses array-specific optimizations.

## Use spread syntax when merging singleton elements

It allows you to be explicit about what element(s) you are appending to the new array.

```js
["hello", "world", ...array];
```

Performs slower as it uses iteration.

Also liable to result in stack overflow when doing something like
```js
[...hugeArray, ...massiveArray, ...giganticArray];
```
 
while
```js
hugeArray.concat(massiveArray).concat(giganticArray); 
```
is fine.
