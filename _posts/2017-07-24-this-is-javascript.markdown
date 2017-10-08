---
layout: post
title:  "This is JavaScript"
date:   2017-07-24
---

[This](https://blog.pragmatists.com/the-many-faces-of-this-in-javascript-5f8be40df52e) 
is a great post about `this`. Here is a summary.

`this` is used in JavaScript similar to the way we use it in everyday life
- when referring to something in context.
We say "The rent is expensive, this is really annoying",
not "The rent is expensive. The expensive rent is really annoying".
Knowing what context `this` helps us understand what is annoying.

In JavaScript, `this` is used as a reference within a context.

## Global Context

When someone says "This is annoying" without any context,
you'll assume it refers to the latest situation. 
Perhaps that person is your roommate,
and they are referring to the fact that your landlord just
increased your rent yesterday. 
Or if that person is your parents,
they are referring to the fact that your younger sibling
crashed their car yesterday.

When using `this` in the browser,
you are referring to the global object - the window.
Thus
```js
const a = 10;
console.log(this.a === window.a); // true
```

## Function context

Function context is like a sentence context.
In the sentence "The rent is expensive, this is really annoying",
the context for `this` is "the rent is expensive".
In JavaScript, `this` refers to the function the object executes in.

```js
const a = 1;

foo() {
	return this.a;
}

console.log(foo() === a); // true
```

The function `foo` executes in the global context (window).

When a function is called as a method on an object, `this` is
set to the object the method is called on.

```js
var obj = {
	method: function() {
		return this;
	}
};

console.log(this === window); // true
console.log(obj.method() === window); // false
```























