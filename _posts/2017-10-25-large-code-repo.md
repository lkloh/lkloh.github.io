---
layout: post
title:  "Very Large Scale Repo"
date:   2017-10-25
---

I started my first software engineering job on a team of less than 10 people,
with maybe 5 customers.
In grad school, projects rarely had more than 5 people on them at most,
so we avoided merge conflicts by emailing each other
when we were going to work on a file.
Now I work at a place with just less than 100 engineers,
and sometimes merge conflicts can be a huge pain.
There's a pretty large chance someone would do something that affects the 
part of the codebase you're been working on.
But ~100 people, that's still doable right now.

Turns out Googles >25000 software engineers work on the same very large codebase,
developed over almost 20 years.
There's no open source version control system to support that,
so Google had to [write their own](https://cacm.acm.org/magazines/2016/7/204032-why-google-stores-billions-of-lines-of-code-in-a-single-repository/fulltext).

## Main features of Google version control

* Codebase distributed across 10 data centers worldwide
* Caching to hide network latency - London dev pulling files from a server in Amsterdam?
* File-level access control -
	don't want anyone accidentally messing up the accounting data
	if they made a typo in the wrong file when tired.
* Google devs have their own workspace on a cloud storage backend to develop on.
* Create a local copy of files before changing them (i.e. Git clone to workspace).
	Only modified files saved to an individual dev's workspace.

## Trunk based development

All work based on the master repo.
Branches made for a release, but only a few engineers working on the release
can write to the release branch.
Pull requests are still made, but they are short lived (a few days).


