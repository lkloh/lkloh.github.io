---
type: post
title: "Using require to load json files in Node.js"
date: 2018-11-14
---

I was trying to hardcode some data for an intermediate dev step,
that would later be removed after syncing to the backend.
I was initially doing it in the .js file
before realizing it made more sense to separate the data source from javascript.

## test.js file
```js
/* globals require */

const data = require(`./data.json`);
console.log(data.name); // prints "Alice"
```

## data.json file
```
{
  "name": "Alice",
  "Age": 12,
  "Address": "123 Main Street, Utopia, 12345",
  "Favorite Foods": [
    "Chocolate",
    "Sushi",
    "Bread"
  ]
}
```

