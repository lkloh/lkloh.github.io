---
layout: post
title:  "Multilines in JavaScript have evolved a lot"
date:   2017-10-23
---

Recently I had to work with some legacy code written in Backbone.
The last time I worked on Backbone was back in 2014. 
I saw pack of a code that looked a bit like this:

```js
// ES5
var display_this = 
	"<div class='person'>" + 
		"<h1><b>Name:</b> LK Loh </h1>" +
		"<p><b>Birthday:</b> October 24</p>" +
		"<p><b>Address:</b> San Francisco</p>" +
	"<div>"`;
```

I was wondering not refactor it like this instead:

```js
// ES5
var display_this = 
	"<div class='person'> \ 
		"<h1><b>Name:</b> LK Loh </h1> \
		"<p><b>Birthday:</b> October 24</p> \
		"<p><b>Address:</b> San Francisco</p> \
	"<div>"`;
```
and cut out that concatenation.

[Apparently](https://stackoverflow.com/questions/805107/creating-multiline-strings-in-javascript)
the whitespace after the slash could cause errors in some browsers
as not all browsers support it probably -- 
there's not explicit requirement to do so in ES5.
So concatenation it is. So ugly though. 

Of course, these days with ES6 we can just do this: 

```js
// ES6
var display_this = 
	`<div class='person'>
		<h1><b>Name:</b> LK Loh </h1> 
		<p><b>Birthday:</b> October 24</p>
		<p><b>Address:</b> San Francisco</p>
	<div>`;
```
