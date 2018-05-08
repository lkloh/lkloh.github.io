---
type: post
title: "Sorting an array of arrays"
date: 2018-05-04
---

To sort this:
```js
const arr = [
  [`zzz`, 35],
  [`xxx`, 57],
  [`ggg`, 2],
  [`hhh`, 4],
  [`rrr`, 23],
];
```

by only the _first_ column in alphabetical order, you do:

```js
const arr = [
  [`zzz`, 35],
  [`xxx`, 57],
  [`ggg`, 2],
  [`hhh`, 4],
  [`rrr`, 23],
];
arr.sort((r1, r2) => r1[0].localeCompare(r2[0]));
```

Now `arr`becomes
```
[`ggg`, 2],
[`hhh`, 4],
[`rrr`, 23],
[`xxx`, 57],
[`zzz`, 35],
```
