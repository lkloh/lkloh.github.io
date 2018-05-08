---
type: post
title: "Using compiled keys in JavaScript keys"
date: 2018-05-04
---

This does not work!
```js
const name = `Alice`;
const foo = {`${name}_Anderson`: `101 Hill Street, CA 94305`}
```

JavaScript does not allow template strings as property keys,
as template strings are not constants, but need to be compiled. 
Only static objects can be used as property keys.

To use a compiled object as a property key, compute it by doing:
```js
const name = `Alice`;
const foo = {[`${name}_Anderson`]: `101 Hill Street, CA 94305`}
```

Thanks [Stack Overflow](https://stackoverflow.com/questions/33194138/template-string-as-object-property-name)!


