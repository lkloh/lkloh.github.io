---
layout: post
title:  "Why you can't just reassign this"
date:   2017-10-29
---

We can't reassign `this` explicitly.

This is fine,
```
class RectangleAllowed {
	constructor(height, width) {
		this.height = height;
		this.width = width;
	}

	allowedOperator() {
		this.height = 3.1415926535898;
	}
}

rectA = new RectangleAllowed(4, 5);
rectA.allowedOperator()
console.log(rectA);
```
as only a property of the rectangle object is alter.

But this is not ok,
```
class RectangleDisallowed {
	constructor(height, width) {
		this.height = height;
		this.width = width;
	}

	disallowedOperator() {
		var newVar = {height: 3.1415926535898, width: this.width};
		this = newVar; // comment out to make it work!
	}
}

rectB = new RectangleDisallowed(4, 5);
rectB.disallowedOperator()
console.log(rectB);
```
as the entire rectange object is altered by calling a function on it,
which would confuse the user.

Running the latter script gave this error:
```
		this = newVar; // comment out to make it work!
		^^^^
ReferenceError: Invalid left-hand side in assignment
    at createScript (vm.js:56:10)
    at Object.runInThisContext (vm.js:97:10)
    at Module._compile (module.js:542:28)
    at Object.Module._extensions..js (module.js:579:10)
    at Module.load (module.js:487:32)
    at tryModuleLoad (module.js:446:12)
    at Function.Module._load (module.js:438:3)
    at Module.runMain (module.js:604:10)
    at run (bootstrap_node.js:389:7)
    at startup (bootstrap_node.js:149:9)
```







