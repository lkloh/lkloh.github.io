---
type: post
title: "Ternary best practices"
date: 2018-05-09
---

Summarized from [here](https://stackoverflow.com/questions/160218/to-ternary-or-not-to-ternary).

## Bad

```js
const sign = n > 0 : `+` : (n === 0 ? `0` : `-`);
```
There is a double ternary here, so not great. 
Makes things confusing the read.
The point of a ternary is to simplify things
(and its a convenient side effect that they get inlined), 
not complicate understanding.

## Better

```js
function getSign(n) {
  if (n === 0) {
    return `0`;
  }
  return n > 0 ? `+` : `-`;
}

const sgn = getSign(n);
```
