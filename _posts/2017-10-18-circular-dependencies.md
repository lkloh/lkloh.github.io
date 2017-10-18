---
layout: post
title:  "Circular Dependencies"
date:   2017-10-18
---

There are two dependencies here between `firstname.py` and `fullname.py`
making a cycle.

```
firstname.py
 ---------------------------------
| def get_first_name():           |
|	return get_name.split(' ')[0] |
 ---------------------------------
  ^             |
  |             |
  |             |
  |             |
fullname.py     V
 ----------------------------------
| def get_name():                  |
|   firstname = query_first_name() |
|   return firstname + ' Richman'  |
 ----------------------------------
              |
query.py      V
 ----------------------------------
| def query_first_name():          |
|   // return first name from db   |
 ----------------------------------
```

To avoid circular dependencies, break the cycle 

```
query.py
 ----------------------------------
| def query_first_name():          |
|   // return first name from db   |
 ----------------------------------
                ^
                |
firstname.py    |
 ---------------------------------
| def get_first_name(arr):        |
|	return query_first_name()     |
 ---------------------------------
  ^             
  |             
  |             
  |             
fullname.py     
 ---------------------------------
| def get_name(arr):              |
|   firstname = get_first_name()  |
|   return firstname + ' Richman' |
 ---------------------------------

```














