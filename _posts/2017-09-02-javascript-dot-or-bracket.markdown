---
layout: post
title:  "Accessing dictionary values in Javascript"
date:   2017-09-02 10:38:34 -0700
---

Scripts for this are [here](https://github.com/lkloh/javascriptPlayground/blob/master/accessingDictValues.js).

Given some dictionary in Javascript, such as

```js
d = {'A': 'Alice', 'B': 'Bob', 'C': 'Carol'}
```

There are two ways to access the values in the dictionary:

*Dot notation*

```js
d.A = 'Alice';
d.B = 'Bob';
d.C = 'Carol';
```

or

*Bracket notation*

```js
d['A'] = 'Alice';
d['B'] = 'Bob';
d['C'] = 'Carol';
```

Convention is to use dot notation if possible,
since it is cleaner, and only use bracket notation if you need to.

## Limitations of dot notation

Dot notation has some limitations in the types of keys it can store, however.

Numbers cannot be used: `d.42 = 'Alice'` will fail.


Also, calling keys in a loop required bracket notation.

```js
function accessByDot(d) {
	console.log('\n\n');
	for (key in d) {
		console.log(d.key);
	}
}

accessByDot(d);
```

will print

```js
undefined
undefined
undefined
```

To get it to print out the key-value pairs in the dictionary, we need:

```js
function accessByBracket(d) {
	console.log('\n\n');
	for (key in d) {
		console.log(d[key]);
	}
}

accessByBracket(d);
```

which will print

```
Alice
Bob
Carol
```

as desired.


