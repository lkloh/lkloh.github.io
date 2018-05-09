---
type: post
title: "Arrow functions with and without parentheses"
date: 2018-04-30
---

With arrow functions, these are acceptable:

```js
const identity = arg => arg;
```

and 

```js
const identity = arg => {
  return arg;
}
```

But then when returning an object, things may get more complicated:
```js
const returnObj = arg => {foo: arg};
```
throws a syntax error.

You need to write
```js
const returnObj = arg => {
  return {foo: arg};
};
```

This is because curly braces are used to denote the function body,
and thus the parser gets confused if you try to write
```js
const returnObj = arg => {foo: arg};
```

You need to enclose the return value in parentheses to keep the parser happy.
```js
const returnObj = arg => ({foo: arg});
```
would work for inlining function.

See more [here](https://www.nczonline.net/blog/2013/09/10/understanding-ecmascript-6-arrow-functions/).



