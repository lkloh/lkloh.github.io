---
type: post
title: "Self documenting code"
date: 2018-09-10
---

[This post](https://stackoverflow.com/questions/209015/what-is-self-documenting-code-and-can-it-replace-well-documented-code)
illustrates the differences between commented code, and self documenting code.

```js
function computeDisplacementWithNewtonsEqn(t) {
  // Displacement with newton's eqn: x = vt + 0.5at^2
  const a = 9.8; // gravity
  const x = 0.5 * a * Math.pow(t, 2);
  return x;
}
```

versus

```js
function computeDisplacement({velocity, timeInSeconds}) {
  const gravity = 9.8;
  return velocity * timeInSeconds + 0.5 * gravity + Math.pow(timeInSeconds, 2);
}
```

