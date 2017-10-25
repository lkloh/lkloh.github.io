---
layout: post
title:  "Destructuring ES6"
date:   2017-10-22
---

Its an ES6 thing, similar to what we have in Python.

```js
const arr = [1, 2, 3];
const a, b;
[a, b] = arr;
console.log(a); // 1
console.log(b); // 2
```

And it really helps with conciseness when you want to do something like this:
```js
function swap(pair) {
	(b, a) = pair;
	return (a, b);
}

const pair = (1, 2);
console.log(swap(pair)); // (2, 1)
```


Sadly, we still can't do this though:
```js
function swap(a, b) {
	b, a = a, b;
	return a, b;
}
```
You can do that in Python, but still no in ES6.