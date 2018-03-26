---
type: post
title: "Disabling git force push to master in a shared repo"
date: 2018-03-22
---

Disabling git force push to master branch in a shared repository is a good idea
as a force push would override remote changes made by team members to the master branch,
potentially destroying other people's hard work if you're not careful.

Thus if you accidentally made the wrong commit to master,
use `git log` to get the commit hash you want to undo, then do
`git revert <commit-hash-I-want-to-get-rid-of>`.

To disable git force on a branch, an admin can protect the branch 
as described [here](https://help.github.com/articles/defining-the-mergeability-of-pull-requests/).


