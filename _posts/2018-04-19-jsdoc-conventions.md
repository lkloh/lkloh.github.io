---
type: post
title: "JSDoc conventions"
date: 2018-04-19
---

[JSDoc](http://usejsdoc.org/about-getting-started.html) has conventions
on how documentation in JavaScript should be written.
Hint: It's not exactly the same as Python.
I work with both often enough that sometimes I forget which language I'm writting in
... until the linter complains that I'm writing CamelCase in Python 
or snake_case in JavaScript.
Unfortunately, the linter can't catch all wrong conventions.

## Docstrings must be placed BEFORE a function, not after the function definition

### Python
```py
def double(n):
  '''Doubles the number passed in'''
  return 2 * n
```

### JavaScript
```js
/** Doubles the number passed in */
function double(n) {
  return 2 * n;
}
```

## When the docstring spans multiple lines, the start and end of the docstring must be empty

### Correct
```js
/**
 * Doubles the number passed in
 * @param {number} n - number to be doubled
 * @return {Number} double of n
 */
function double(n) {
  return 2 * n;
}
```

### Wrong
```js
/** Doubles the number passed in
 * @param {number} n - number to be doubled
 * @return {Number} double of n */
function double(n) {
  return 2 * n;
}
```




