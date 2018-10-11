---
type: post
title: "Lodash Flatmap"
date: 2018-10-10
---

I wanted to transform an array of
`[1,2,3,4,5]` into `[1, -1, 2, -2, 3, -3, 4, -4, 5, -5]`,
so I did this:

```js
const flatten = require(`lodash/flatten`);
const map = require(`lodash/map`);

function transform(arr) {
  return flatten(map(arr, n => [n, -1 * n]));
}
```

but turns out you can just use [flatmap](https://lodash.com/docs/#flatMap) instead:
```js
const flatMap = require(`lodash/flatMap`);

function transform(arr) {
  return flatMap(arr, n => [n, -1 * n]);
}
```

