---
layout: post
title:  "JavaScript Strict Mode"
date:   2017-10-06
---

```
"use strict";
```

What is [strict mode]()?
* Introduced in EC5 (c. 2009)
* Prevents some poorly designed features from being used
* Throws more exceptions - blocks some unsafe actions: fail fast and loudly
* Strict mode is not a subset of javascript, but has different semantics from normal code
* Supported in all major browser (except IE9 and below)

Read more from [here](https://www.nczonline.net/blog/2012/03/13/its-time-to-start-using-javascript-strict-mode/).

## No global variables

* Strict: All variables must be declared
* Non strict: Assigning values to an undeclared variable makes it a global variable

## Unique properties in objects/functions

This throws a syntax error
```js
"use strict";

const object = {
    foo: `bar`,
    foo: `bar`.
}
```

No error
```js
const object = {
    foo: `bar`,
    foo: `bar`.
}
```

## Eval is safer

Throws error
```js
"use strict";

eval("var x = 10;");
console.log(x)
```

No error
```js
eval("var x = 10;");
console.log(x);
```

## Best practices

`"use strict";` in functions only, not global context when dealing with large codebases
that were developed over many years. 
```js
function myFunc() {
    "use strict";
    // do stuff
}
```

Start using it in new stuff that is being built out,
to help avoid more errors/unsafe practices.


