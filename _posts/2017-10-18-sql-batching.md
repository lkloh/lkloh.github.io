---
layout: post
title:  "SQL Batching"
date:   2017-10-18
---

Big-O doesn't describe the fixed costs of each SQL query,
which likely involves a network call to the database.
To save time, try to batch related SQL queries in one query.

## SELECT

* Indexed db: `O(log n)` to search
* Non-indexed db: `O(n)` to search

## INSERT

* Indexed db: `O(log n)` to add in the right place
* Non-indexed db: `O(1)` to append to the end of the db

## UPDATE

* Indexed db: `O(log n)` to search for the row to update
* Non-indexed db: `O(n)` to search for the right row to update

## JOIN

* Profile how long it takes to run the query
* Profile against different loads - query optimizers use different algorithms depending on load

Thanks [Stack Overflow](https://stackoverflow.com/questions/1347552/what-is-the-big-o-for-sql-select).



