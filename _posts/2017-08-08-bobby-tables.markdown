---
layout: post
title:  "Little Bobby Tables"
date:   2017-08-07 01:57:45 -0700
---

[Little Bobby Tables](https://xkcd.com/327/)

`MySQLCursor.execute()` does the sanitization for you, mostly.

If you've got a query to run, you may want to do

```python
query = (
  "SELECT id, first_name, last_name, birthday
  FROM my_table"
  "WHERE age < %d"
)
cursor.execute(insert_stmt % 42)
```
since `42` is a number, not a string.

But you should instead do

```python
query = (
  "SELECT id, first_name, last_name, birthday
  FROM my_table"
  "WHERE age < %s"
)
cursor.execute(insert_stmt, [42])
```
to help avoid similar scenarios.

And to make it easier to change to another database,
since the interfaces for various databases mainly follow the
[Python standard database](https://www.python.org/dev/peps/pep-0249/).
































