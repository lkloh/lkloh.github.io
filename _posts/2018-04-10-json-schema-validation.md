---
type: post
title: 'JSON Schema Validation library - Voluptuous'
date: 2018-04-10
---

[Voluptuous](https://github.com/alecthomas/voluptuous) is a Python library for
validating data coming into Python such as JSON, YAML, etc.

## Example Schema

```py
validate_params = Schema({
  'gender': In(['male', 'female', 'other']),
  'type': In(['boolean', 'string', 'unicode']),
}, required=True)
```

This ensures that any JSON object passed into `validate_params`
must have key `gender` and values `male/female/other`,
and also key `type` and values `boolean/string/unicode`.

Any parameter of other forms will cause the function to throw an error
notifying that the JSON object is malformed.

Useful for servers to verify that a request is well formed.

```py
params1 = {
  'gender': 'female',
  'type': 'boolean',
}
validate_params(params1) # pass

params2 = {
  'gender': 'male',
  'type': 'alien',
}
validate_params(params2) # fail
```

## Data Transformation

According to [these](https://julien.danjou.info/python-schema-validation-voluptuous/)
[articles](https://github.com/alecthomas/voluptuous/issues/124), 
you can exploit Voluptuous to transform the data you pass in.
Though maybe be careful about doing it as the API official documentation
does not explicitly explain how to do data transformations.

```py
from voluptuous import All, In, Schema

def replace_boolean(value):
  if value == 'boolean':
    return 'boolean_special'
  else:
    return value

validate_params = Schema({
  'gender': In(['male', 'female', 'other']),
  'type': All(In(['boolean', 'string', 'unicode']), replace_boolean),
}, required=True)
```

And now the output of `validate_params` will update the `type` value if it is `boolean`.

```py
params3 = {
  'gender': 'male',
  'type': 'boolean',
}
params3 = validate_params(params3)
```
and the output of `params3` is 
```
{
  'gender': 'male',
  'type': 'boolean_special',
}
```








