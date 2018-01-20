---
type: post
title: "UNIX_TIMESTAMP in MySQL and null date parameters"
date: 2018-01-18
---

`UNIX_TIMESTAMP(datetime)` returns the number of seconds between 1970-01-01 00:00:00 UTC
and `datetime`. Thus `datetime` needs to be a date after Jan 1, 1970, 
such as Jan 18, 2018 for example.

But what happens if you are trying to pass in a `null` date to `UNIX_TIMESTAMP`?
The specs didn't say. They did say that `UNIX_TIMESTAMP()`
with an empty argument returns the current UTC timestamp,
but not what happens when it is passed a null value.
Does it throw an error (that would such, SQL databases often have missing values),
return the time the query was run, etc?

Turns out it just returns a null value when I actually tried it.
Phew. 

