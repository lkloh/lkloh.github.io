---
type: post
title: "forEach instead of map when you do not care about the return value"
date: 2018-05-10
---

## When to use "map" instead of "forEach"

When you care about the return value.

```js
function double(arr) {
  return arr.map(n => 2 * n);
}

const arr = [1, 2, 3];
const doubleArr = double(arr); // [2, 4, 6]
```

## When to use "forEach" instead of "map"

When altering the state of something.

```js
function setStudentsToAlumni() {
  this.state.students.forEach(person => person.set(`alumni`));
}

this.setStudentsToAlumni(); // no return value
```

