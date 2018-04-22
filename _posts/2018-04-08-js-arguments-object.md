---
type: post
title: "The JavaScript arguments object"
date: 2018-04-08
---

Turns out you can get all the arguments passed into a function by using the `arguments` keyword.

```js
function(a, b, c) {
  expect(a).to.equal(arguments[0]);
  expect(b).to.equal(arguments[1]);
  expect(c).to.equal(arguments[2]);
}
```

Though why use it these days when we have destructuring in ES6?

Now you can even do this:
```js
function example({firstName, lastName, SSN=0}) {
  console.log(firstName); // John
  console.log(lastName); // Smith 
  console.log(SSN); // 0
}

example({
  firstName: `John`,
  lastName: `Smith`,
});
```


