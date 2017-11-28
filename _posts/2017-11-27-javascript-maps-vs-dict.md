---
layout: post
title:  "Javascript maps let you iterate in order of insertion"
date:   2017-11-27
---

Maps and dicts in JavaScript pretty much behave the same right?

```js
var dict = {
	foo: {a: 1, b: 2, c: 3}, 
	bar: {a: 1, b: 2}
};
console.log(dict);
console.log(dict.foo ? 'present' : 'not_present');
console.log(dict.not_present ? 'present' : 'not_present');

console.log();

var map = new Map();
map.set('foo', {a: 1, b: 2, c: 3});
map.set('bar', {a: 1, b: 2});
console.log(map);
console.log(map.get('foo') ? 'present' : 'not_present');
console.log(map.get('not_present') ? 'present' : 'not_present');
```

Maps can iterate their key-value pairs in the order they were inserted.
The can be very valuable as it allows cross-platform compatibility.
Otherwise your iteration was at the mercy of the undelying implementation
of the dict iteration,
or you were forced to use something like an array to do stuff,
which doesn't have nice properties like letting you look up 
stuff in constant time.

