---
layout: post
title:  "Leaky abstractions mean you must understand the underlying implementation"
date:   2017-10-12
---

Here's a nice [post](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/) 
about various leaky abstractions.

One of example is this SQL table with the schema:
```
my_table
--------
* user_name PRIMARY KEY
* first_name
* last_name
* birthday
```

Depending on the database you are using,
both queries below get rows beloning to people called "John". 

But 

```
SELECT *
FROM (SELECT user_name FROM my_table WHERE first_name = 'John') as john_table
WHERE user_name = john_table.user_name;
```

is a lot faster than

```
SELECT *
FROM my_table
WHERE first_name = 'John'
```

because of leaky abstractions.

The first query gets the usernames of people called "John",
then pulls out all the rows belonging to them.

The second one directly retrieves rows belonging to people called "John".

So how you do stuff impacts performance,
even when it shouldn't matter.
The blackbox isn't really a blackbox, just a toolkit.







