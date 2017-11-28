---
layout: post
title:  "Check that a python object has attributes first"
date:   2017-10-08
---

Recently I as was to review something along the lines of
```py
// Buggy
if hasattr(person, 'college') and person.college.is_public_college:
  allocate_financial_aid(person)
```

But I forgot to ask them to check that `person.college` also has the attribute `is_public_college`.

What this line really should be is

```py
// Ideal
if hasattr(person, 'college') and hasattr(person.college, 'is_public_college') and person.college.is_public_college:
  allocate_financial_aid(person)
```

The problem with depth has come up more than once, when an object has many attributes that are also objects
with their own subattributes. Perhaps a linter that checks for the "total_depth" of an object can help and complain if there are no adequate checks for that the attribute exists.

## Ideal linter

```py
// Wrong
if person.college.is_public_college:
	allocate_financial_aid(person)
```

warns that user _did not check if attributes exist_

```py
// Ok
if attribute_exists(person.college.is_public_college) and person.college.is_public_college:
	allocate_financial_aid(person)
```


