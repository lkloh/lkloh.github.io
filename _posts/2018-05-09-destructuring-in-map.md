---
type: post
title: "Destructuring an array of arrays"
date: 2018-05-09
---

## Good

```js
const arr = [
  [`A`, 2],
  [`B`, 3],
  [`C`, 4],
  [`D`, 5],
  [`E`, 6],
];

function double(arr) {
  return arr.map(row => {
    const [key, value] = row;
    return [key, 2 * value];
  });
}
```

## Better

```js
const arr = [
  [`A`, 2],
  [`B`, 3],
  [`C`, 4],
  [`D`, 5],
  [`E`, 6],
];

const doubledArr = arr.map(([key, value]) => [key, 2 * value]);
```
