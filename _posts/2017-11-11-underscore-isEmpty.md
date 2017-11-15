---
layout: post
title:  "Underscore isEmpty"
date:   2017-11-11
---

Often you don't know if the variable passed to a javascript function
has the type you expect it to have, so you must check.
```js
function updateUser(user, props) {
	if (_.isEmpty(props)) { // props is null/undefined/empty set
		return;
	} else { // props has a key-value pair(s)
		user['id'] = hash(props);
	}
}
```

And `_.isEmpty` works:

```js
// ES6
var _ = require('underscore');

console.log(`Null: ${_.isEmpty(null)}`); // true
console.log(`Undefined: ${_.isEmpty(undefined)}`); // true
console.log(`Empty set: ${_.isEmpty({})}`); // true
console.log(`Non-empty set: ${_.isEmpty({a: 1})}`); // false
```
