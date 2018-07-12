---
type: post
title: "for vs forEach in Javascript"
date: 2018-07-11
---

Modified from [here](https://thejsguy.com/2016/07/30/javascript-for-loop-vs-array-foreach.html).

## forEach

Try to use this if possible.

```js
const fruits = [`apple`, `pear`, `banana`];
fruits.forEach(fruit => console.log(fruit));
```

is much cleaner and requires less cognitive overhead to understand than

```js
const fruits = [`apple`, `pear`, `banana`];
for (let i = 0; i < fruits.length; i++) {
  console.log(fruit);
}
```

It also creates fewer off by one errors, as one could do
```js
const fruits = [`apple`, `pear`, `banana`];
fruits.forEach((fruit, index) => console.log(`${fruit} at index ${index}`));
```

instead of
```js
const fruits = [`apple`, `pear`, `banana`];
for (int i = 0; i < fruits.length; i++) {
  console.log(`${fruit} at index ${index}`);
}
```

## for

Use this when you might want to break out of a loop early.
`forEach` will iterate over every single item,
while `for` will break out of the loop immediately.

Thus
```js
for (let i = 0; i < fruits.length; i++) {
  if (fruit.isRotten()) {
    return null;
  }
}
```

is more performance efficient than

```js
let hasRottenFruit = false;
fruit.forEach(fruit => {
  if (fruit.isRotten()) {
    hasRottenFruit = true;
  }
});
if (hasRottenFruit) {
  return null;
}
```






