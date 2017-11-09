---
layout: post
title:  "What is a constant in ES6?"
date:   2017-11-08
---

ES5 called all variables `var`.

ES6 introduced `const` and `let`.

```js
// Constant
const MEANING_OF_LIFE = 42;

// Not constant!!!
const dict = {a: 1, b: 2};
dict[c] = 3;
```

Does that mean I should have written 
```js
const MEANING_OF_LIFE = 42;

const DICT = {a: 1, b: 2};
DICT[c] = 3;
```
if I wanted [good style](https://google.github.io/styleguide/jsguide.html#naming-constant-names)?

Not necessarily, as a `const` variable [can change](https://mathiasbynens.be/notes/es6-const).

You only use ALL CAPS TO DECLARE A VARIABLE if it can never get updated.





