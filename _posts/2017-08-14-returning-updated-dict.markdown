---
layout: post
title:  "Returning an updated Javascript Dictionary/object"
date:   2017-08-14 01:57:45 -0700
---

Given this object:
```js
const john = {
	firstName: `John`,
	lastName: `Doe`,
	gender: `Male`,
	college: `Harvard`,
	citizenship: `United States`,
};
```

If I wanted to update this object and return a new one in the process
-- to avoid having a function mutate an input value, 
I would used [Object.assign](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign) to do

```js
function returnUpdatedDict(d, fieldsToUpdate) {
	return Object.assign({}, d, fieldsToUpdate);
}
```

So if John wants to become a female and move to Utopia, I would do:
```js
goToHeaven = {
	firstName: `Jane`,
	gender: `Female`,
	citizenship: `Utopia`,
};
const jane = returnUpdatedDict(person, goToHeaven);
```

that will return a new object, `jane`, which has form:
```js
{
	firstName: `Jane`,
	lastName: `Doe`,
	gender: `Feale`,
	college: `Harvard`,
	citizenship: `Utopia`,
}
```
