---
type: post
title: "Ternary best practices"
date: 2018-05-09
---

Summarized from [here](https://stackoverflow.com/questions/160218/to-ternary-or-not-to-ternary).

## Bad

```js
const sgn = n > 0 : `+` : (n === 0 ? `ZERO` : `-`);
```
There is a double ternary here, so not great. 
Makes things confusing to read.
The point of a ternary is to simplify things,
not strictly to inline stuff.
It should not complicate understanding.

## Better

```js
function getSign(n) {
  if (n === 0) {
    return `ZERO`;
  }
  return n > 0 ? `+` : `-`;
}

const sgn = getSign(n);
```
