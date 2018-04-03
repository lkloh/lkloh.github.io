---
type: post
title: "Asking someone to re-review a pull request after making requested changes"
date: 2018-04-03
---

Best practice - give them the set of commit hashes to look at after the review.

Otherwise, squashing all the commits from the initial review into one,
and squashing all the commits from review #2 into one would do.
They can just take a look at one commit to see all new changes,
instead of looking at everything again. This saves time and gives them more context.

Best practice is to write meaningful commit messages,
but sometimes my commit messages don't make sense if I went down one path
and had to backtrack out to another to find a solution.
So `git reset --soft HEAD~<number-of-previous-commits-to-squash> && git commit -m 'Squash commits'`
is your friend.



