---
layout: post
title:  "Check that a python object has attributes first"
date:   2017-10-08
---

Recently I as was to review something along the lines of
```py
if hasattr(person, 'college') and person.college.is_public_college:
	allocate_financial_aid(person)
```

But I forgot to ask them to check that `person.college` also 
has the attribute `is_public_college`.

What this line really should be is

```py
if hasattr(person, 'college') and hasattr(person, 'is_public_college') and person.college.is_public_college:
	allocate_financial_aid(person)
```

