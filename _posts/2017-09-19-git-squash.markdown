---
layout: post
title:  "Git Squash"
date:   2017-09-19 11:05:37 -0700
---

It's probably a lot easier to squash lots of commits together,
than have a huge git workflow.
Suppose you checked out a branch called `dev`,
and made 5 commits to it.
Now you want those 5 commits to be merge to 1 on your branch.
The best way to do this is:

```
git reset --soft HEAD~5 &&
git commit
```

You'll need to write a new commit message.
Things will be harder if you want all of your old commit messages to be
prepopulated.
But why would you need that unless your branch is trying to accomplish `x` 
different tasks at the same time?
Even if it is, there's probably a way to 
rephrase what you're doing in a more concise way.

Thanks [Stack Overflow](https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git)!