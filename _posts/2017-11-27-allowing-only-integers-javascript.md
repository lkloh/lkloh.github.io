---
layout: post
title:  "Only integers are allowed"
date:   2017-11-28
---

This bit of code in JavaScript allows the user to input only integers.
```js
this.bind('keydown', this.allowOnlyIntegers, this);

...

function allowOnlyIntegers(e) {
	var ZERO_CHAR_CODE = 48;
	var NINE_CHAR_CODE = 57;
	if (ZERO_CHAR_CODE > e.charCode || e.charCode > NINE_CHAR_CODE) {
		e.preventDefault();
	}
}
```

A better way to do things is like this:
```js
this.bind('keydown', this.allowOnlyIntegers, this);

...

function allowOnlyIntegers(e) {
	if ('0'.charCodeAt(0) > e.charCode || '9'.charCodeAt(0) > NINE_CHAR_CODE) {
		e.preventDefault();
	}
}
```