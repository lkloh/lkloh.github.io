---
type: post
title: "Converting a JavaScript boolean to a Python boolean"
date: 2018-08-23
---

If you're sending this from the client (written in JavaScript),
to the backend (written in Python), you have to be careful as JavaScript booleans
appear as `true|talse` while Python booleans appear as `True|False`.


```js
// JavaScript Client
params = {
  name: 'Alice',
  phone: 123456789,
  is_student: true,
};

pass_to_server(params);
```

```py
// Python Server
params = obtain_from_client(params)

response = {}
if params.is_student:
  response['discount'] = 0.8 * sell_price
return response
```

and the problem is that this is always going to return a discount regardless of whether
the party is a student or not, as `bool('true') = True` and `bool('false') = True` in Python.

Instead you'll want to package it as JSON objects instead:
```js
// JavaScript Client
params = {
  name: 'Alice',
  phone: 123456789,
  is_student: true,
};

pass_to_server(JSON.stringify(params));
```

```py
// Python Server
import json

params = json.loads(obtain_from_client(params))

response = {}
if params.is_student:
  response['discount'] = 0.8 * sell_price
return response
```
