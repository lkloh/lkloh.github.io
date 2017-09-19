---
layout: post
title:  "Rebasing with master on Git"
date:   2017-08-04 01:57:45 -0700
---

## No conflicts

Lets call your branch `dev`.

`git checkout dev` to go to your branch.

`git fetch` to fetch the updates from master.

`git rebase origin master` to replay your changes on top of what other people have done and 
committed to master.

## With conflicts

After running the last command, you will get an error message saying you can't merge.
Fix ALL the conflicts on the files that git complained about,
and do `git add <path-to-file-with-conflict>` on each file that had conflicts 
(that you just fixed).

Once you have fixed ALL the conflicts in the code base, now you can do
`git commit -m 'Fixed merge conflict'`.
Do not commit before fixing everything.
Afterwards, you should get a message saying that all conflicts are resolved.

And now do `git push origin dev` to get your updated branch reviewed and merged. 
