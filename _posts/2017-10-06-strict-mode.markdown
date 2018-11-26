---
layout: post
title:  "JavaScript Strict Mode"
date:   2017-10-06
---

```
"use strict";
```

What is strict mode?
* Introduced in ES5 (c. 2009)
* Prevents some poorly designed features from being used
* Throws more exceptions - it blocks some unsafe actions, failing fast and loudly
* Strict mode is not a subset of javascript, but has different semantics from normal code
* Supported in all major browsers (except IE9 and below)

Read more from [here](https://www.nczonline.net/blog/2012/03/13/its-time-to-start-using-javascript-strict-mode/).

## No global variables

* Strict: All variables must be declared
* Non strict: Assigning values to an undeclared variable makes it a global variable

## Unique properties in objects/functions

Throws error:
```js
"use strict";

const object = {
    foo: `bar`,
    foo: `bar`,
}
```

No error:
```js
const object = {
    foo: `bar`,
    foo: `bar`,
}
```

## Eval is unsafe!

Throws error:
```js
"use strict";

eval("var x = 10;");
console.log(x);
```

No error:
```js
eval("var x = 10;");
console.log(x);
```

## Best practices

`"use strict";` in functions only, not global context when dealing with large codebases
that were developed over many years. Otherwise you may find that old code starts breaking.

```js
function myFunc() {
    "use strict";
    // do stuff
}
```

Start using it in new stuff that is being built out, to help avoid more errors/unsafe practices.

## "use strict" is turned on by default in JavaScript modules

As described [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#Strict_mode_for_modules)

```js
export function foo() {
  x = 3; // throws an error as "x" is not declared
}
```

