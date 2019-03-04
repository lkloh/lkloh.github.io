---
type: post
title: "Creating lists of unique objects using ES6 arrays vs sets"
date: 2019-03-03
---

## Creating lists of unique objects using sets

This class checks for existence of a value of a set in O(1) time. 
```js
class ObjSet {
  constructor() {
    this.obj = [];
  }
  
  // checks for existence of "val" in O(1) time
  function has(val) {
    return val in this.obj;
  }

  // tries to add unique val in  O(1) time
  function add(val) {
    if (!this.has(val)) {
      this.obj.add(val);
    }
  }
}
```

What happens if you check for the existance of an object in that set?
```js
var objSet = new ObjSet();
objSet.add({x: 1});
console.log(objSet.has({x: 1})); // true
console.log(objSet.has({x: 2})); // true
```

This happens because `arr.has(key)` only works right on
numbers and strings. If `key` is an object, it gets cast to a string first.
That's why
```js
console.log({x: 1} + ''); // [object Object]
```
and therefore we ended up with `this.obj = "[object Object]"`.

To fix this problem, modify the class to:
```js
class ArrSet {
  constructor() {
    this.arr = [];
  }
  
  // checks for existence of "val" in O(N) time
  function has(val) {
    return this.arr.indexOf(val) > -1;
  }

  // tries to add unique val in  O(N) time
  function add(val) {
    if (!this.has(val)) {
      this.arr.push(value);
    }
  }
}
```

and then
```js
var arrSet = new ArrSet();
arrSet.add({x: 1}); // arrSet = [{x: 1}]
console.log(arrSet.has({x: 1})); // true
console.log(arrSet.has({x: 2})); // false
```
as expected.

Unfortunately using `ArrSet` takes O(N) time while
`ObjSet` takes O(1) time, but then sometimes you still need `ArrSet` 
if you're trying to create unique objects (that are not numbers or strings).









Summarized from [here](https://egghead.io/lessons/javascript-use-es6-sets-to-improve-javascript-performance).

