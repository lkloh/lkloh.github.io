---
layout: post
title:  "Enclosing strings in JavaScript"
date:   2017-07-23 11:05:37 -0700
---

In JavaScript, you could use enclose a string in three ways:
```js
'abcd'
"abcd"
`abcd`
```

In general, for ES5, you are encouraged to use double quotes. This is because
```js
console.log("John's chair");
```

is easier to read and write than
```js
console.log('John\'s chair');
```

In ES6, you could make this a template literal and write
```js
console.log(`John's chair`);
```

Template strings let you compile expressions within the `${..}`, such as:
```js
function divResult(a, b) {
	return String(a / b);
}

const result = `Result of 42 / 7 is ${divResult(42, 7)}`;
``` 

Another advantage of template strings is that you could make the string a multiline string:
```js
const introMe = 
	`My name is Jane Smith.
	I am 21 years old.
	Reading books is my hobby.`;
```

