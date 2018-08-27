---
type: post
title: "Object Spread for JS dicts"
date: 2018-08-18
---

Object spread could shrink this chunk of code
```js
const extend = require(`lodash/extend`);
const params = {
  first_name: 'John',
  last_name: 'Doe',
  birthday: new Date(2000, 01, 01),
};

// do random stuff

params = extend(params, {
  city: 'San Francisco',
  state: 'California', 
});
```

to


```js
const params = {
  first_name: 'John',
  last_name: 'Doe',
  birthday: new Date(2000, 01, 01),
};

// do random stuff

params = {
  ...params,
  city: 'San Francisco',
  state: 'California', 
};
```

