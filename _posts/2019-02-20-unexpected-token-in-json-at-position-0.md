---
type: post
title: "Unexpected token in json at position 0"
date: 2019-02-20
---

Summarized from [here](https://daveceddia.com/unexpected-token-in-json-at-position-0/).

Sometimes when trying to make a HTTP request, 
```js
const users = fetch('/users').then(res => res.json());
```

You get this error message:
```
Unhandled Rejection (SyntaxError): Unexpected token < in JSON at position 0
```

This means the request worked, but `res.json()` failed as you are
trying a parse an invalid json string.

The most likely cause is that the response was HTML, not JSON.

To understand why the server is returning HTML instead of JSON,
try logging what's going on.
```js
const users = [];
fetch('/users').
  .then(res => res.text())
  .then(text => console.log(text));
```

In my case I realized that the server was returning HTML because there was some error
in the server side code. Whoops.





