---
type: post
title: "Source control at Facebook"
date: 2018-06-10
---

Summarized from [here](https://code.facebook.com/posts/218678814984400/scaling-mercurial-at-facebook/).

## Size of the source code (c. 2014)

* Thousands of commits a week
* > Linux kernel (17 million LOC, 44000 files)
* Deploy twice a day


## c. 2012 

Subversion server with Git mirror.


## Why Facebook stuck to a single repository when the code base was becoming a bottleneck

* Devs often make large changes throughout the (huge) code base.
* Having a single repository is useful for continuous modernization;
  splitting it up makes large refactorings harder.
* Splitting the repo to work for source control is itself not a good reason
  to split the repo.

## Solution: Scale an existing version control system

* Most engineers used Git,
  but in the end Facebook decided that Git was too difficult to work with at scale.
* Decided to scale Mercurial instead, as it is similar in usage and functionality to Git,
* Written in modular Python with native code for hot paths
* Mercurial community was willing to work with Facebook and keep their scale in mind
  when adding new features.


## Improving the performance of Mercurial

* New graph algorithms
* Finding out what files changed within a huge repository.
  * Git examines every file (gonna take a long time at scale).
  * Perforce forces users to tell it which files they are gonna edit (not user-friendly).
  * Made Mercurial monitor the file system for changes,
    by querying the build system's file monitor, Watchman.
* Enabling Watchman make Mercurial about 5x faster than Git.


## Cloning and pulling at scale

### The problem
Given the number of devs at Facebook,
that is a lot of people committing to master at any given time of the day.
Pulling from master is going to take a long time, even if you do it every day.

### Existing solutions
* Subversion is a centralized system that
  works around this by checking out one commit only and leaving all the history on the server,
  but if the server goes down - no more work.
* Git/Mercurial copy all history to the client, but allows a dev to browse and commit locally.

### Improving for scale
* During a pull, Mercurial figures out what changed on the server since the last pull,
  and downloads new commit metadata and file contents.
  (This takes a long time at Facebook's scale).
* Facebook created an extension called remotefilelog,
  which causes clone and pull to download _only commit metadata_,
  and _omit file changes_.
* File changes are only downloaded on demand using memcache.
* Downloading file changes lazily ensures clone and pull are fast.

### Downtime: when the central Mercurial server goes down
* Remotefilelog caches file revisions needed for a dev's local commits 
  so they can checkout and commit without needing access to the server.
* Operations that do not need file contents (e.g. `log`) are local.
* Memcache is a caching layer in front of the central Mercurial server 
  to continue to serve most file content requests even if the central repository goes down.
* Of course this assumes you have a fast, reliable Internet connection.

### Performance gains
* Clone and pull are 10x faster when lazily obtaining file content.
* Large rebases are 2x faster due to the way local data on disk is stored.














