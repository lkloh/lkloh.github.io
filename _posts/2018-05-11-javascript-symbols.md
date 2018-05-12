---
type: post
title: "JavaScript Symbols for guaranteed-unique keys"
date: 2018-05-11
---

[Symbols](https://hacks.mozilla.org/2015/06/es6-in-depth-symbols/) can be used to 
generate unique keys when you really want to name a property key in a dictionary 
`author` but are worried that somewhere down the line someone else may decided on `author`
for a different reasons.

It helps avoid name clashes while still allowing you to name things
in a format suitable for humans.

```js
const life = Symbol(42);

console.log(life === Symbol(42)); // false
console.log(Symbol(42) === Symbol(42)); // false
console.log(life === life); // true
```


