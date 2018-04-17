---
type: post
title: "Readability"
date: 2018-04-11
---

Given a function like this:
```py
def capitalize_person_fields(person):
  new_person = {}
  for field in person:
    new_person[field] = person[field].capitalize() if type(person[field]) == 'string' else person[field]
  return new_person
```

Now suppose I want `capitalize_person_fields` to additionally transform all valid JSON objects 
that have gender `male` to gender `MALE` as well.

One could do this:

```py
def capitalize_person_fields(person):
  new_person = {}
  for field in person:
    if type(person[field]) == 'string':
      new_person[field] = 'MALE' if person[field] == 'male' else person[field].capitalize()
    else:
      new_person[field] = person[field]
  return new_person
```

but this is more readable since transforming just the gender field for a particular value is a one-off event
and should be treated as such:
```py
def capitalize_person_fields(person):
  new_person = {}
  for field in person:
    new_person[field] = person[field].capitalize() if type(person[field]) == 'string' else person[field]
  if new_person.gets('gender') == 'male':
    new_person['gender'] = 'MALE'
  return new_person
```




