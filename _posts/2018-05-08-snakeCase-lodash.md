---
type: post
title: "Dealing with whitespaces in JavaScript"
date: 2018-05-08
---

One could do this to convert a string with white spaces
into something suitable for a filename or user id...

```js
const name = "John Doe";
const transformToId = str => str.replace(/\s/g, '_');
const id = transformToId(name); // John_Doe
```

But this is even more effective:

```js
import snakeCase from 'lodash/snakeCase';

const name = "John Doe";
const id = snakeCase(name); // John_Doe
```

