---
layout: post
title:  "When to return this"
date:   2017-11-29
---

We write
```js
class FooBar {
	constructor() {}

	function foo() {
		console.log(`foo`);
		return this;
	}

	function bar() {
		console.log(`bar`);
		return this;
	}
}
```

instead of 
```js
class FooBar {
function foo() {
	console.log(`foo`);
}

function bar() {
	console.log(`bar`);
}
```

to use function chaining.
This [explains it a lot better](https://stackoverflow.com/questions/8300844/what-does-return-this-do-within-a-javascript-function) than me.

We can do
```js
var fb = FooBar();
fb.foo().bar();
```

in the first case.