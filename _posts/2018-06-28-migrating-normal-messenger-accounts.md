---
type: post
title: "Migrating Messenger storage"
date: 2018-06-26
---

Summarized from [here](https://code.facebook.com/posts/201318390519340).

## Messenger at its inception

Originally designed for direct messaging similar to email.

Monolithic service.


## After Messenger started scaling 

* Read-through caching service for queries
* Iris to queue writes to subscribers (e.g. sevices)
* Storage service to retain message history


## Messenger now

Mobile, real-time communications used by individuals and businesses.

* Data schema redesigned and simplified, with consistent invariants 
  to ensure data is formatted correctly
* HBase (key-value store based on HDFS) to MyRocks (integrates RocksDB as a MySQL Storage enginer)


## Challenges during migration

* Ensure users did not experience interruptions during migration
* Migration involved reading historical data on HBase clusters (I/O operations);
  reading to quickly would degrade the performance of HBase.
* A lot of information to migrate, and with the data schema change meant
  lots of parsing existing legacy data and accounting for corner cases
* Rolling out the new database and services required fixing software and hardware bugs.
* Facebook did it by having two migration flows: a normal one for 99.9% of the cases,
  and one for hard-to-migrate accounts.
