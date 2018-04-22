---
type: post
title: "Undefined is not null in JavaScript"
date: 2018-04-22
---

Given this function:
```js
function defaultFunc(a='my special default value!') {
  console.log(a);
}
```

If you call

```js
defaultFunc('control case');
```

then `control case` gets output.

If you call 

```js
defaultFunc(null);
```

then the default value does _not_  gets logged.
`null` means that "no value" has been selected, so `null` gets logged instead.

To invoke the default value, you need to pass in:
```js
defaultFunc(undefined)
```

Then `my special default value!` gets logged.

