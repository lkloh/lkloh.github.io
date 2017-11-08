---
layout: post
title:  "Extending a JSON object in JS"
date:   2017-11-07
---

Lodash can help in this, as with many other things one may want to do in JavaScript.

Using [extend](https://lodash.com/docs/4.17.4#assignIn): 

```js
var dict = {
	a: 1,
	b: 2,
	c: 3,
};
.extend(dict, {
	d: 4,
	e: 5,
});
console.log(dict); 
// returns {a: 1, b: 2, c:3, d: 4, e: 5};
```

You could also do this if desired:

```js
var dictA = {
	a: 1,
	b: 2,
	c: 3,
};
var dictB = {
	d: 4,
	e: 5,
}
var dict = .extend(dictA, dictB);
console.log(dict); 
// returns {a: 1, b: 2, c:3, d: 4, e: 5};
```






