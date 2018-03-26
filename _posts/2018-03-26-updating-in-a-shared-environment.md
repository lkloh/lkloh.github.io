---
type: post
title: "Updating dev resources in a shared environment"
date: 2018-03-26
---

## Updating to master on your local repo

Only when necessary - e.g. there is a merge conflict in your pull requests so you
absolutely need to rebase.

## Grabbing a snapshot of production

Only when necessary too -
there is a script that takes the snapshot that could break,
or the production database could have corrupted data since the last time you updated and now.

## Summary

Dev environment is being updated all the time,
may or may not be rigorously tested,
so only rebase when necessary to avoid being
the first to debug a breaking change,
and getting blocked by it.

