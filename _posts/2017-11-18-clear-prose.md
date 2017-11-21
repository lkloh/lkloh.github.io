---
layout: post
title:  "Clear prose"
date:   2017-11-18
---

I wrote something like this:

```js
// possible locations are ['home', 'work', 'party', 'airplane', 'volcano']
if ((prevLoc !== 'home') && (currLoc === 'home')) {
	this.cookDinner();
} else if ((prevLoc === 'home') && (currLoc !== 'home')) {
	this.putOnShoes();
}
```

Hard to understand. 
Someone suggested in code reviews that I write it this way instead for clarity:

```js
if ((prevLoc !== currLoc) {
	if (currLoc === 'home')
		this.cookDinner();
	} else {
		this.putOnShoes();
	}
}
```
Which is bad as the `else` branch could mean transitioning between an `airplane` and a `party`


I changed it to
```js
if (prevLoc !== currLoc) {
	if ((prevLoc !== 'home') && (currLoc === 'home')) {
		this.cookDinner();
	} else if ((prevLoc === 'home') && (currLoc !== 'home')) {
		this.putOnShoes();
	}
}
```
instead.

I really should have thought more deeply before telling people why their way doesn't work.
This would have done the trick:
```js
if (prevLoc !== currLoc) {
	if (currLoc === 'home') {
		this.cookDinner();
	} else if (prevLoc === 'home') {
		this.putOnShoes();
	}
}
```



