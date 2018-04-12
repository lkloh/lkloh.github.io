---
type: post
title: "Readability"
date: 2018-04-11
---

Given a schema for JSON like this:
```py
validate = Schema({
  Required('name'): str,
  Require('gender'): In('male', 'FEMALE'),
  Required('ssn'): int,
  Optional('age'): int,
})
```

If I wanted to transform all valid JSON objects 
that have gender `male` to gender `MALE`,
I could either choose to do this:

```py
validate(person)
for field in person:
  person[field] = 'MALE' if field == 'gender' and person.get(field) == 'male' else person.get('gender')
```

but this is likely more readable and efficient:
```py
if person.get('gender') == 'male':
  person['gender'] = 'MALE'
```




