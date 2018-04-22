---
type: post
title: "git pull: fatal"
date: 2018-04-10
---

When I got `Git pull: fatal: Couldn’t find remote ref refs/heads`,
I tried pruning stale branches in the repo by doing
```
git remote prune origin --dry-run
```
to check which branches would be deleted, then
```
git remote prune origin
```
to delete them.

Though it didn't help - the real reason was because I had been trying to pull someone's
remote branch from the wrong repository. 

See [here](http://bartoz.no-ip.org/archives/3715) for more.

