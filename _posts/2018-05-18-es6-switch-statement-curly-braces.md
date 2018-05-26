---
type: post
title: "What curly braces for each case in a SWITCH statement do"
date: 2018-05-18
---

What's the difference between
```
const fruitColor = ``;
switch (fruit) {
  case `apple`:
    fruitColor = `red`;
    break;
  case `pear`:
    fruitColor = `green`;
    break;
  case `grapes`:
    fruitColor = `purple`;
    break;
  default:
    fruitColor = `brown`; // rotten fruit
}
```

and

```
const fruitColor = ``;
switch (fruit) {
  case `apple`: {
    fruitColor = `red`;
    break;
  } case `pear`: {
    fruitColor = `green`;
    break;
  } case `grapes`: {
    fruitColor = `purple`;
    break;
  } default: {
    fruitColor = `brown`; // rotten fruit
  }
}
```

?

Curly braces let you define a new function scope.
Thus you could write

```
const fruitColor = prevColor;
switch (fruit) {
  case `apple`: {
    const prevColor = `red`;
    fruitColor = prevColor; // red
    break;
  } case `pear`: {
    fruitColor = `green`;
    break;
  } case `grapes`: {
    fruitColor = `purple`;
    break;
  } default: {
    fruitColor = `brown`; // rotten fruit
  }
}
```

but

```
const fruitColor = prevColor;
switch (fruit) {
  case `apple`:
    const prevColor = `red`;
    fruitColor = prevColor;
    break;
  case `pear`:
    fruitColor = `green`;
    break;
  case `grapes`:
    fruitColor = `purple`;
    break;
  default:
    fruitColor = `brown`; // rotten fruit
}
```

throws a syntax error about a redefined variable.

Read more [here](https://stackoverflow.com/questions/42480949/what-do-the-curly-braces-do-in-switch-statement-after-case-in-es6).



