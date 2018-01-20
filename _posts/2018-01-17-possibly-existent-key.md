---
type: post
title: "Possibly existent key in a struct"
date: 2018-01-17
---

```js
function fooIsTrue(options) {
  if (options && _.hasKey('foo', options) {
    return options.foo;
  } else {
    return false;
  }
}
```

Could be more concisely written as

```js
function fooIsTrue(options) {
  var options = options || {};
  return !!options.foo;
}
```

If options has `foo` as a key, then it just returns `options.foo`.

If `options` does not have `foo` as a key, then `options.foo`
returns `null`, `!null` returns `true`, and `!!null` returns false as required.

