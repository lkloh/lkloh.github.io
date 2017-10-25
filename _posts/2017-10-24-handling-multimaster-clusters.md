---
layout: post
title:  "Handling multi-master clusters"
date:   2017-10-24
---

If you're a company need to store large amounts of data for a long time,
(think Fitbit or something)
here are two things you might want to do:
* Store multiple copies of your data in backup locations. 
	A data center in Singapore, one in Europe.
* Use multi-master clusters. Fitbit does have lots of data
	streaming in from their customer's phones after all.

## Unique ID collision on two master nodes

If you're a well known company with lots of users,
somethings you have two master nodes ingesting data at the same time.
Somethings the unique id created for a new piece of incoming data
might even be the same on the two master nodes.
That's going to be a real problem when committing the data,
since now the same piece of data has _two_ unique ids.

## How to mitigate

Before
* Master node 1 creates ids: 1, 2, 3, 4 ...
* Master node 2 creates ids: 1, 2, 3, 4 ...

After
* Master node 1 creates ids: 1, 3, 5, 7, 9, ...
* Master node 2 creates ids: 2, 4, 6, 8, 10, ...

Here's the [article](https://mariadb.org/auto-increments-in-galera/) with more details.
