---
layout: post
title:  "Useful Lodash function: Pick"
date:   2017-08-12
---

Given a dictionary like
```js
const person = {
	firstName: `John`,
	lastName: `Doe`,
	gender: `Male`,
	college: `Harvard`,
	citizenship: `United States`,
};
```

If you wanted a subset of the object's keys, say `firstName`, `lastName`, and `college`, 
you could do:
```js
function getSubset(person) {
	return {
		firstName: person.firstName, 
		lastName: person.lastName, 
		college: person.college,
	}
}
```

Or you could refactor with the `pick` function from 
[lodash](https://lodash.com/docs/4.17.4#pick) to be
```js
function getSubset(person) {
	return pick(person, [`firstName`, `lastName`, `college`]);
}
```


























